# Nameless Dhamma — установка для Ксюши

## Что делать Ксюше

Никакие stage-файлы вручную запускать по очереди не нужно.

Открой новый обычный чат ChatGPT и отправь **одно сообщение**:

> Установи мне Nameless Dhamma из https://github.com/namelessdhamma/give-nd . Открой `START_HERE.md` и выполни установку автономно до конца. Не проси меня вручную запускать stage-файлы и не задавай рутинных вопросов. Останавливайся только если мне действительно нужно подключить приложение/дать доступ или когда потребуется новый чистый чат для финальной проверки.

После этого делай только то, что ChatGPT действительно попросит сделать самой: обычно это нажатие **Connect / Allow / Authorize** для нужного приложения.

GitHub подключать к аккаунту не нужно: репозиторий публичный.

Gemini NotebookLM заранее подключать не нужно: он подключается позже, после установки ND External Connecting.

## Правила для установщика

This file is the human-facing orchestration layer. It simplifies installation choreography only. It does **not** change ND architecture, authority, topology, contracts, skills, qualification requirements, or target-isolation rules.

1. Read `INSTALLATION_INDEX.md`.
2. Recover existing target state first. If `migration/TARGET_INSTALL_STATE.json` exists, resume from its last verified provider readback. Never recreate already-qualified target objects blindly.
3. Execute Stages 01 → 07 in order. Each numbered stage remains a bounded transaction with its own receipt and provider readback.
4. When this `START_HERE.md` orchestration is active, any stage-level wording that says “stop this stage and instruct Ksyusha to run the next file” is a **standalone fallback only**. After a stage reaches PASS, automatically open/read the next numbered stage and continue in the same chat.
5. Do not ask Ksyusha to paste stage filenames, say `Go`, or confirm routine operations.
6. Visible execution may stop only for:
   - **AUTHORIZATION_GATE** — Ksyusha must connect/authorize a target-owned service;
   - **CONTEXT_HANDOFF** — the current chat cannot safely continue;
   - **COLD_QUALIFICATION_BOUNDARY** — Stage 07 PASS; Stage 08 must run in a new clean chat.

### Authorization gate

If Google Drive, Linear, Plugin Creator, Gemini NotebookLM, or another actually required target capability is not connected:

- checkpoint and read back current install state first;
- ask Ksyusha for **one exact action only**;
- do not redesign ND or substitute another architecture;
- after authorization, resume from provider truth and the durable checkpoint.

Ksyusha may reply simply:

> Продолжай.

### Context handoff

If the current chat cannot safely finish the remaining installation, first persist/read back the durable checkpoint and give Ksyusha exactly this continuation message for a new chat:

> Продолжи установку Nameless Dhamma из https://github.com/namelessdhamma/give-nd по `START_HERE.md` с последнего проверенного `TARGET_INSTALL_STATE.json`. Не начинай заново и не переделывай уже подтверждённые этапы.

Recover from Ksyusha-owned Drive/Linear/provider readbacks, not old chat memory.

### Final clean-chat boundary

After Stage 07 PASS, do **not** run Stage 08 in the migration chat.

Tell Ksyusha to open a new clean chat and send exactly:

> @ND Automation Agent Выполни финальную cold qualification моей установленной Nameless Dhamma по https://github.com/namelessdhamma/give-nd/blob/main/08_COLD_QUALIFICATION.md . Восстанови CURRENT только через мой target Linear StateHead → мой target Registry. Не используй Savva/source authority как target CURRENT. Исправь безопасные migration defects автономно и заверши до PASS либо одного точного внешнего blocker.

After Stage 08 PASS, normal use is:

`@ND Automation Agent + обычная задача`

## Human effort target

**одно стартовое сообщение → только реальные Connect/Authorize действия при необходимости → одно финальное сообщение в чистом чате.**

Все numbered stage files — внутренние шаги установщика, а не ручной чек-лист для Ксюши.
