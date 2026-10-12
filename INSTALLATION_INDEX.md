## EXISTING PARTIAL INSTALL — USE STAGE U FIRST

Если у Ксюши уже существует XEN-5 с Registry1.64.2 (31/22) и Stage08 BLOCKED без Songwriter, **не запускай повторный первоначальный Stage01–07 или Stage08 без обновления**. Следуй самостоятельному [UPDATE_IN_PROGRESS.md](UPDATE_IN_PROGRESS.md): Stage U1–U5 — одна возобновляемая дельта-операция плюс целевая квалификация с отдельными квитанциями. Это НЕ девятый этап первоначальной установки. После фактической целевой публикации и холодного теста обновления вернись к полному Stage08 и его нерешённым тестам.

**Human Output source qualification PASS (2026-10-12):** [GitHub Actions](https://github.com/namelessdhamma/give-nd/actions/runs/38228524520) — 262 integrity/builder checks + 137 clean-install executable Human Output checks; **0 failures**. Previous 253-check link elsewhere in this document is historical. Ksyusha target Stage06/Stage08 remain NOT_RUN.

**2026-10-12 UPDATE:** New Human Output gate [HUMAN_OUTPUT_INSTALLATION_GATE.md](HUMAN_OUTPUT_INSTALLATION_GATE.md) is mandatory in existing Stage06 and fresh Stage08 alongside, not instead of, Anti-Hang. Transfer the exact installed Agent plugin 1.7.8 package and script; upstream Registry 1.66.1 is the source authority and retains an older 1.7.5 launcher binding. Ksyusha's target candidate must explicitly adopt the reconciled 1.7.8 delta after readback; never downgrade a target-owned newer qualified package.

# ND → Ksyusha — INCREMENTAL UPDATE INDEX

SOURCE: **VERIFIED PASS (253 checks, 0 findings, [GitHub Actions](https://github.com/namelessdhamma/give-nd/actions/runs/38132059956))**. TARGET: **NOT_RUN** until owner-account Stage06 and fresh-chat Stage08.

MODE: **UPDATE_EXISTING_TARGET**, preserve Ksyusha's installed StateHead, verified target provider bindings and already-current components. Never rebuild an existing qualified target component merely because the source file changed.
SOURCE: NAM-143 → Registry **1.66.1** / SHA-256 `1da459ac1027e234b5d1860625e3b79fb7ca8b0d574ffbc0b739941fa438cc71`.
SCOPED SOURCE PROJECTION: [32 components / 23 launchers](canonical-artifacts/ND_CAPABILITY_REGISTRY_KSYUSHA_SCOPE_FROM_v1_66_1.json); source-only, NONAUTHORITATIVE pending target rebind.
SOURCE PLUGINS: 23 functional bundles (22 launcher-backing, plus External Connecting).
GATE: [ANTI_HANG_INSTALLATION_GATE.md](ANTI_HANG_INSTALLATION_GATE.md), Stage06 and Stage08 only.

## Entry

Ksyusha sends only the message in [START_HERE.md](START_HERE.md). Stages are installer-internal transactions and auto-advance once accepted; no routine per-stage `Go` prompts.

**Before any write**, discover her EXISTING root and target `migration/TARGET_INSTALL_STATE.json`, existing Plugin Creator packages and target provider truth. Build the smallest safe delta against the new in-scope source projection. Each old stage becomes an idempotent inspection, selective upgrade or readback:
- `PASS_ALREADY_CURRENT` if actually evidenced equivalent;
- `UPDATE_WITH_READBACK` only when target upgrade is necessary;
- `BLOCKED` or `NOT_RUN` otherwise.

## The existing stage sequence (no ninth stage)

| Internal stage | Delta work for existing target | Must preserve |
| --- | --- | --- |
| [01](01_FOUNDATION_DRIVE_LINEAR.md) | Locate target StateHead/Registry/Drive/receipts; verify ownership; checkpoint | Original target root and all already-qualified system objects |
| [02](02_CORE_RUNTIME_EXTERNAL_CONNECTING.md) | Upgrade Agent 1.3.5/plugin1.7.8 and Anti-Hang1.7.0/plugin1.2.1 with exact source files/readback; retain Generation and External Connecting | Target provider account authority and live effect identities |
| [03](03_NOTEBOOKLM_SEMANTIC_MEMORY.md) | Verify target memory route/current notebooks if needed; defer absent nonessential NotebookLM provision to separate authorized task without claiming a TEMP_TASK test PASS | No new competing semantic Core; no original notebook deletion |
| [04](04_RESEARCH_STACK.md) | Verify/reuse existing Research and other unchanged Children; only repair proven mismatch | No unnecessary research/plugin recreation |
| [05](05_WRITING_VISUAL_STACK.md) | True Writer0.9.3/plugin1.2.4, Writer Orchestra1.0.6, new Songwriter0.2.3 under Writer; retain Literary Critic | No True Sound or music Studio |
| [06](06_REGISTRY_PREPUBLICATION.md) | Reconcile 32/23 scoped binding graph, all changed plugin and canonical sources, target-owned IDs, `ANTI_HANG_INSTALLATION_GATE` prepublication receipt | No false PASS; fail closed |
| [07](07_STATEHEAD_PUBLICATION.md) | Guarded serialized update of **existing target StateHead** to exactly one verified target successor Registry LAST | No duplicate StateHead, no authority cutover on a failed gate |
| [08](08_COLD_QUALIFICATION.md) | New clean-chat independently test root, Anti-Hang three subcycles and physical Songwriter→Critic chain; verify target-owned readbacks | Source-account secrets/projects and excluded audio remain absent |

Only Stage08 must be in a separate new clean chat. Stage01–07 run automatically under one initial user authorization, across internal safe subcycles; confirmed external authorization is the only routine user action.

## Required update-specific invariant

A missing capability is recovered via the current reserve/Generation/External Connecting chain, not fake completion. Preserved healthy target CORE and ACTIVE_PROJECT may remain; no `TEMP_TASK` lifecycle PASS without real creation, actual Inquisitor cleanup, and provider-verified absence.

For changes to live StateHead, insist on exact old anchor and serialized single-writer; write all target artifacts and stage receipts before publication; statehead publication is the LAST authoritative write in that transaction. Reruns reconcile each existing effect rather than replaying consequences.

## Evidence and freeze boundary

Source transfer files have provider-observed source IDs/hashes and functional plugin bundle content. Source `1.66.0` includes three excluded audio components; the target 32/23 graph is explicitly SCOPED, not a forged unchanged source Registry hash. Its successor MUST be generated with verified target-owned provider bindings.

Historical `SOURCE_STAGED_INSTALLATION_CLOSURE_RECEIPT.json`, `CURRENT_TRANSFER_BASELINE.json` (prior versions) and previous publication receipts are provenance only unless a new actual qualification result says otherwise.

**Source CANDIDATE ≠ Ksyusha target PASS.** Do not claim target Stage06/08 passed until the separate actual receipts exist.
