#!/usr/bin/env python3
"""Deterministic verification of the public, NONAUTHORITATIVE ND->Ksyusha source package."""
from __future__ import annotations
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
errors: list[str] = []
checks: list[str] = []

def check(cond, label):
    (checks if cond else errors).append(label)

def load(p):
    return json.loads((ROOT / p).read_text(encoding="utf-8-sig"))

def sha256(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()

def blobsha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\x00" + data).hexdigest()

def run():
    manifest = load("PUBLIC_PACKAGE_MANIFEST.json")
    qual = load("PUBLIC_PACKAGE_QUALIFICATION.json")
    scope = load("canonical-artifacts/ND_CAPABILITY_REGISTRY_KSYUSHA_SCOPE_FROM_v1_66_1.json")
    inv = load("canonical-artifacts/COMPONENT_INVENTORY.json")
    bundle_manifest = load("PLUGIN_EXPORT_CURRENT_MANIFEST.json")
    binds = load("BINDING_MAP_TEMPLATE.json")
    selectable = load("SELECTABLE_SET_CURRENT.json")
    expected = {x["path"]: x for x in manifest["files"]}
    actual = {str(p.relative_to(ROOT)).replace("\\", "/"): p for p in ROOT.rglob("*")
              if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts
              and str(p.relative_to(ROOT)).replace("\\", "/") != "PUBLIC_PACKAGE_MANIFEST.json"}
    check(set(expected) == set(actual),
          "fileset exact match (missing: %s; extra: %s)" %
          (sorted(set(expected)-set(actual)), sorted(set(actual)-set(expected))))
    for name in sorted(set(expected) & set(actual)):
        data = actual[name].read_bytes()
        check(expected[name]["size_bytes"] == len(data) and expected[name]["blob_sha"] == blobsha(data),
              "manifest raw blob/size parity: "+name)

    real_count = len(actual)+1
    check(manifest["counts"]["total_files"] == real_count, "public file count")
    check(manifest["counts"]["plugin_bundles"] == 23, "manifest 23 plugin bundles")
    check(manifest["counts"]["stage_files"] == 8, "exact 8 original stages")
    check(manifest["counts"].get("standalone_update_stage_u") == 1, "one standalone cumulative update Stage U")
    check(manifest["counts"]["anti_hang_installation_gates"] == 1, "one shared Anti-Hang gate")
    check(manifest["counts"].get("human_output_installation_gates")==1, "one additional Human Output gate")
    check(manifest["total_payload_bytes"] == sum(p.stat().st_size for p in actual.values()), "total bytes")

    source_hash = "1da459ac1027e234b5d1860625e3b79fb7ca8b0d574ffbc0b739941fa438cc71"
    excluded = {"TRUE_SOUND", "STUDIO_EXECUTOR", "SOUND_CRITIC"}
    check(scope["transfer_scope"]["source_raw_sha256"] == source_hash, "source hash pinned")
    check(scope["status"].startswith("SOURCE_SCOPED_TRANSFER_CANDIDATE"), "scope not target authority")
    check(scope["transfer_scope"]["source_provider_bindings"].startswith("NONSELECTABLE"), "source IDs are not target authority")
    check("audio_domain_adoption" not in scope, "no audio-domain adoption payload")
    check(len(scope["components"]) == 32 and len(scope["runtime_invocation_bindings"]["launchers"]) == 23, "32/23 scope")
    check(scope["runtime_invocation_bindings"]["launcher_count"] == 23, "launcher binding count")
    check(excluded.isdisjoint({c["component_key"] for c in scope["components"]}), "no audio components")
    check(excluded.isdisjoint({c["component_key"] for c in scope["runtime_invocation_bindings"]["launchers"]}), "no audio launchers")
    for k in ["resolution_rules","validation_infrastructure","durable_pipeline","post_t4_memory_migration_convergence",
              "semantic_core_adoption","mandatory_hook_enforcement_20261003","autonomous_internal_continuation_20261010"]:
        check(k in scope, "full source system-contract section: "+k)

    graph = [x.strip() for x in (ROOT/"LAUNCHER_GRAPH_CURRENT.txt").read_text().splitlines()
             if re.match(r"^\d{2} \| ", x)]
    listed_uris = [x.split(" | ")[4] for x in graph]
    bound_uris = [x["launcher_uri"] for x in scope["runtime_invocation_bindings"]["launchers"]]
    check("ND_CAPABILITY_REGISTRY 1.66.1" in (ROOT/"CURRENT_POINTER.txt").read_text(), "current source pointer is 1.66.1")
    check("Registry 1.66.0" not in (ROOT/"CURRENT_POINTER.txt").read_text(), "no stale 1.66.0 pointer")
    check("1.66.1" in (ROOT/"LAUNCHER_GRAPH_CURRENT.txt").read_text().splitlines()[0], "launcher graph source authority 1.66.1")
    check("1.7.8_TARGET_CANDIDATE_NOT_SOURCE_BOUND" in (ROOT/"LAUNCHER_GRAPH_CURRENT.txt").read_text(), "source bound 1.7.5 vs new target candidate 1.7.8")
    check("KSYUSHA_RUNTIME_RECOVERY.md" in selectable["current_control"], "target runtime gate recovery is current")
    check("ALL_PLUGIN_LAUNCHERS_GATE.md" in selectable["current_control"], "all ND role plugins target gate selected")
    check("scripts/test_all_plugin_launchers.py" in selectable["current_control"], "all launcher build audit selected")
    check(len(graph) == len(set(listed_uris)) == 23 and set(listed_uris) == set(bound_uris),
          "23/23 exact launcher URI parity")
    check([int(x.split(" | ")[0]) for x in graph] == list(range(1,24)), "graph ordinals 01-23")
    parents = {x["component_key"]: x.get("structural_parent_launcher_uri") for x in scope["runtime_invocation_bindings"]["launchers"]}
    check(parents.get("SONGWRITER") == "skills://plugins/nd-true-writer/nd-launch-true-writer",
          "Songwriter Child parent")
    check(inv["component_count"] == 32 and {x["key"] for x in inv["components"]}
          == {x["component_key"] for x in scope["components"]}, "component inventory scope")

    files = bundle_manifest["files"]
    check(len(files) == len({x["name"] for x in files}) == 23, "23 unique source plugin bundles")
    check(len(binds["plugin_bindings"]) == 23, "23 target plugin binding slots")
    check("nd-songwriter" in binds["plugin_bindings"], "target songwriter rebind")
    check("ANTI_HANG_INSTALLATION_GATE.md" in selectable["current_control"], "gate selected")
    check("HUMAN_OUTPUT_INSTALLATION_GATE.md" in selectable["current_control"], "Human Output gate selected")
    check("UPDATE_IN_PROGRESS.md" in selectable["current_control"], "Stage U entry selected")
    check("KSYUSHA_FINISH_INSTALL.md" in selectable["current_control"], "new final Ksyusha prompt selected")
    check("KSYUSHA_RUNTIME_RECOVERY.md" in selectable["current_control"], "runtime visibility recovery selected")
    check("scripts/test_runtime_recovery_contract.py" in selectable["current_control"], "source runtime recovery test selected")
    check("scripts/plan_stage_u.py" in selectable["current_control"], "Stage U planner selected")
    check("scripts/test_stage_u.py" in selectable["current_control"], "Stage U offline regression selected")
    check("scripts/test_human_output_install.py" in selectable["current_control"], "Human Output executable selected")
    check("SOURCE_STAGED_INSTALLATION_CLOSURE_RECEIPT.json" in selectable["nonselectable_provenance"], "old receipt nonselectable")
    check(qual["overall_verdict"] in ("SOURCE_VERIFIED_PASS_TARGET_NOT_RUN","SOURCE_CANDIDATE_PENDING_NEW_RUN_TARGET_NOT_RUN","SOURCE_CANDIDATE_PENDING_STAGE_U_CI_TARGET_NOT_RUN"), "source honestly scoped; target NOT_RUN")
    check(qual["checks"]["anti_hang_stage06_target"].startswith("NOT_RUN"), "stage06 not falsely passed")
    check(qual["checks"]["anti_hang_stage08_target"].startswith("NOT_RUN"), "stage08 not falsely passed")
    check(qual["checks"].get("human_output_stage06_target")=="NOT_RUN", "Human Output Stage06 not falsely passed")
    check(qual["checks"].get("human_output_stage08_target")=="NOT_RUN", "Human Output Stage08 not falsely passed")
    check(qual["checks"].get("stage_u_target_prepublication")=="NOT_RUN", "Stage U prepublication not falsely passed")
    check(qual["checks"].get("stage_u_target_publication")=="NOT_RUN", "Stage U target XEN-5 cutover not falsely passed")
    check(qual["checks"].get("stage_u_target_cold")=="NOT_RUN", "Stage U cold not falsely passed")
    check(qual["source_evidence"]["exact_current_source_plugin_versions"]["nd-automation-agent"]=="1.7.8", "installed 1.7.8 selected")

    for f in files:
        p = "plugin-export-current/" + f["name"]
        check(p in actual, "bundled plugin present: "+p)
        if p not in actual:
            continue
        bundle = load(p)
        contents = bundle["contents"]
        check(bundle["schema"] == "ND_PLUGIN_SOURCE_BUNDLE_v1"
              and bundle["version"] == f["source_version"]
              and bundle["current_release_id"] == f["source_release"]
              and len(contents) > 0, "bundle metadata parity: "+p)
        check(f["blob_sha"] == blobsha((ROOT/p).read_bytes()), "plugin manifest SHA: "+p)

    # True current canonical bytes verified independently against CURRENT NAM-143+Drive.
    canonical = {
        "canonical-artifacts/system/ND_AUTOMATION_AGENT_v1_3_5_AUTONOMOUS_CONTINUATION.md": "4c2255cfc41df28054b892e077b7b8edb0119d05459491290278801855529993",
        "canonical-artifacts/components/ANTI_HANG_RUNTIME/ND_ANTI_HANG_RUNTIME_v1_7_0_SCOPED_OWNED_BOUNDARY.json": "76683264bda8c504f501ecdf93cf87f0267fb2fd220d58c3b7eb5ecb8823ae5f",
        "canonical-artifacts/components/TRUE_WRITER/ND_True_Writer_v0_9_3_SONGWRITER_CHILD_CANONICAL.md": "6336ffef4964cabe1a6772d18860ab437e71e6e4dc3379ff87ad9a92bfc05f0c",
        "canonical-artifacts/components/WRITER_ORCHESTRA_RUNTIME/ND_Writer_Orchestra_Runtime_v1_0_6_SONGWRITER.md": "a21c0c0f6f5f3cfc16d2c2f3bba51472c16bf217187625a83141e7d453f79ea2",
        "canonical-artifacts/components/SONGWRITER/ND_Songwriter_v0_2_3_CANONICAL_SKILL.md": "920ebc9daa21d754dffddad0eca28ee4c4c929c5fc794644e20e729ccdcda3ab",
    }
    for p,h in canonical.items():
        check(sha256(p)==h, "canonical source SHA-256 exact: "+p)

    # No high-confidence credentials/personal email in any public file (including provenance files).
    patterns = [
        re.compile(rb"sk-proj-[A-Za-z0-9_-]{15,}"),
        re.compile(rb"sk-[A-Za-z0-9_-]{32,}"),
        re.compile(rb"ghp_[A-Za-z0-9]{35,}"),
        re.compile(rb"github_pat_[A-Za-z0-9_]{35,}"),
        re.compile(rb"AKIA[A-Z0-9]{16}"),
        re.compile(rb"AIza[A-Za-z0-9_-]{30,}"),
        re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(rb"xox[baprs]-[A-Za-z0-9-]{18,}"),
        re.compile(rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    ]
    for p in sorted(actual.values()):
        b = p.read_bytes()
        # The verifier necessarily contains patterns as source literals; skip its own text only.
        if p.name == "verify_transfer.py":
            continue
        for regex in patterns:
            if regex.search(b):
                errors.append("HIGH_CONFIDENCE_PUBLIC_SECRET_OR_EMAIL_IN "+str(p.relative_to(ROOT)))
                break
    checks.append("public credential/email scan performed")

    # Builder source-level functional smoke test for every transferred plugin, not only metadata.
    synthetic = json.loads(json.dumps(binds))
    for i,(key, binding) in enumerate(synthetic["navigator_rebind"].items(),start=1):
        binding["target_identifier"] = "KSY-"+str(i)
        binding["target_url"] = "https://linear.app/ksyusha/issue/KSY-"+str(i)
    for i, item in enumerate(synthetic["semantic_workspaces"].values(),start=1):
        item["target"] = "TARGET-KSYUSHA-NOTEBOOK-"+str(i)
    for key in ("target_drive_system_root","target_registry_file","target_supabase_project","target_github_repo"):
        synthetic["provider_bindings"][key]="TARGET-TEST-ONLY-"+key
    with tempfile.TemporaryDirectory(prefix="nd-ksyusha-") as temp:
        bfile = pathlib.Path(temp)/"bindings.json"
        bfile.write_text(json.dumps(synthetic),encoding="utf-8")
        for f in files:
            source = ROOT/"plugin-export-current"/f["name"]
            command = [sys.executable,str(ROOT/"build_target_plugin.py"),str(source),str(bfile),temp]
            proc = subprocess.run(command,text=True,capture_output=True,timeout=20)
            check(proc.returncode==0, "target builder executed for "+f["name"]+
                  (" ERROR: "+proc.stderr[-300:]+proc.stdout[-300:] if proc.returncode else ""))
            if proc.returncode == 0:
                report = pathlib.Path(temp)/f["name"].removesuffix(".json")/"ND_TARGET_BUILD_REPORT.json"
                check(report.exists() and json.loads(report.read_text())["status"]=="BUILT_PROVIDER_REBIND_ONLY",
                      "builder report "+f["name"])

    outcome = {"verdict":"PASS" if not errors else "FAIL", "checks":len(checks),
               "failures":len(errors), "findings":errors[:120],
               "scope":"SOURCE_STATIC_AND_BUILDER_ONLY__NOT_TARGET_STAGE06_OR_STAGE08"}
    print(json.dumps(outcome,ensure_ascii=False,indent=2))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    run()
