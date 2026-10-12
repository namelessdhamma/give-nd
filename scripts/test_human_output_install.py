#!/usr/bin/env python3
"""Run real installed-file and executable cycle-policy tests in isolated clean build.
SOURCE_ONLY: does not claim fresh ChatGPT host, Ksyusha account, or real Writer invocation.
"""
from __future__ import annotations
import importlib.util
import json
import pathlib
import subprocess
import sys
import tempfile

ROOT=pathlib.Path(__file__).resolve().parents[1]
checks=0
def demand(value, reason):
    global checks
    checks+=1
    if not value: raise AssertionError(reason)

bundle=json.loads((ROOT/"plugin-export-current/nd-automation-agent.json").read_text(encoding="utf-8"))
manifest=json.loads((ROOT/"PLUGIN_EXPORT_CURRENT_MANIFEST.json").read_text(encoding="utf-8"))
demand(bundle["version"]=="1.7.8","Plugin version must equal observed installed version")
demand(bundle["current_release_id"]=="pluginrel_6acc996feb988191b8a499ac681b2828","Installed release provenance")
demand(len(bundle["contents"])==len(bundle["text_files"])==12,"12 exact installed files")
demand(set(bundle["contents"])=={f["path"] for f in bundle["text_files"]},"Installed path parity")
demand(all(len(v.encode("utf-8"))==next(f["size_bytes"] for f in bundle["text_files"] if f["path"]==k) for k,v in bundle["contents"].items()),"Source-file exact byte sizes")
record=next(v for v in manifest["files"] if v["name"]=="nd-automation-agent.json")
demand(record["source_version"]==bundle["version"] and record["source_release"]==bundle["current_release_id"],"Manifest selection parity")
name="skills/nd-launch-automation-agent/"
policy=bundle["contents"][name+"references/MESSAGE_POLICY.md"]
launcher=bundle["contents"][name+"SKILL.md"]
demand("SILENT_CONTINUE" in policy and "SILENT_CONTINUE" in launcher,"Default silence")
demand("no OUTCOME_UNKNOWN" in policy and "observed auto-reentry surface" in policy,"Committed cycle safety")
demand("Never ask routine " in policy and "Go" in policy,"Never force Go")
demand("Do not force a compression ratio" in policy and "keep the full relevant content" in policy,"No fixed compression or essential information loss")
for term in ["uncertainty","safety warnings","provenance","unresolved failures"]:
    demand(term in policy,"Preserve meaningful content: "+term)
for term in ["MAY use CURRENT True Writer","optional bounded editorial","PEER_SERVICE","original substantive owner","Writer follows its existing Child and Literary Critic process","No new Writer call is justified solely for brevity"]:
    demand(term in policy,"Editorial optionality/invariant: "+term)
demand("Skip optional editorial calls for routine progress, simple answers, raw evidence, urgent incidents" in policy,"No routine Writer invocation")
demand("This is presentation guidance only" in policy,"Presentation-only boundary")
demand("ANTI_HANG_LAUNCHER_URI" in launcher and "TASK_ENTRY" in launcher and "USER_STOP" in launcher,"Anti-Hang hook identity retained")
demand("continue_after_material_return" in launcher,"Agent autonomous continuation unchanged")

# Isolated install: actually execute the repository's target-builder on a fresh temp tree.
source_bm=json.loads((ROOT/"BINDING_MAP_TEMPLATE.json").read_text(encoding="utf-8"))
for i,(key,val) in enumerate(source_bm["navigator_rebind"].items(),1):
    val["target_identifier"]="KSY-TEST-"+str(i)
    val["target_url"]="https://linear.app/ksyusha/issue/KSY-TEST-"+str(i)
for i,val in enumerate(source_bm["semantic_workspaces"].values(),1):
    val["target"]="TARGET-KSYUSHA-SEMANTIC-"+str(i)
for key in ("target_drive_system_root","target_registry_file","target_supabase_project","target_github_repo"):
    source_bm["provider_bindings"][key]="TARGET-CLEAN-BUILD-"+key
