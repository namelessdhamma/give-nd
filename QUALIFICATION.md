# ND → Ksyusha — CURRENT Qualification Matrix

Authority for source comparison: `NAM-143 -> bound CURRENT Registry -> exact component/launcher`.
Source baseline at this rebase: Registry `1.64.2`, publication `ND-ANTI-HANG-TAIL-HARDENING-FINAL-20261004-1`.

Every gate is PASS/FAIL with provider/readback evidence. A historical transfer file, copied ID, successful tool call, or source prompt does not establish CURRENT.

## A. Source-package currentness
- [ ] Registry 1.64.2 exact snapshot present and hash-matched.
- [ ] 31 CURRENT components accounted for.
- [ ] 22 CURRENT launchers accounted for.
- [ ] Explicit Anti-Hang launcher present.
- [ ] Automation Agent 1.3.2 / plugin 1.7.3 selected.
- [ ] Anti-Hang 1.6.0 / plugin 1.2.0 selected.
- [ ] True Memory 0.4.2, True Research 1.8.2, True Developer 0.4.2, True Writer 0.9.2, True Visual 0.2.2, True Doctor 0.4.2, Generation 15.2 selected.
- [ ] Predecessor 1.60.x–1.64.1, Anti-Hang 1.2.x/1.5.0 and old Agent/message-policy artifacts are provenance only.
- [ ] Runtime/bootstrap source differs from current main only where explicitly classified as provenance or target-specific rebind.
- [ ] A1 current source is NAM-619; NAM-167/NAM-129/NAM-130 are predecessor provenance only.
- [ ] Secret scan passes.

## B. Authority
- [ ] Exactly one target StateHead exists.
- [ ] Target StateHead binds exactly one target CURRENT Registry.
- [ ] Target Registry resolves exact target-active component/launcher graph.
- [ ] Source account IDs cannot become selectable target currentness.
- [ ] Former/alternate StateHeads are nonselectable provenance only.
- [ ] Target StateHead is published LAST after underlying provider readbacks.
- [ ] Cold recovery succeeds from target StateHead without this transfer prompt.

## C. Launcher graph
- [ ] All 22 launchers are visible/callable.
- [ ] `skills://plugins/nd-anti-hang/nd-launch-anti-hang` is explicit and callable.
- [ ] Launcher Contract v6 relationships match source CURRENT.
- [ ] Automation Agent remains root.
- [ ] Anti-Hang remains cross-cutting runtime, not controller.
- [ ] Developer Executor is nested under True Developer at `skills://plugins/nd-true-developer/nd-launch-developer-executor`.
- [ ] No stale native/v5/predecessor route overrides CURRENT v6 bindings.
- [ ] External Connecting remains recovery/route-creation support, not cognitive owner.

## D. Automation Agent orchestration
- [ ] Every user task enters Anti-Hang TASK_ENTRY.
- [ ] Every substantive task passes True Memory TASK_MEMORY_GATE.
- [ ] Exact substantive Supervisor is invoked.
- [ ] At least one owned Child/helper executes for each substantive Supervisor call.
- [ ] Applicable Critic/acceptance executes before substantive return.
- [ ] Material returns re-enter Automation Agent root.
- [ ] Same Supervisor/Child may be invoked AGAIN when materially needed.
- [ ] Missing owner/Child route triggers recovery; Agent/parent does not imitate the missing owner.
- [ ] No ritual fan-out.
- [ ] Internal cycle rendering defaults to SILENT_CONTINUE; no routine `Go`.

## E. True Memory
- [ ] TASK_MEMORY_GATE emitted for substantive task.
- [ ] Long/complex work binds or creates one appropriate TEMP_TASK when required.
- [ ] Supervisor/Children share one bounded semantic context chain; Child does not create competing persistent memory root.
- [ ] Rebind/requery occurs only when accepted material information made the current packet decision-stale.
- [ ] CORE persists.
- [ ] ACTIVE_PROJECT persists while useful/active.
- [ ] TEMP_TASK cleanup executes through True Memory -> Inquisitor before completion.
- [ ] Cleanup readback proves retired/deleted TEMP_TASK is not selectable.
- [ ] Cold recovery does not resurrect retired TEMP_TASK.

## F. Supervisor chains
- [ ] Research -> owned Child/helper -> Research Critic -> repair/recheck when material.
- [ ] Developer -> Developer Executor -> Developer Critic -> Executor AGAIN after material finding -> targeted recheck.
- [ ] Writer -> Writer Child -> Literary Critic -> repair/recheck when material.
- [ ] Visual -> Visual Creator -> True Visual acceptance.
- [ ] Doctor -> required CURRENT peer/helper service(s) -> verified incident closure.
- [ ] Mandatory receipts/verdicts are present where CURRENT contracts require them.

