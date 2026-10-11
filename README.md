# Nameless Dhamma — Ksyusha Installer / Updater

Public source for creating **or updating in place** an independent Ksyusha-owned Nameless Dhamma.

CURRENT sync epoch: `ND-KSYUSHA-SYNC-20261011-1`.

## Самый простой запуск

Отправить в обычный ChatGPT-чат одно сообщение:

> Установи или обнови мою Nameless Dhamma из https://github.com/namelessdhamma/give-nd . Открой START_HERE.md, сначала выполни CURRENT_SYNC.md, восстанови существующий TARGET_INSTALL_STATE.json и продолжи автономно с последнего подтверждённого состояния. Ничего уже установленного не переустанавливай с нуля. NotebookLM пока не подключай. Работай FREE_ONLY, без TinyFish и других платных маршрутов. Не проси Go и не задавай рутинных вопросов. Остановись только на реальном Connect/Authorize, непреодолимом provider gate или обязательной границе нового чистого чата Stage 08.

Human entrypoint: `START_HERE.md`.

## Transfer baseline

This sync transfers the exact source **Registry 1.65.2 pre-audio profile**:
- 32 components;
- 23 launchers;
- 23 private plugin bundles;
- Automation Agent 1.3.5 / plugin 1.7.5;
- Anti-Hang 1.7.0 / plugin 1.2.1;
- True Writer 0.9.3 / Writer Orchestra 1.0.6;
- Songwriter 0.2.3.

Fresh source CURRENT is later Registry 1.66.0, but its only structural additions are TRUE_SOUND + STUDIO_EXECUTOR + SOUND_CRITIC. That coupled audio/Music Studio contour is intentionally deferred from this sync.

## Existing installs

Installer runs `CURRENT_SYNC.md` first, recovers target provider truth, applies only changed deltas, and resumes the actual stage. It must not restart Stages 01–05 or recreate already-qualified objects merely because the public package was updated.

## NotebookLM / cost

NotebookLM is currently `DEFERRED_OPTIONAL_CAPABILITY_PENDING_SEPARATE_INSTALLATION`. Its absence is not a Stage 06/07/08 blocker.

Default external-route policy: `FREE_ONLY`. No TinyFish, paid overage, paid credits or unknown-cost routes without separate explicit authorization.

## Qualification

Anti-Hang is behaviorally qualified on the target twice:
1. Stage 06 PREPUBLICATION;
2. Stage 08 COLD in a new chat.

Song-writing qualification uses:
`Automation Agent -> True Writer -> Songwriter -> True Writer -> Literary Critic -> True Writer -> Agent`.

Source package publication never equals target installation PASS.

Normal use after target Stage 08 PASS: `@ND Automation Agent + ordinary goal`.
