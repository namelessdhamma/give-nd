# ND → Ksyusha — Staged Installation Index

STATUS: CURRENT TARGET INSTALLATION PATH  
SOURCE BASELINE: NAM-143 → ND_CAPABILITY_REGISTRY 1.64.2  
PUBLICATION: ND-ANTI-HANG-TAIL-HARDENING-FINAL-20261004-1

## Why the installation is staged

Ksyusha's ND is intentionally installed in bounded stages rather than one monolithic run. Each stage is independently resumable, ends with provider readback, and leaves a durable checkpoint for the next chat.

Ksyusha does NOT need Gemini NotebookLM before installation begins. NotebookLM is connected in Stage 03, after CURRENT Generation + External Connecting have already been installed in the target account.

Before final StateHead publication, the target instance is BOOTSTRAP / NONAUTHORITATIVE. Do not treat partially installed @ND launchers as target CURRENT.

## How Ksyusha uses these files

Human entrypoint: **`START_HERE.md`**.

Ksyusha normally sends one installation request and does **not** manually invoke numbered stage files. The installer executes these bounded stages internally and automatically continues after each PASS:

1. `01_FOUNDATION_DRIVE_LINEAR.md`
2. `02_CORE_RUNTIME_EXTERNAL_CONNECTING.md`
3. `03_NOTEBOOKLM_SEMANTIC_MEMORY.md`
4. `04_RESEARCH_STACK.md`
5. `05_WRITING_VISUAL_STACK.md`
6. `06_REGISTRY_PREPUBLICATION.md`
7. `07_STATEHEAD_PUBLICATION.md`
8. In a NEW clean chat: `08_COLD_QUALIFICATION.md`

Google Drive, Linear and Plugin Creator may already be connected, but this is not required choreography: if a required target-owned service is absent, the installer checkpoints first and requests only the exact authorization action. GitHub account connection is not required to read this public installer. Gemini NotebookLM is intentionally connected later in Stage 03.

If a fresh chat is required before Stage 07, the executor recovers from target provider readbacks and `TARGET_INSTALL_STATE.json`, not previous chat memory.

When `START_HERE.md` orchestration is active, stage-level “stop and run the next file” wording is standalone fallback only; PASS automatically advances to the next stage.

## Durable checkpoint contract

Stage 01 creates a target Drive system root and:

- `migration/TARGET_INSTALL_STATE.json`
- `migration/receipts/`

Every stage before StateHead publication updates `TARGET_INSTALL_STATE.json` and writes a stage receipt. Re-running a stage must first inspect its existing receipt and provider truth; never blindly duplicate already verified objects.

The target Linear StateHead issue may be created in Stage 01, but it remains explicitly `BOOTSTRAP / NONAUTHORITATIVE` until Stage 07.

## Source package rules

Use:
- `HANDOFF_CURRENT.md`
- `BOOTSTRAP_CURRENT.txt`
- `TRANSFER_MANIFEST.json`
- `SELECTABLE_SET_CURRENT.json`
- `ALLOWED_DIFFERENCES.json`
- `PROJECT_EXCLUSIONS_CURRENT.txt`
- `BINDING_MAP_TEMPLATE.json`
- `LAUNCHER_GRAPH_CURRENT.txt`
- `PLUGIN_EXPORT_CURRENT_MANIFEST.json`
- `plugin-export-current/*.json`
- `SEMANTIC_WORKSPACES_CURRENT.txt`
- `QUALIFICATION.md`

Do not select historical `TARGET_BOOTSTRAP.md`, validation-a1/a2/a3, predecessor registries, stale plugin bundles, or source-account provider ownership.

Savva's credentials, personal memory, mail/calendar/contact data and excluded project payload never transfer.

## Global invariant

Target authority becomes real only after:

target-owned provider objects → exact readbacks → target Registry → prepublication qualification PASS → target Linear StateHead published LAST → cold recovery in a fresh chat.
