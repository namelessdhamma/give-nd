# Stage 01 — Target Foundation: Drive + Linear

ROLE: TARGET BOOTSTRAP EXECUTOR  
TARGET STATE: NONAUTHORITATIVE  
NOTEBOOKLM: NOT REQUIRED

## Objective

Create the target-owned durable installation foundation for Ksyusha without installing the cognitive runtime yet.

## Preconditions

- The public transfer repository is readable from its GitHub URL; Ksyusha does NOT need to connect her GitHub account just to install ND.
- Ksyusha can authorize her own Google Drive and Linear.
- Plugin Creator should be connected by Stage 02.
- A target GitHub account/repository is optional unless a later CURRENT capability actually requires it.
- Do not require Gemini NotebookLM in this stage.

## Execution

1. Read `INSTALLATION_INDEX.md`, `HANDOFF_CURRENT.md`, `TRANSFER_MANIFEST.json`, `SELECTABLE_SET_CURRENT.json`, `ALLOWED_DIFFERENCES.json`, and `PROJECT_EXCLUSIONS_CURRENT.txt`.
2. Inventory target access to:
   - Google Drive;
   - Linear;
   - Plugin Creator.
   Treat GitHub as optional during bootstrap because this installation source is public. Record only capability/authorization state. Never copy source credentials.
3. Create a Ksyusha-owned Drive root named clearly as the ND system root. Under it create durable areas for:
   - target canonical system artifacts;
   - target control/currentness artifacts;
   - plugin source/export provenance;
   - migration state and receipts;
   - a clearly NONAUTHORITATIVE frozen source-baseline area.
4. Store the transfer control artifacts and exact source Registry snapshot under the frozen source-baseline/provenance area. They are installation inputs, not target CURRENT. Do not place the source Registry snapshot in a location or status that can be mistaken for Ksyusha's target Registry. Target canonical/control surfaces are populated progressively and the target Registry itself is not created until Stage 06.
5. Create `migration/TARGET_INSTALL_STATE.json` with:
   - source baseline = Registry 1.64.2;
   - current stage = 01;
   - target Drive root ID;
   - authorization inventory;
   - target StateHead = not yet authoritative;
   - next stage = 02.
6. Create the target Linear issue that will eventually become Ksyusha's StateHead. It MUST be clearly marked:
   - `BOOTSTRAP / NONAUTHORITATIVE`;
   - source baseline reference only;
   - no CURRENT claim;
   - no source NAM-143 ownership.
   Preserve the semantic role/title of the source StateHead, but use a target-owned Linear identifier.
7. Create only the minimum bootstrap Linear navigation required to resume installation. Do not mass-create speculative child issues. Exact target navigators are created when their corresponding components are installed.
8. Read back every created Drive and Linear object. Reconcile any ambiguous write before retry.

## Forbidden

- No NotebookLM creation.
- No target Registry publication.
- No StateHead CURRENT/AUTHORITATIVE status.
- No source provider ID treated as target ownership.
- No personal/project payload transfer.

## Completion

Write `migration/receipts/STAGE_01_FOUNDATION_RECEIPT.json` and update `TARGET_INSTALL_STATE.json`.

PASS requires verified target Drive root + verified BOOTSTRAP/NONAUTHORITATIVE Linear StateHead + no unauthorized source-account dependency.

Then stop this stage and instruct Ksyusha to run `02_CORE_RUNTIME_EXTERNAL_CONNECTING.md`.
