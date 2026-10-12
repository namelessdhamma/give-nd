#!/usr/bin/env python3
"""Stage U public package regression tests; these are NOT Ksyusha target acceptance tests."""
import copy
import hashlib
import importlib.util
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("stage_u", ROOT/"scripts/plan_stage_u.py")
stage_u = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stage_u)
source = json.loads((ROOT/"canonical-artifacts/ND_CAPABILITY_REGISTRY_KSYUSHA_SCOPE_FROM_v1_66_1.json").read_text(encoding="utf-8"))
target = copy.deepcopy(source)
target["version"] = "1.64.2"
target["components"] = [x for x in target["components"] if x["component_key"] != "SONGWRITER"]
target["runtime_invocation_bindings"]["launchers"] = [x for x in target["runtime_invocation_bindings"]["launchers"] if x["component_key"] != "SONGWRITER"]
target["runtime_invocation_bindings"]["launcher_count"] = 22
head = {"identifier": "XEN-5", "registry_id": "TARGET-FIXTURE-REGISTRY-OLD", "registry_id_readback": "TARGET-FIXTURE-REGISTRY-OLD", "registry_version":"1.64.2","registry_sha256":"a"*64,"anchor":"FIXTURE-OLD-ANCHOR"}
count = 0
def check(c, name):
    global count
    count += 1
    if not c:
        raise AssertionError(name)
before=json.dumps(target,sort_keys=True)
result=stage_u.analyze(target,source,head)
check(result["status"]=="READ_ONLY_PLAN_NOT_AN_INSTALLATION_OR_QUALIFICATION", "only planning")
check(result["target_statehead"]=="XEN-5" and result["old_anchor_present"], "old root retained")
check(result["target_counts"] == {"components":31,"launchers":22}, "31/22 target")
check(result["source_scoped_counts"] == {"components":32,"launchers":23}, "32/23 source")
check(result["songwriter_missing"] is True, "missing Songwriter explicitly detected")
check(result["missing_component_keys"]==["SONGWRITER"], "only one added component")
check(result["missing_launcher_keys"]==["SONGWRITER"], "only one added launcher")
check(result["known_user_report_31_22_match"], "matches reported target inventory")
check(set(result["gates"].values()) == {"NOT_RUN"}, "fixture not false PASS")
check(json.dumps(target,sort_keys=True)==before, "no target mutation")
check("nd-automation-agent" in result["mandatory_packages"] and "nd-anti-hang" in result["mandatory_packages"], "cumulative package includes agent and anti-hang")
check("nd-songwriter" in result["mandatory_packages"] and "nd-true-writer" in result["mandatory_packages"], "cumulative package includes writer and songwriter")
try:
    stage_u.analyze(target,source,{**head,"identifier":"NAM-143"})
    raise AssertionError("invalid owner accepted")
except ValueError:
    count+=1
try:
    stage_u.analyze(target,source,{**head,"registry_id_readback":"SAVVA-ID"})
    raise AssertionError("unverified current anchor accepted")
except ValueError:
    count+=1
try:
    stage_u.analyze(target,source,{**head,"anchor":None})
    raise AssertionError("missing anchor accepted")
except ValueError:
    count+=1
try:
    stage_u.analyze(target,source,{**head,"registry_version":"1.66.1"})
    raise AssertionError("wrong target Registry version accepted")
except ValueError:
    count+=1
with_audio = copy.deepcopy(source)
with_audio["components"].append({"component_key":"TRUE_SOUND"})
try:
    stage_u.analyze(target,with_audio,head)
    raise AssertionError("source audio accepted")
except ValueError:
    count+=1
audio_target=copy.deepcopy(target)
audio_target["components"].append({"component_key":"TRUE_SOUND"})
try:
    stage_u.analyze(audio_target,source,head)
    raise AssertionError("target audio accepted")
except ValueError:
    count+=1
current_head={**head,"registry_version":"1.66.1"}
all_current=stage_u.analyze(source,source,current_head)
check(all_current["missing_component_keys"]==[] and all_current["missing_launcher_keys"]==[], "idempotent no missing component")
check(all_current["songwriter_missing"] is False, "no reinstall of already installed songwriter")
check(not all_current["known_user_report_31_22_match"], "fresh readback overrides old user report")
doc=(ROOT/"UPDATE_IN_PROGRESS.md").read_text(encoding="utf-8")
for clause in ("XEN-5", "Registry1.64.2","1.7.8","1.7.0","0.2.3","1.0.6","Stage U1","Stage U2","Stage U3","Stage U4","Stage U5","SILENT_CONTINUE","OUTCOME_UNKNOWN","Literary Critic","HUMAN_OUTPUT_INSTALLATION_GATE_STAGE06.json","ANTI_HANG_INSTALLATION_GATE_STAGE06.json","STAGE_U_COLD_QUALIFICATION.json", "FULL_STAGE08_PASS", "raw.githubusercontent.com"):
    check(clause in doc,"missing procedural invariant "+clause)
bundle=json.loads((ROOT/"plugin-export-current/nd-automation-agent.json").read_text(encoding="utf-8"))
check(bundle["version"]=="1.7.8", "real updated package selected")
check(bundle["contents"]["skills/nd-launch-automation-agent/references/MESSAGE_POLICY.md"].count("PEER_SERVICE")>=1,"editorial peer in installed policy")
check((ROOT/"ANTI_HANG_INSTALLATION_GATE.md").is_file(), "anti-hang standalone gate readable in public source")
check((ROOT/"HUMAN_OUTPUT_INSTALLATION_GATE.md").is_file(), "human-output standalone gate readable in public source")
check((ROOT/"plugin-export-current/nd-songwriter.json").is_file(), "songwriter source bundle included")
print(json.dumps({"verdict":"PASS","checks":count,"failures":0,"scope":"STAGE_U_SOURCE_FIXTURE_AND_READ_ONLY_PLAN_ONLY","target_provider_installed":"NOT_RUN","target_stage08":"NOT_RUN"},ensure_ascii=False))
