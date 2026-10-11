# Nameless Dhamma — Ксюша: обновление существующей установки

**Тип операции:** инкрементальное обновление уже существующей ND, НЕ повторная установка с нуля.

**Источник:** [give-nd](https://github.com/namelessdhamma/give-nd), CURRENT источник `NAM-143 → Registry 1.66.0`. Целевая власть всегда принадлежит **твоему**, а не Savva, StateHead/Registry.

## Одно сообщение от Ксюши

> @ND Automation Agent Обнови мою уже установленную Nameless Dhamma по https://github.com/namelessdhamma/give-nd/blob/main/START_HERE.md . Восстанови мой текущий StateHead, Registry и проверенные компоненты. Не устанавливай ND заново и не создавай дубликаты. Внеси лишь актуальные Anti-Hang 1.7.0 / Agent 1.3.5 и Songwriter 0.2.3 под True Writer, сохраняя всё рабочее. Пройди предусмотренные проверки, включая ANTI_HANG_INSTALLATION_GATE в Stage06 и новом чате Stage08. Не переноси музыкальную студию, мои или чужие секреты и личные данные. Продолжай внутренние циклы автономно без команды Go; запрашивай только реально необходимые Connect/Authorize.

## Обязательное поведение установщика

1. Сначала прочитай `INSTALLATION_INDEX.md`, `CURRENT_POINTER.txt`, `ANTI_HANG_INSTALLATION_GATE.md`, затем CURRENT источник. Пользуйся целевыми провайдерскими readbacks, а не памятью прежнего чата.
2. Выясни существующий target-owned Linear StateHead, CURRENT Registry, Plugin Creator releases, target Drive и последний `migration/TARGET_INSTALL_STATE.json`. Это режим **UPDATE_EXISTING_TARGET**, а не `NEW_BOOTSTRAP`; ранее проверенные объекты сохраняются.
3. Выполни стадии 01–07 **как внутренние идемпотентные проверки/дельта-операции**: `PASS_ALREADY_CURRENT` для уже совпадающих компонентов; `UPDATE_WITH_READBACK` только для отличающихся; `BLOCKED` при настоящем внешнем gate. Не считай `SKIP` без чтения доказательством PASS.
4. В обновлении допускаются только нынешние root Agent + Anti-Hang + Writer/Songwriter и действительно необходимые зависимые контракты. Сохраняются прочие target-owned структуры. Никакого нового музыкального Studio и True Sound/Studio Executor/Sound Critic.
5. Изолируй source и target: все source provider IDs/release IDs используются лишь для сравнения и provenance. Все целевые активные привязки должны принадлежать Ксюше. Не переносить Savva OAuth, токены, личную память, проекты и объекты.
6. Stage06 выполняет `ANTI_HANG_INSTALLATION_GATE.md` как самостоятельную матрицу доказательств. Все требуемые вердикты должны быть PASS до target StateHead publication. Недоступный тест — NOT_RUN/BLOCKED, **не** фиктивный PASS.
7. Stage07 публикует только одну связанную обновлённую target Registry через существующий target StateHead с guarded single-writer + provider readback; не создаёт конкурирующий корень. Stage08 — отдельный **чистый чат**.
8. Выполняй безопасные внутренние подциклы без рутинных сообщений или Go. Переход между файлами Stage01→Stage07 автоматический после PASS; фразы «run next stage» в файлах — только fallback для самостоятельного запуска.
9. Если прав доступа нет — сначала checkpoint/readback, затем одно точное действие Connect/Authorize для Ксюши. После авторизации продолжи из текущего доказанного состояния. Не утверждай успешность, пока фактический target readback не подтвердил.

## Только реальные паузы

**AUTHORIZATION_GATE:** Ксюша подтверждает запрошенный доступ к своему провайдеру.

**CONTEXT_HANDOFF:** продолжение из целевого `TARGET_INSTALL_STATE.json`, без пересоздания подтверждённых объектов. Текст нового запроса:

> Продолжи обновление моей существующей Nameless Dhamma по https://github.com/namelessdhamma/give-nd/blob/main/START_HERE.md и моему последнему проверенному TARGET_INSTALL_STATE.json. Не начинай установку заново.

**COLD_QUALIFICATION_BOUNDARY:** после Stage07 PASS в новом чате:

> @ND Automation Agent Проведи независимую cold qualification моего обновлённого ND по https://github.com/namelessdhamma/give-nd/blob/main/08_COLD_QUALIFICATION.md и ANTI_HANG_INSTALLATION_GATE.md. Источник CURRENT — исключительно мой target StateHead → Registry. Реально проверь Anti-Hang и True Writer → Songwriter → True Writer → Literary Critic → True Writer. Не выдавай NOT_RUN за PASS.

После подлинного Stage08 PASS: `@ND Automation Agent + обычная задача`.
