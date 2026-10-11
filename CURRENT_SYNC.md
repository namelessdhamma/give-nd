# ND → Ksyusha — CURRENT_SYNC 2026-10-11

SYNC_ID: `ND-KSYUSHA-SYNC-20261011-1`  
MODE: **IN-PLACE / RESUMABLE / NO REINSTALL**

## Authority and transfer profile
Fresh source authority: `NAM-143 -> bound CURRENT Registry`. Source CURRENT is Registry 1.66.0. Its only structural additions over exact predecessor Registry 1.65.2 are TRUE_SOUND + STUDIO_EXECUTOR + SOUND_CRITIC; all 32 predecessor components / 23 launcher bindings are exact-reused.

The user deferred Music Studio. This sync therefore transfers the coherent **pre-audio Registry 1.65.2 profile**, not a broken partial audio contour.

## Delta from the previous public package
- Registry 1.64.2 → **1.65.2**.
- Automation Agent 1.3.2 → **1.3.5**; plugin 1.7.3 → **1.7.5**.
- Anti-Hang 1.6.0 → **1.7.0**; plugin 1.2.0 → **1.2.1**.
- True Writer 0.9.2 → **0.9.3**; plugin 1.2.3 → **1.2.4**.
- Writer Orchestra 1.0.5 → **1.0.6**.
- add Songwriter **0.2.3**, launcher `skills://plugins/nd-songwriter/nd-launch-songwriter`.
- topology becomes **32 components / 23 launchers**; 23 transferred plugins, of which 22 back launchers and External Connecting is the recovery-skill plugin.

Songwriter is lyrics/prosody only. Required route:
`Automation Agent -> True Writer -> Songwriter -> True Writer -> Literary Critic -> True Writer -> Agent`.
It never performs audio generation.

## Mandatory sync preflight
Before any numbered stage:
1. recover target provider truth and `TARGET_INSTALL_STATE.json`;
2. if this sync receipt already exists/readbacks, do not replay it;
3. otherwise update only already-created objects affected by this delta;
4. write/read back `migration/receipts/CURRENT_SYNC_20261011.json`;
5. resume the actual target stage. Never reset to Stage 01 merely because package source changed.

### By target progress
- Before Stage 02: use the new bundles when Stage 02 is reached.
- Stage 02+: guarded-update/rebuild target Agent and Anti-Hang, preserve target-owned identity where possible, read back releases/canonical copies.
- Stage 05+: update True Writer and Writer Orchestra; add target Songwriter; preserve unaffected Writer/Visual Children.
- Stage 06 candidate exists: supersede the old 1.64.2/31/22 candidate and build/patch target Registry from 1.65.2 semantics with existing target provider IDs. Re-run changed gates and global consistency only.
- Stage 07/08 already published: treat this as an ordinary successor update, not reinstall. Prepare/prequalify successor objects while old target StateHead remains authority, then publish the successor StateHead binding LAST and cold-qualify the changed surfaces.

## NotebookLM / cost
NotebookLM is **not an installation gate** for Ksyusha now. Record `DEFERRED_OPTIONAL_CAPABILITY_PENDING_SEPARATE_INSTALLATION` and `NONAUTHORITATIVE / NONSELECTABLE`. Do not fabricate LM PASS.

Default route policy is **FREE_ONLY**. Do not use TinyFish, paid overage, paid credits, or unknown-cost routes without separate explicit authorization.

## ANTI_HANG_INSTALLATION_GATE
One logical mandatory gate executes twice: PREPUBLICATION in Stage 06 and independently COLD in Stage 08.
States: `PASS | FAIL | BLOCKED | NOT_RUN`.

Actual target execution must prove:
1. target StateHead/Registry resolves target Agent + Anti-Hang;
2. launcher and executable kernel are bound;
3. all seven hooks plus unique action IDs;
4. one request executes >=3 useful sequential safe subcycles with zero Go;
5. Child RETURN/local phase/checkpoint does not close the whole task;
6. pending external effect blocks only dependent work; independent safe work continues;
7. owner-verified usable result may integrate before optional cleanup;
8. OUTCOME_UNKNOWN reconciles before replay;
9. USER_STOP opens no new work, preserves unknown outcome, and never invents remote cancellation;
10. pressure narrows/compacts the next tranche and continues;
11. GLOBAL_WAIT_EXTERNAL only after a complete current runnable/reconcile/recovery/wake scan;
12. normal final return only after semantic done_when + required verification/persistence;
13. ordinary internal cycles do not force user-visible text;
14. no whole-task time/call/cycle/phase cap and no routine confirmation gate.

Historical source tests are reference evidence only; they never substitute target gate execution.

## Completion
CURRENT_SYNC completes after changed target objects and receipt are read back and the installer resumes from the previous target stage without reinstalling unaffected work.
