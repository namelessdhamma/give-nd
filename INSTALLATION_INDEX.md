# ND → Ksyusha — Staged Installation Index

STATUS: CURRENT TARGET INSTALLATION PATH  
SOURCE BASELINE: NAM-143 → ND_CAPABILITY_REGISTRY 1.64.2  
PUBLICATION: ND-ANTI-HANG-TAIL-HARDENING-FINAL-20261004-1

## Why the installation is staged

Ksyusha's ND is intentionally installed in bounded stages rather than one monolithic run. Each stage is independently resumable, ends with provider readback, and leaves a durable checkpoint for the next chat.

Ksyusha does NOT need Gemini NotebookLM before installation begins. NotebookLM is connected in Stage 03, after CURRENT Generation + External Connecting have already been installed in the target account.

Before final StateHead publication, the target instance is BOOTSTRAP / NONAUTHORITATIVE. Do not treat partially installed @ND launchers as target CURRENT.

## How Ksyusha uses these files

Initial connections required: **Google Drive + Linear + Plugin Creator**. GitHub account connection is not required to read this public installer. Gemini NotebookLM is intentionally connected later in Stage 03.

Execute exactly one file at a time, in order:

1. `01_FOUNDATION_DRIVE_LINEAR.md`
2. `02_CORE_RUNTIME_EXTERNAL_CONNECTING.md`
3. `03_NOTEBOOKLM_SEMANTIC_MEMORY.md`
4. `04_RESEARCH_STACK.md`
5. `05_WRITING_VISUAL_STACK.md`
6. `06_REGISTRY_PREPUBLICATION.md`
7. `07_STATEHEAD_PUBLICATION.md`
8. In a NEW clean chat: `08_COLD_QUALIFICATION.md`

A stage may be run in a fresh chat. Give that chat the public repository URL plus the exact stage filename. The executor must recover state from target provider readbacks and the durable install checkpoint, not from previous chat memory.

If a required service asks Ksyusha to authorize/connect it, request only that authorization. After authorization she can say: `Continue this stage from the last verified checkpoint.`

Do not proceed to the next stage until the current stage reaches PASS or reports one exact irreducible authorization/provider gate.

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
