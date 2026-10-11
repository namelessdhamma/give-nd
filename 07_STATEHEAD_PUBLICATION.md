# Stage 07 — Publish verified target Registry successor LAST

MODE: UPDATE_EXISTING_TARGET. Ksyusha already has a target authoritative StateHead. This stage MUST update **that exact issue** through a serialized guarded transaction, never create a second StateHead or reset provider ownership.

## Preconditions (all actual provider evidence)

- Recover currently active Ksyusha StateHead and old Registry, including exact preupdate head/token/anchor.
- Stage06 receipt = PASS from real target providers, including `ANTI_HANG_INSTALLATION_GATE_STAGE06.json` all mandatory checks PASS and current target canonical/provider hashes.
- 32 target-scoped components, 23 target-scoped launchers, 23 plugin bundles (22 launcher-backing plus recovery skill), target exact IDs and source/currentness isolation.
- Excluded source audio family TRUE_SOUND, STUDIO_EXECUTOR, SOUND_CRITIC and active Studio project do not enter target authority.
- No unresolved ambiguous effect and no concurrent writer whose expected old target StateHead anchor would be stale.

## Execution

1. Verify exact old target StateHead and target Registry by provider readback. If absent, this task is not a license to rebootstrap; return a TRUE_GATE for separately authorized new installation.
2. Reconcile unchanged verified target components; read back every new/changed source-correct target canonical/plugin artifact. Publish and verify successor target Registry in Ksyusha-owned Drive, with new own ID/hash and old-target provenance.
3. Complete necessary checkpoints/receipts **before** authority mutation: `TARGET_INSTALL_STATE.json` = `PUBLICATION_PENDING`, exact old head, successor Registry ID/hash and Stage06 actual PASSES.
4. Guard on exact OLD target StateHead anchor; no blind overwrite on conflicts. Update **existing** Linear target StateHead LAST to exactly the successor target Registry. No source NAM-143 provider IDs become target authority.
5. Read back target StateHead and verify single authority and exact successor binding. Do no more underlying architectural mutations in this transaction. This is an UPDATE from target CURRENT to target CURRENT, not BOOTSTRAP-to-CURRENT.
6. On conflict or uncertain commit, read back and reconcile the existing effect before any new attempt. Never bypass Stage06 gates.

## Result

Return target StateHead URL, successor target Registry ID/hash, actual publication verdict and only real blockers. After Stage07 PASS, Ksyusha must open a separate clean chat to run [08_COLD_QUALIFICATION.md](08_COLD_QUALIFICATION.md) with [ANTI_HANG_INSTALLATION_GATE.md](ANTI_HANG_INSTALLATION_GATE.md). No Stage08 PASS may be inherited from Stage06 or the source package.
