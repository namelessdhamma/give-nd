#!/usr/bin/env python3
"""Source-only regression: no stale launcher authority or logically impossible Stage U gate."""
import json
import pathlib
import re
root=pathlib.Path(__file__).resolve().parents[1]
checks=[]
def ck(value,name):
    if not value: raise AssertionError(name)
    checks.append(name)
def rd(name):return (root/name).read_text(encoding="utf-8")
source=json.loads(rd("canonical-artifacts/ND_CAPABILITY_REGISTRY_KSYUSHA_SCOPE_FROM_v1_66_1.json"))
g=rd("LAUNCHER_GRAPH_CURRENT.txt")
pointer=rd("CURRENT_POINTER.txt")
anti=rd("ANTI_HANG_INSTALLATION_GATE.md")
docs={n:rd(n) for n in ["KSYUSHA_RUNTIME_RECOVERY.md","KSYUSHA_FINISH_INSTALL.md","START_HERE.md","UPDATE_IN_PROGRESS.md","06_REGISTRY_PREPUBLICATION.md","07_STATEHEAD_PUBLICATION.md","08_COLD_QUALIFICATION.md","QUALIFICATION.md"]}
ck("1.66.1" in pointer and "1.66.0" not in pointer,"CURRENT pointer source exact")
ck("1.66.1" in g.splitlines()[0] and "1.66.0" not in g,"launcher graph exact source")
ck("1.66.1" in anti and "1.66.0" not in anti,"anti-hang gate exact source")
ck("1.7.8_TARGET_CANDIDATE_NOT_SOURCE_BOUND" in g,"no false upstream adoption")
ck("1.7.5" in pointer and "1.7.8" in pointer,"source bound versus selected delta")
ck("1.7.5" in anti and "1.7.8" in anti,"gated source and target release distinction")
ck("SOURCE" in g.splitlines()[0] and "NONAUTHORITATIVE" in g.splitlines()[0],"no source root target claim")
entries=[x for x in g.splitlines() if re.match(r"^\d\d \| ",x)]
ck(len(entries)==23 and len(source["runtime_invocation_bindings"]["launchers"])==23,"23 transfer launchers")
ck({x.split(" | ")[4] for x in entries}=={x["launcher_uri"] for x in source["runtime_invocation_bindings"]["launchers"]},"exact URI parity")
ck(source["runtime_invocation_bindings"]["launcher_count"]==23,"source scoped launcher count")
ck(source["runtime_invocation_bindings"]["launchers"][0]["qualified_plugin_version"]=="1.7.5","source Registry remains unaltered")
ck("CANDIDATE" in docs["KSYUSHA_RUNTIME_RECOVERY.md"] and "NONCURRENT" in docs["KSYUSHA_RUNTIME_RECOVERY.md"],"candidate stage not source current")
ck("U3a" in docs["KSYUSHA_RUNTIME_RECOVERY.md"] and "U3b" in docs["KSYUSHA_RUNTIME_RECOVERY.md"] and "U5" in docs["KSYUSHA_RUNTIME_RECOVERY.md"],"gates logically staged")
ck("host" in docs["KSYUSHA_FINISH_INSTALL.md"].lower(),"host blocker prioritized")
ck("Do not reinstall" in docs["KSYUSHA_FINISH_INSTALL.md"],"four packages preserved")
ck("NOT_RUN" in docs["KSYUSHA_FINISH_INSTALL.md"],"runtime no false pass")
ck("blocked" in docs["KSYUSHA_RUNTIME_RECOVERY.md"].lower(),"true gate allowed")
ck("Plugin Creator" in docs["KSYUSHA_RUNTIME_RECOVERY.md"] and "SKILL_LOADED" in docs["KSYUSHA_RUNTIME_RECOVERY.md"],"plugin versus host exposure differentiated")
ck("ChatGPT" in docs["KSYUSHA_RUNTIME_RECOVERY.md"],"host surface explicit")
ck("Stage08" in docs["KSYUSHA_FINISH_INSTALL.md"],"physical cold targeted")
ck("SILENT_CONTINUE" in docs["KSYUSHA_FINISH_INSTALL.md"],"internal cycle model retained")
ck("Stage06 BLOCKED" in docs["06_REGISTRY_PREPUBLICATION.md"],"not bypass current host")
ck("after U4" in docs["KSYUSHA_RUNTIME_RECOVERY.md"] or "after guarded publication" in docs["KSYUSHA_RUNTIME_RECOVERY.md"],"postpublication cold boundary")
ck("Stage08" in docs["08_COLD_QUALIFICATION.md"],"cold gate intact")
ck("1.66.1" in docs["QUALIFICATION.md"] and "Current source 1.66.0" not in docs["QUALIFICATION.md"],"qualification version repaired")
ck("NOT_RUN" in docs["KSYUSHA_RUNTIME_RECOVERY.md"],"target proof honestly pending")
print(json.dumps({"verdict":"PASS","checks":len(checks),"failures":0,"scope":"SOURCE_RUNTIME_HANDOFF_INVARIANTS_ONLY__NOT_TARGET_CHATGPT_QUALIFICATION"}))