with tempfile.TemporaryDirectory(prefix="nd-human-output-clean-") as tmp:
    td=pathlib.Path(tmp)
    binding_file=td/"target-bindings.json"
    binding_file.write_text(json.dumps(source_bm,ensure_ascii=False),encoding="utf-8")
    result=subprocess.run([sys.executable,str(ROOT/"build_target_plugin.py"),str(ROOT/"plugin-export-current/nd-automation-agent.json"),str(binding_file),str(td/"installed")],
        capture_output=True,text=True,timeout=30)
    demand(result.returncode==0,"Real target-builder clean install failed: "+result.stderr[-1000:]+result.stdout[-1000:])
    dest=td/"installed"/"nd-automation-agent"
    report=json.loads((dest/"ND_TARGET_BUILD_REPORT.json").read_text())
    demand(report["status"]=="BUILT_PROVIDER_REBIND_ONLY" and report["file_count"]==12,"Target clean build receipt")
    installed_policy=(dest/name/"references/MESSAGE_POLICY.md").read_text(encoding="utf-8")
    demand(installed_policy==policy,"Installed MESSAGE_POLICY exact source content")
    installed_script=dest/name/"scripts/message_policy.py"
    demand(installed_script.read_text(encoding="utf-8")==bundle["contents"][name+"scripts/message_policy.py"],"Installed executable script exact source content")
    spec=importlib.util.spec_from_file_location("nd_target_cycle_policy",installed_script)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cb=module.cycle_boundary
    for i in range(100):
        demand(cb(material_cycle_complete=True,material_continuation=True)=="SILENT_CONTINUE","Internal subcycle must stay silent #"+str(i))
    demand(cb(material_cycle_complete=False,material_continuation=True,significant_milestone=True)=="SILENT_CONTINUE","Non-material boundary cannot force visible output")
    demand(cb(material_cycle_complete=True,material_continuation=True,user_requested_progress=True)=="VISIBLE_PROGRESS_AUTO_CONTINUE","Requested progress possible")
    demand(cb(material_cycle_complete=True,material_continuation=True,important_finding_or_blocker=True)=="VISIBLE_PROGRESS_AUTO_CONTINUE","Material blocker can surface")
    demand(cb(material_cycle_complete=True,material_continuation=True,external_wait_transition=True)=="VISIBLE_PROGRESS_AUTO_CONTINUE","True external wait can surface")
    demand(cb(material_cycle_complete=True,material_continuation=True,result_direction_changed=True)=="VISIBLE_PROGRESS_AUTO_CONTINUE","Material direction change can surface")
    demand(cb(material_cycle_complete=True,material_continuation=True,significant_milestone=True,readback_complete=True,continuation_compacted=True,observable_local_result=True,next_frontier=True,auto_reentry_surface_observed=False)=="VISIBLE_PROGRESS_AUTO_CONTINUE","No claimed committed re-entry without observed surface")
    demand(cb(material_cycle_complete=True,material_continuation=True,significant_milestone=True,readback_complete=True,continuation_compacted=True,observable_local_result=True,next_frontier=True,auto_reentry_surface_observed=True)=="COMMITTED_CYCLE_AUTO_REENTER","Verified auto-entry condition executable")
    demand(cb(material_cycle_complete=True,material_continuation=True,significant_milestone=True,readback_complete=True,continuation_compacted=True,observable_local_result=True,next_frontier=True,auto_reentry_surface_observed=True,outcome_unknown=True)=="VISIBLE_PROGRESS_AUTO_CONTINUE","Unknown effects cannot be committed")
    demand(cb(material_cycle_complete=True,material_continuation=True,recovery_anchor_needed=True,readback_complete=True,continuation_compacted=True,observable_local_result=True,next_frontier=True,auto_reentry_surface_observed=True)=="COMMITTED_CYCLE_AUTO_REENTER","Recovery anchor re-entry verified")
print(json.dumps({"verdict":"PASS","checks":checks,"tested":"exact installed Agent 1.7.8 package, isolated fresh target-built files, real cycle_boundary execution and policy contract","target_owner_account":"NOT_RUN","fresh_ChatGPT_session":"NOT_RUN","physical_editor_peer":"NOT_RUN"},ensure_ascii=False))
