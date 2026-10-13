# ND Ксюши — полный Plugin-Launcher Inventory Gate

**Задача:** проверить и при необходимости восстановить **все** пользовательские `@ND` плагины-лаунчеры, а не только четыре пакета Stage U.

## Фактическая модель ND

- Каждый `SKILL.md` — навык **внутри плагина ChatGPT**; `@Plugin Creator` создаёт/обновляет приватные плагины. `plugin.json` содержит `extensions.com.openai.interface.displayName` для пользовательского имени `@ND …`.
- Точка пользовательского входа — выбор установленного `@ND Automation Agent` в ChatGPT. `@ND True Research`, `@ND True Writer` и остальные Supervisors могут быть выбраны для адресной диагностики. **Children не требуют ручного упоминания пользователем при обычной задаче**: их владелец-Supervisor выбирает маршрут; прямой запрос к Child должен возвращаться через владельца.
- `skills://plugins/<plugin>/<skill>` — идентичность навыка в Registry и каталоге Skills; это не URL исполняемого сервера. Одного описания передачи управления недостаточно, чтобы объявить физическое исполнение другого ChatGPT-плагина.
- `Automation Agent → True Memory task gate → соответствующий Supervisor → его Child/helper → обязательный Critic/acceptance → Supervisor → ROOT → следующий полезный подцикл`. Anti-Hang — семь cross-cutting hooks, не отдельный task owner; циклы `SILENT_CONTINUE`, без рутинного Go.
- **Критическая граница:** созданный/прочитанный через Plugin Creator архив != доступный в текущем чате выбранный `@plugin` != фактический вызов Child/Critic. Фиксируй каждый уровень отдельно.

## Что передано в исходном пакете

**23 URI / 22 launcher-backed plugin bundles**, плюс **1 отдельный плагин External Connecting** для восстановления подключений = **23 плагина**.

| Роль | Launcher URIs / source plugin packages |
| --- | --- |
| ROOT | Automation Agent — `nd-automation-agent` |
| Supervisors | True Memory — `nd-true-memory`; True Developer — `nd-true-developer`; True Doctor — `nd-true-doctor`; True Research — `nd-true-research`; True Writer — `nd-true-writer`; True Visual — `nd-true-visual`; True SMM — `nd-true-smm` (сохранять статус `NOT ADOPTED`, если целевой readback его подтверждает) |
| True Memory Child | Inquisitor — `nd-inquisitor` |
| True Developer Children | Developer Executor — **второй SKILL в `nd-true-developer`**, не обязательный отдельный плагин; Developer Critic — `nd-developer-critic` |
| True Research Children | PCPA — `nd-pcpa`; DAE — `nd-dae`; PAE — `nd-pae`; Research Critic — `nd-research-critic` |
| True Writer Children | Books Creator — `nd-books-creator`; Technical Writer — `nd-technical-writer`; Story Architect — `nd-story-architect`; Literary Critic — `nd-literary-critic`; Songwriter — `nd-songwriter` (до публикации XEN-5 `NONCURRENT CANDIDATE`) |
| True Visual Child | Visual Creator — `nd-visual-creator` |
| Cross-cutting | Anti-Hang — `nd-anti-hang` |
| Recovery support | Generation — `nd-generation` |
| Separate recovery plugin | External Connecting — `nd-external-connecting`, `skills://plugins/nd-external-connecting/connecting-external-capabilities` |

Источник точных URI и родительских связей — `canonical-artifacts/ND_CAPABILITY_REGISTRY_KSYUSHA_SCOPE_FROM_v1_66_1.json` и `LAUNCHER_GRAPH_CURRENT.txt`. Установщик НЕ добавляет три исключённых аудиальных роли (`TRUE_SOUND`, `STUDIO_EXECUTOR`, `SOUND_CRITIC`). Не переносит личные данные, ключи и проекты исходного пользователя.

## TARGET gate (Ксюшин аккаунт): проверь **каждый** пакет/навык

