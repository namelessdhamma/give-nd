# Stage 06 — Target Registry + Prepublication Qualification

ROLE: TARGET BOOTSTRAP EXECUTOR  
TARGET STATE: NONAUTHORITATIVE / READY-FOR-PUBLICATION CANDIDATE

## Objective

Converge all target-owned IDs into one target Capability Registry and prove the clone is ready before authority publication.

## Execution

1. Recover all Stage 01-05 receipts and direct provider truth.
2. Complete the target `BINDING_MAP_TEMPLATE.json` using ONLY target provider readbacks:
   - Drive;
   - Linear;
   - NotebookLM;
   - target Plugin Creator releases;
   - GitHub/runtime coordinates where applicable;
   - external routes;
   - scheduler/provider IDs.
   Any provider binding that CURRENT does not actually require for Ksyusha must be replaced with an explicit non-placeholder state such as `NOT_REQUIRED_BY_TARGET_CURRENT`; do not carry unresolved `${...}` placeholders into the Registry. Never place credentials in the binding map.
3. Materialize the complete in-scope target-owned canonical system/component artifact set in Ksyusha's Drive from the frozen transfer sources. Apply only verified allowed target-provider substitutions where an artifact contains source-bound provider coordinates. Preserve exact semantic/body content otherwise. Provider-read back every target canonical artifact and record its target Drive ID/hash in `canonical_artifact_rebind`.
4. Reconcile the system NotebookLM workspaces so their authoritative source links/content point to Ksyusha's target-owned canonical Drive artifacts rather than frozen source-baseline/provenance copies. Wait for READY/readback.
5. Build the target Capability Registry by cloning source Registry 1.64.2 semantics and replacing only fields permitted by `ALLOWED_DIFFERENCES.json`, including target canonical artifact IDs/hashes and target plugin/provider bindings.
6. Include:
   - 31 CURRENT components accounted for;
   - 22 CURRENT launchers;
   - separate CURRENT External Connecting recovery skill;
   - target semantic workspace IDs;
   - target provider routes;
   - A1 sole self-evolution semantics.
7. If the A1 scheduler object is part of the target clone, provision it now in a DISABLED/DORMANT state and bind its target-owned ID. Do not let it run before cold qualification.
8. Persist the target Registry in Ksyusha's Drive and read back exact content/hash.
9. Verify target Linear navigation parity against `LINEAR_CURRENT_MAP.txt`: every required stable target navigator exists with target-owned IDs and preserved status/role semantics; source IDs remain provenance only.
10. Run all prepublication portions of `QUALIFICATION.md`, including:
   - authority structure except final CURRENT publication;
   - 22/22 launcher visibility/callability;
   - External Connecting recovery-skill visibility;
   - Supervisor/Child/Critic topology;
   - Anti-Hang seven-hook semantics;
   - True Memory + target NotebookLM lifecycle capability;
   - FAILED_ROUTE != FAILED_CAPABILITY;
   - isolation and exclusions;
   - A1 sole self-evolution contour.
11. Repair any target migration defect and repeat the affected qualification. Do not redesign architecture.
12. Verify the target bootstrap StateHead still says BOOTSTRAP/NONAUTHORITATIVE and points to no competing CURRENT Registry.
13. Update `TARGET_INSTALL_STATE.json` to `PREPUBLICATION_PASS` only after all checks are satisfied.

## Completion

Write `migration/receipts/STAGE_06_PREPUBLICATION_RECEIPT.json`.

PASS requires a verified target Registry + complete prepublication qualification with zero unresolved material findings.

Then stop this stage and instruct Ksyusha to run `07_STATEHEAD_PUBLICATION.md`.
