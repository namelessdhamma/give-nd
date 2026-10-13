#!/usr/bin/env python3
"""Audit the full ND->Ksyusha plugin-launcher packaging and owner hierarchy.

SOURCE ONLY: the Ksyusha account/provider/ChatGPT host is not queried here.
"""
from __future__ import annotations
import json
import pathlib

ROOT=pathlib.Path(__file__).resolve().parents[1]
checks=[]
def chk(ok,label):
    if not ok: raise AssertionError(label)
    checks.append(label)
def load(path):
    return json.loads((ROOT / path).read_text("utf-8-sig"))

scope=load("canonical-artifacts/ND_CAPABILITY_REGISTRY_KSYUSHA_SCOPE_FROM_v1_66_1.json")
source=load("PLUGIN_EXPORT_CURRENT_MANIFEST.json")
plugin_entries=source["files"]
launchers=scope["runtime_invocation_bindings"]["launchers"]
chk(len(plugin_entries)==23,"23 total source plugin packages")
chk(len(launchers)==23,"23 exact source scoped launcher identities")
chk(len({l["launcher_uri"] for l in launchers})==23,"unique scoped URI")
chk(len({l["component_key"] for l in launchers})==23,"unique scoped semantic keys")
packages={}
for entry in plugin_entries:
    slug=entry["name"].removesuffix(".json")
    pkg=load("plugin-export-current/"+entry["name"])
    chk(pkg["name"]==slug,"source bundle ID "+slug)
    chk(pkg["version"]==entry["source_version"],"version "+slug)
    c=pkg["contents"]
    chk("plugin.json" in c,"plugin.json "+slug)
    manifest=json.loads(c["plugin.json"])
    chk(manifest.get("name")==slug,"plugin manifest name "+slug)
    display=(manifest.get("extensions",{}).get("com.openai",{}).get("interface",{}).get("displayName"))
    chk(isinstance(display,str) and display.startswith("ND "),"@ ND displayName "+slug)
    skill_paths=[p for p in c if p.startswith("skills/") and p.endswith("/SKILL.md")]
    chk(bool(skill_paths),"packaged skill "+slug)
    packages[slug]={"files":c,"skills":skill_paths,"display":display}

expected_slug_set={l["launcher_uri"].split("/")[3] for l in launchers}
chk(len(expected_slug_set)==22,"22 launcher-backed distinct plugin packages")
chk(set(packages)==expected_slug_set|{"nd-external-connecting"},"exact package coverage incl recovery")
roots=[l for l in launchers if l["role"]=="ROOT"]
chk(len(roots)==1 and roots[0]["component_key"]=="AUTOMATION_AGENT","single root")
by_uri={l["launcher_uri"]:l for l in launchers}
for l in launchers:
    uri=l["launcher_uri"]
    parts=uri.split("/")
    chk(len(parts)==5 and parts[0]=="skills:" and parts[2]=="plugins","launcher URI schema "+uri)
    slug,skill=parts[3],parts[4]
    c=packages[slug]["files"]
    p="skills/"+skill+"/SKILL.md"
    chk(p in c,"launcher skill packaged "+uri)
    body=c[p]
    chk(uri in body,"exact launcher identity in skill "+uri)
    if l.get("structural_parent_launcher_uri"):
        chk(l["structural_parent_launcher_uri"] in by_uri,"parent included "+uri)
        chk(l["structural_parent_launcher_uri"] in body or
            "STRUCTURAL_PARENT" in body or "Structural parent" in body,
            "parent protocol present "+uri)
    chk("ND-LAUNCHER-CONTRACT-v6" in body or
        l["component_key"]=="SONGWRITER",
        "v6 launcher contract "+uri)
chk(set(packages["nd-true-developer"]["skills"])=={
    "skills/nd-launch-true-developer/SKILL.md",
    "skills/nd-launch-developer-executor/SKILL.md"},
    "Developer Executor belongs inside True Developer plugin")
chk("nd-developer-executor" not in packages,"do not transfer standalone legacy Executor")
chk("skills/connecting-external-capabilities/SKILL.md"
    in packages["nd-external-connecting"]["skills"],"External Connecting recovery skill")
chk("SONGWRITER" in {l["component_key"] for l in launchers},"Songwriter child in scoped candidate")
song=next(l for l in launchers if l["component_key"]=="SONGWRITER")
chk(song["structural_parent_launcher_uri"]=="skills://plugins/nd-true-writer/nd-launch-true-writer",
    "Songwriter parent is Writer")
excluded={"TRUE_SOUND","STUDIO_EXECUTOR","SOUND_CRITIC"}
chk(excluded.isdisjoint({l["component_key"] for l in launchers}),"audio exclusion exact")
ck_doc=(ROOT/"ALL_PLUGIN_LAUNCHERS_GATE.md").read_text(encoding="utf-8")
chk("23 плагина" in ck_doc and "23 URI" in ck_doc,"complete target @ gate documented")
chk("PLUGIN_PROVIDER_READBACK" in ck_doc and "REAL_CHILD_CRITIC_RETURN" in ck_doc,
    "provenance levels not collapsed")
print(json.dumps({
    "verdict":"PASS","checks":len(checks),"failures":0,
    "source_launcher_uris":len(launchers),
    "unique_launcher_plugins":len(expected_slug_set),
    "separate_recovery_plugins":1,
    "unique_plugin_bundles":len(packages),
    "scope":"SOURCE_PACKAGE_ONLY__KSYUSHA_TARGET_PLUGIN_AND_CHATGPT_HOST_NOT_RUN"
},ensure_ascii=False))
