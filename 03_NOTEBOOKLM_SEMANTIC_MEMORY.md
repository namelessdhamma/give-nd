# Stage 03 — Connect NotebookLM + Build Semantic Memory

ROLE: TARGET BOOTSTRAP EXECUTOR WITH INSTALLED EXTERNAL CONNECTING  
TARGET STATE: NONAUTHORITATIVE

## Objective

Use the already-installed External Connecting capability to connect/qualify Gemini NotebookLM in Ksyusha's account, then build target-owned ND semantic workspaces.

## Preconditions

Stage 02 PASS. In particular:
- Generation is installed;
- External Connecting is installed and OPERATION_QUALIFIED;
- target StateHead is still BOOTSTRAP/NONAUTHORITATIVE.

Ksyusha having no NotebookLM connection before this stage is expected and is NOT a defect.

## Execution

1. Recover target state from `TARGET_INSTALL_STATE.json` and Stage 02 receipt.
2. Enter the target External Connecting skill directly for the explicit capability goal: connect and qualify Gemini NotebookLM for Ksyusha.
3. Follow `REUSE -> EXTEND -> CREATE`. If authorization is required, request only Ksyusha's NotebookLM authorization, preserve checkpoint, and continue after authorization.
4. Prove the NotebookLM route at least OPERATION_QUALIFIED:
   - list/read capability works;
   - create a bounded disposable notebook/source fixture if required;
   - verify provider readback;
   - remove the disposable fixture if created.
5. Create target-owned system semantic workspaces defined by `SEMANTIC_WORKSPACES_CURRENT.txt`:
   - Semantic Core;
   - True Memory;
   - True Research;
   - GPT Skills;
   - A1 Self-Evolution.
6. Do NOT reuse source NotebookLM IDs. Do NOT import excluded source ACTIVE_PROJECT notebooks.
7. Seed each target notebook from target-owned Drive canonical/system material, curated for its role. Source project/personal payload remains excluded.
8. Wait for all required sources to become READY. Thin/error/failed sources are not accepted as success.
9. Record target notebook/source IDs in the target binding working copy and target install state.
10. Verify NotebookLM remains NONAUTHORITATIVE: it is semantic working memory, never StateHead/currentness authority.

## Memory semantics to preserve

- CORE persists.
- ACTIVE_PROJECT persists while useful.
- Long/complex production tasks later use True Memory TASK_MEMORY_GATE and TEMP_TASK lifecycle.
- TEMP_TASK completion later requires True Memory -> Inquisitor cleanup.
- No competing persistent semantic root.

## Completion

Write `migration/receipts/STAGE_03_NOTEBOOKLM_RECEIPT.json` and update `TARGET_INSTALL_STATE.json`.

PASS requires a target-qualified NotebookLM route plus all five target system workspaces ready and rebound.

Then stop this stage and instruct Ksyusha to run `04_RESEARCH_STACK.md`.
