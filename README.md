# Nameless Dhamma — Ksyusha Installer

This repository is a **public, self-contained installer snapshot** for creating an independent Ksyusha-owned Nameless Dhamma instance.

Source baseline:

- StateHead: `NAM-143`
- Capability Registry: `ND_CAPABILITY_REGISTRY 1.64.2`
- Publication: `ND-ANTI-HANG-TAIL-HARDENING-FINAL-20261004-1`

The source ND remains separate and is not modified by this installer.

## Самая простая установка

Ксюше не нужно вручную проходить восемь файлов.

Открыть обычный новый чат ChatGPT и отправить одно сообщение:

> Установи мне Nameless Dhamma из https://github.com/namelessdhamma/give-nd . Открой `START_HERE.md` и выполни установку автономно до конца. Не проси меня вручную запускать stage-файлы и не задавай рутинных вопросов. Останавливайся только если мне действительно нужно подключить приложение/дать доступ или когда потребуется новый чистый чат для финальной проверки.

Дальше ChatGPT сам выполняет Stages 01–07. Если ему действительно нужен доступ к сервису, Ксюша нажимает Connect / Allow / Authorize и отвечает `Продолжай.`

После Stage 07 ChatGPT сам даст одну готовую строку для нового чистого чата с финальной проверкой.

**GitHub account connection is not required.** The repository is public.

**Gemini NotebookLM is not required before starting.** It is connected later through the installed External Connecting capability.

Human entrypoint: **`START_HERE.md`**.

## Installation stages

The numbered files remain bounded/resumable implementation transactions and are normally executed automatically by the installer:

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

- one-message human orchestration in `START_HERE.md`;
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