## G. Anti-Hang 1.6.0
- [ ] Seven events supported: TASK_ENTRY, BEFORE_ACTION, AFTER_ACTION, AFTER_MATERIAL_RETURN, PRESSURE, BEFORE_USER_RETURN, USER_STOP.
- [ ] Each external action has unique action_id.
- [ ] BEFORE_ACTION(action_id=X) precedes matching AFTER_ACTION(action_id=X).
- [ ] Exact external-action, MATERIAL-return and PRESSURE counts match trace.
- [ ] Exactly one TASK_ENTRY occurs at trace start.
- [ ] PRESSURE hook is present when pressure was observed.
- [ ] USER_STOP freezes new operations on the stopped branch.
- [ ] USER_STOP never assumes remote provider cancellation.
- [ ] Ambiguous consequential effect reconciles before replay.
- [ ] Broad opaque prepare/write/readback composites are isolated.
- [ ] Nonterminal external effect blocks only dependent frontier.
- [ ] Unchanged status is not blindly polled without material wake.
- [ ] Safe runnable work causes AUTO_CONTINUE.
- [ ] GLOBAL_WAIT_EXTERNAL occurs only after a complete scan proves no runnable/reconcile/recovery/wake work.
- [ ] BEFORE_USER_RETURN is the final whole-task hook.
- [ ] Malformed/missing-order/missing-pair/multiplicity traces fail closed toward repair/continuation.

## H. Message policy
- [ ] Ordinary internal hooks, handoffs, readbacks, recovery hops, pressure changes, phase changes and safe-cycle rotations are silent.
- [ ] 100 ordinary internal cycles produce 0 routine visible progress messages.
- [ ] Visible progress appears only for explicit request or user-significant milestone/finding/blocker/external-wait/direction-change/recovery anchor.
- [ ] COMMITTED_CYCLE_AUTO_REENTER is exceptional, not routine per-cycle narration.
- [ ] No claim of fresh outer-turn reset, guaranteed UI persistence, guaranteed client interruptibility or guaranteed provider cancellation.

## I. External recovery
- [ ] FAILED_ROUTE != FAILED_CAPABILITY.
- [ ] Consequential ambiguous effect -> readback/reconcile before retry/failover.
- [ ] Qualified same-capability reserve is tried when semantically appropriate.
- [ ] Permission denial, stale revision, invalid payload/schema and semantic/domain errors are repaired rather than blindly cross-provider replayed.
- [ ] Generation 15.2 executes MANDATORY_RECOVERY_FRONTIER.
- [ ] If no existing CURRENT route satisfies semantics, External Connecting is invoked.
- [ ] Recovery never transfers substantive ownership away from original owner.
- [ ] Only exact irreducible TRUE_GATE stops the affected branch/task.

## J. Isolation
- [ ] Source OAuth/API keys/cookies/private keys/service secrets absent.
- [ ] Source personal memory/mail/calendar/contact payload absent.
- [ ] Excluded project payload not ACTIVE/SELECTABLE: Blue Sea; Geny Gieny; Nibbana-conditions research project.
- [ ] Other source personal/product project payload not activated unless explicitly authorized.
- [ ] Architecture/fault-tolerance references retained only as nonselectable evidence/provenance where structurally required.
- [ ] Source ND cannot access target personal/project state and target clone cannot inherit source credentials.

## K. A1 Self-Evolution
- [ ] Exactly one CURRENT self-evolution contour: A1 / NAM-619 semantics.
- [ ] Modes preserved: SYSTEM_AUDIT, FIELD_HISTORY_AUDIT, EXTERNAL_HORIZON_SCAN, CAPABILITY_EXPERIMENT, DEFECT_REPRODUCTION, SELECTIVE_EVOLUTION.
- [ ] Default state remains research-first under FREEZE.
- [ ] SELECTIVE_EVOLUTION is rare/evidence-gated and executed by proper CURRENT owner.
- [ ] Old A1/A2/A3 contours are provenance only; no active A2/A3 predecessor scheduler is recreated.

## L. Publication / cold handover
- [ ] Target provider objects and routes read back before authority publication.
- [ ] Target StateHead publication occurs last.
- [ ] Fresh target chat with only `@ND Automation Agent + normal goal` cold-recovers target CURRENT.
- [ ] One substantive Supervisor/Child/Critic chain completes.
- [ ] One target durable effect writes and reads back.
- [ ] One injected route failure recovers without user provider-choice choreography.
- [ ] Final result satisfies the semantic goal without routine `Go`.

Target qualification cannot be marked PASS until target-owned provider objects exist and the cold-run evidence above is collected.
