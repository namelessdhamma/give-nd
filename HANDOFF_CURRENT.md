# ND → Ksyusha — HANDOFF CURRENT

STATUS: SOURCE HANDOFF COMPLETE / STAGED TARGET INSTALLATION REQUIRED

## Current target installation path

Use `INSTALLATION_INDEX.md` as the human entrypoint.

Ksyusha installs ND in bounded stages, one MD file at a time:

1. `01_FOUNDATION_DRIVE_LINEAR.md`
2. `02_CORE_RUNTIME_EXTERNAL_CONNECTING.md`
3. `03_NOTEBOOKLM_SEMANTIC_MEMORY.md`
4. `04_RESEARCH_STACK.md`
5. `05_WRITING_VISUAL_STACK.md`
6. `06_REGISTRY_PREPUBLICATION.md`
7. `07_STATEHEAD_PUBLICATION.md`
8. NEW clean chat: `08_COLD_QUALIFICATION.md`

Each stage can run in a fresh chat and recovers from target Drive/Linear/provider readbacks rather than chat memory.

## Source baseline

- StateHead: NAM-143
- Registry: ND_CAPABILITY_REGISTRY 1.64.2
- Publication: ND-ANTI-HANG-TAIL-HARDENING-FINAL-20261004-1
- Transfer mode: isomorphic CURRENT ND clone with target-owned provider bindings.

## Package contents

The package contains:
- exact CURRENT Registry snapshot and canonical system artifacts;
- exact 22-launcher graph;
- exact functional source for 21 private plugins backing those 22 launchers;
- exact functional source for the separate CURRENT External Connecting recovery-skill plugin;
- target binding template;
- semantic-workspace map;
- allowed-differences and project/personal exclusions;
- full qualification matrix;
- staged installation instructions.

`PLUGIN_EXPORT_CURRENT_MANIFEST.json` is the plugin-source manifest.

## NotebookLM sequencing

Ksyusha does NOT need Gemini NotebookLM before installation begins.

Stage 02 first installs target-owned Generation + External Connecting.  
Stage 03 then uses External Connecting to connect/qualify Ksyusha's NotebookLM and creates target-owned semantic workspaces.

This avoids making NotebookLM a prerequisite for bootstrapping the capability that is responsible for connecting missing external systems.

## What is intentionally NOT transferred

No Savva credentials, OAuth grants, cookies, API keys, private personal memory, Gmail/calendar/contacts, active personal/product projects, or source provider ownership.

Generated binary caches such as `__pycache__/*.pyc` are intentionally excluded. They are not behavioral source.

## Authority rules

- Source CURRENT is selected only by `NAM-143 -> Registry 1.64.2`.
- Target CURRENT does not exist until Stage 07 publishes Ksyusha's target StateHead LAST.
- Before Stage 07, all target launchers are BOOTSTRAP/NONAUTHORITATIVE even if callable.
- Historical `TARGET_BOOTSTRAP.md`, validation-a1/a2/a3, predecessor registries and stale plugin bundles are NONSELECTABLE provenance.
- Source plugin IDs/releases are provenance only and must not become target ownership.
- Target Drive/Linear/NotebookLM/GitHub/Supabase/runtime IDs and credentials are target-owned.
- No production mutation to Savva's ND is part of this handoff.

## Remaining gate

The only intended remaining gate is target-account authorization/provisioning by Ksyusha while executing the staged files.
