# ND → Ksyusha — HANDOFF CURRENT

STATUS: SOURCE CURRENT SYNC READY / TARGET IN-PLACE UPDATE REQUIRED

Human entrypoint: `START_HERE.md`. Installer MUST run `CURRENT_SYNC.md` before choosing/resuming a numbered stage.

## Source transfer baseline
- source StateHead: NAM-143;
- fresh source CURRENT observed: Registry 1.66.0;
- transfer profile: exact predecessor Registry **1.65.2**, Drive `1brrS9gZkKoJc375FnicRpfACKfz97vIg`, SHA-256 `2697a11697680f18bab9cd3d72d07b63d6baf5aa6ee4f0f0f785661c4bd59576`;
- reason: 1.66.0 adds only TRUE_SOUND + STUDIO_EXECUTOR + SOUND_CRITIC. The user deferred Music Studio/audio, so the coupled audio contour is excluded rather than partially installed.

## Current transferred deltas
- Automation Agent 1.3.5 / plugin 1.7.5;
- Anti-Hang 1.7.0 / plugin 1.2.1;
- True Writer 0.9.3 / plugin 1.2.4;
- Writer Orchestra 1.0.6;
- Songwriter 0.2.3 as True Writer Child;
- 32 components / 23 launchers / separate External Connecting recovery skill;
- 23 transferred private plugin bundles.

## Target update rule
This is an **upgrade**, not a reinstall. Recover Ksyusha's `TARGET_INSTALL_STATE.json` and provider readbacks. Update only changed target objects, preserve already-qualified unaffected work, supersede an old 1.64.2 Registry candidate if present, and resume the real current stage.

NotebookLM is currently optional/deferred and NONSELECTABLE. Core Stage 06/07/08 may PASS without it. External routes default FREE_ONLY.

## Mandatory target gates
- Stage 06: `ANTI_HANG_INSTALLATION_GATE` PREPUBLICATION + Writer/Songwriter route.
- Stage 08: independent COLD Anti-Hang gate + Writer/Songwriter route in a new target chat.

Source tests do not establish target PASS.

## Authority
Source IDs/releases are provenance only. Target authority becomes/changes CURRENT only when the target Registry is fully prequalified and Ksyusha's target StateHead is published LAST.
