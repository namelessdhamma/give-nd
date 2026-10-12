#!/usr/bin/env python3
"""Stage U READ-ONLY inventory diff. NEVER connects to or mutates a provider.

Inputs must be copied from ACTUAL Ksyusha target provider readbacks. A local plan
is not a publication gate, installation receipt, or successful qualification.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCOPE = ROOT / "canonical-artifacts/ND_CAPABILITY_REGISTRY_KSYUSHA_SCOPE_FROM_v1_66_1.json"
EXCLUDED = {"TRUE_SOUND", "STUDIO_EXECUTOR", "SOUND_CRITIC"}

def keyed(items, name):
    values = {}
    for item in items:
        key = item.get("component_key")
        if not isinstance(key, str) or not key or key in values:
            raise ValueError(f"{name}: invalid/duplicate component_key: {key}")
        values[key] = item
    return values

def analyze(target, source, statehead):
    if not isinstance(target, dict) or not isinstance(source, dict) or not isinstance(statehead, dict):
        raise ValueError("Expected JSON objects")
    target_components = keyed(target.get("components", []), "target components")
    source_components = keyed(source.get("components", []), "source components")
    target_launchers = keyed(target.get("runtime_invocation_bindings", {}).get("launchers", []), "target launchers")
    source_launchers = keyed(source.get("runtime_invocation_bindings", {}).get("launchers", []), "source launchers")
    if len(source_components) != 32 or len(source_launchers) != 23:
        raise ValueError("Source 32/23 scoped projection was not verified")
    if EXCLUDED & (source_components.keys() | source_launchers.keys()):
        raise ValueError("Audio roles cannot be installed via Stage U")
    if statehead.get("identifier") != "XEN-5":
        raise ValueError("StateHead must be independently verified as existing target XEN-5")
    bound = statehead.get("registry_id")
    actual = statehead.get("registry_id_readback")
    if not bound or bound != actual:
        raise ValueError("Target StateHead Registry binding has not been reconciled by provider readback")
    current_sha = statehead.get("registry_sha256")
    if not isinstance(current_sha, str) or len(current_sha) != 64:
        raise ValueError("Read back exact 64-character target Registry checksum; do not use report assertion alone")
    if target.get("version") != statehead.get("registry_version"):
        raise ValueError("Target Registry version and StateHead binding disagree")
    if EXCLUDED & (target_components.keys() | target_launchers.keys()):
        raise ValueError("Existing target includes excluded audio: manual scoped reconciliation required")
    added_components = sorted(set(source_components) - set(target_components))
    added_launchers = sorted(set(source_launchers) - set(target_launchers))
    target_only = sorted(set(target_components) - set(source_components))
    changed = sorted(
        key for key in (set(target_components) & set(source_components))
        if target_components[key].get("canonical_hash") != source_components[key].get("canonical_hash")
    )
    wrong_parents = sorted(
        k for k in (set(target_launchers) & set(source_launchers))
        if target_launchers[k].get("structural_parent_launcher_uri") != source_launchers[k].get("structural_parent_launcher_uri")
    )
    if not statehead.get("anchor"):
        raise ValueError("Missing exact old XEN-5 anchor: guarded publication is unavailable")
    return {
        "status": "READ_ONLY_PLAN_NOT_AN_INSTALLATION_OR_QUALIFICATION",
        "target_statehead": "XEN-5", "target_registry_version": target["version"],
        "target_registry_id": bound, "target_registry_sha256": current_sha,
        "old_anchor_present": True,
        "source_projection_version": source["version"],
        "target_counts": {"components": len(target_components), "launchers": len(target_launchers)},
        "source_scoped_counts": {"components": 32, "launchers": 23},
        "missing_component_keys": added_components,
        "missing_launcher_keys": added_launchers,
        "target_only_keys_requiring_reconciliation": target_only,
        "same_key_changed_canonical_hash_keys": changed,
        "parent_mismatch_keys": wrong_parents,
        "known_user_report_31_22_match": len(target_components) == 31 and len(target_launchers) == 22,
        "songwriter_missing": "SONGWRITER" in added_components and "SONGWRITER" in added_launchers,
        "mandatory_packages": {
            "nd-automation-agent": "1.7.8; MUST provider-readback target package",
            "nd-anti-hang": "1.2.1; MUST provider-readback target package",
            "nd-true-writer": "1.2.4; preserve CURRENT Writer child ownership",
            "nd-songwriter": "0.2.3; required if missing under target True Writer",
        },
        "gates": {
            "stage_u_prepublication": "NOT_RUN",
            "anti_hang_stage06": "NOT_RUN",
            "human_output_stage06": "NOT_RUN",
            "songwriter_physical_chain": "NOT_RUN",
            "target_statehead_publication": "NOT_RUN",
            "stage_u_cold": "NOT_RUN",
            "full_stage08": "NOT_RUN",
        },
        "authority_warning": "Never publish from this plan; obtain target-owned provider readbacks and Stage U receipt PASS first",
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--target-registry", required=True, type=Path)
    p.add_argument("--statehead", required=True, type=Path)
    p.add_argument("--source-registry", type=Path, default=SCOPE)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    source = json.loads(args.source_registry.read_text(encoding="utf-8-sig"))
    target = json.loads(args.target_registry.read_text(encoding="utf-8-sig"))
    statehead = json.loads(args.statehead.read_text(encoding="utf-8-sig"))
    report = analyze(target, source, statehead)
    serialized = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    else:
        print(serialized, end="")

if __name__ == "__main__":
    main()
