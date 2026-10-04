# Nameless Dhamma — Ksyusha Installer

This repository is a **public, self-contained installer snapshot** for creating an independent Ksyusha-owned Nameless Dhamma instance.

Source baseline:

- StateHead: `NAM-143`
- Capability Registry: `ND_CAPABILITY_REGISTRY 1.64.2`
- Publication: `ND-ANTI-HANG-TAIL-HARDENING-FINAL-20261004-1`

The source ND remains separate and is not modified by this installer.

## Simplest installation

Before starting, Ksyusha connects these apps to her ChatGPT:

- **Google Drive**
- **Linear**
- **Plugin Creator**

That is enough to begin.

**GitHub account connection is not required** to read this installer because the repository is public.

**Gemini NotebookLM is not required yet.** It is connected later, during Stage 03, after External Connecting is installed.

### First message in Ksyusha's ChatGPT

Give ChatGPT this repository URL and say:

> Read `INSTALLATION_INDEX.md` from this repository and execute `01_FOUNDATION_DRIVE_LINEAR.md` autonomously. Treat the repository files as the installation source. Do not redesign ND.

After a stage reaches PASS, run the next numbered MD file. A new chat may be used for every stage.

## Installation stages

1. `01_FOUNDATION_DRIVE_LINEAR.md`
2. `02_CORE_RUNTIME_EXTERNAL_CONNECTING.md`
3. `03_NOTEBOOKLM_SEMANTIC_MEMORY.md`
4. `04_RESEARCH_STACK.md`
5. `05_WRITING_VISUAL_STACK.md`
6. `06_REGISTRY_PREPUBLICATION.md`
7. `07_STATEHEAD_PUBLICATION.md`
8. **New clean chat:** `08_COLD_QUALIFICATION.md`

The target StateHead stays **BOOTSTRAP / NONAUTHORITATIVE** until Stage 07. It becomes target CURRENT only after the target Registry and all provider bindings have passed prepublication qualification.

## What is included

This public repository contains only the minimum CURRENT installation set:

- staged installation instructions;
- exact CURRENT Capability Registry snapshot;
- exact CURRENT canonical component/system artifacts needed for the clone;
- 22 target-transfer plugin source bundles:
  - 21 private plugins backing the 22-launcher graph;
  - 1 separate External Connecting recovery-skill plugin;
- target binding template;
- target plugin builder;
- qualification matrix;
- project/personal exclusion rules.

## What is not included

This repository intentionally excludes:

- Savva credentials, OAuth grants, cookies, API keys or provider secrets;
- personal memory, Gmail, Calendar or Contacts;
- active personal/product project payload;
- predecessor registries and obsolete installation paths;
- historical validation/provenance that is not required for installation;
- source account ownership as target authority.

## Authority rule

The public repository is a **frozen installation source**, not Ksyusha's future authority.

During installation:

`public source -> target-owned Drive / Linear / NotebookLM / Plugin Creator -> target Registry -> target StateHead LAST`

After Stage 07, Ksyusha's target CURRENT resolves only through:

`Ksyusha target Linear StateHead -> bound target Capability Registry -> exact target components/launchers`

Then Stage 08 performs fresh-chat cold qualification.

## Normal use after PASS

`@ND Automation Agent + ordinary goal`