1. Прочитай XEN-5 и действующий target Registry; восстанови сохранённые target-owned Plugin Creator IDs, релизы и существующие Stage01–07 receipts. Пакеты считаются уже установленными **только при точном readback из целевого аккаунта**, а не по наличию исходного `plugin-export-current/*.json`.
2. Построй **полный target-owned инвентарь из 23 plugin packages**, в нём у каждого: source_slug, target_plugin_id, target_release_id, `plugin.json` displayName, набор файлов `SKILL.md`, версия, target navigator/parent, owner/role, `@mention selectable`, single skill load evidence, applicable typed Child/return evidence, result verdict. Для `nd-true-developer` проверь **два** skills в одном плагине. Extra `nd-external-connecting` не подменяет Registry-URI.
3. Для **каждого** установленного пакета проверь доступность как реально выбранного `@`-плагина в ChatGPT, а не текстовое совпадение или один раз найденный каталог. Для текущей Ksyusha сессии сначала устранить проблему отсутствующей видимости через настройки и инвентарь Plugins/skills, без фиктивного специального `skills://` executor. Реальный новый чат — отдельное действие только если среда это позволяет; не утверждать, что он был создан, по одному промпту.
4. Уже подтверждённые пакеты **не переустанавливать**. Пакет отсутствует или повреждён? Сначала целевой readback; восстановить только данный пакет через `@Plugin Creator`, `build_target_plugin.py` и verified target rebind. Старый редундантный `nd-developer-executor` не выбирать, если CURRENT указывает на дочерний skill внутри `nd-true-developer`.
5. **Proof levels в receipt:** `PLUGIN_PROVIDER_READBACK` → `SKILL_DISCOVERY` → `SELECTED_AT_MENTION` → `ACTUAL_PLUGIN_SKILL_LOAD` → `OBSERVED_HOST_TOOL_ACTION` → `REAL_CHILD_CRITIC_RETURN`. Не заменять последний уровень Python fixture, выдуманной трассой или собственным описанием GPT. Если host не предоставляет наблюдаемую межплагинную телеметрию, указать конкретно не подтверждённую границу.
6. Закрытие Stage U и Stage08 требует действительных U3 prepublication gates, guarded XEN-5, потом **отдельной** cold-квалификации целевого CURRENT. Songwriter до публикации — кандидат; физический CURRENT Songwriter тест после публикации. Нет исходных source/provider IDs в целевом CURRENT.
7. Записать `migration/receipts/ALL_PLUGIN_LAUNCHERS_TARGET_INVENTORY.json` и provider readback в Drive Ксюши. `PASS` только когда все обязательные установленные target Plugins и selected Skills доказаны отдельно по каждому; `BLOCKED` — с точным непроверенным полем и владельцем внешнего ограничения. Этот инвентарь не подменяет физическую Stage08.

## Реальный опыт, который нельзя игнорировать

- В исходном аккаунте текущий доступный каталог содержал все 23 из 23 scoped launcher URI, но это **не доказывает** то же самое в аккаунте Ксюши.
- В истории ND были cold-start сеансы со stale launcher binding, а также отдельные scheduled/host-поверхности с **пустым списком Skills**. Поэтому `plugin_created`, `skill_list_visible`, `@selection` и `actual_child_return` — независимые проверки.
- Ксюша сообщила про Plugin Creator readback четырёх обновлённых пакетов (Agent1.7.8, Anti-Hang1.2.1, Writer1.2.4, Songwriter0.2.3), 6/6 compile +5/5 isolated checks, но Skills отсутствовали в её текущей сессии. Это не даёт права считать **прочие 19 пакетов** неисправными или исправными без пообъектной проверки.
- Запрещено заново разрабатывать ND или менять каноническую архитектуру вместо устранения доказанного route/visibility дефекта. Сохраняй A1 замороженным, NotebookLM optional, no paid routes/audio.

**Результат:** полная поимённая инвентаризация и квалификация launcher-плагинов; устранение только доказанных расхождений; продолжение автономно без рутинного Go.
