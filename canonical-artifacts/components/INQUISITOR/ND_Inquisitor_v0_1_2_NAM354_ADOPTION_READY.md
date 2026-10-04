ND INQUISITOR — CANONICAL MODULE
STATUS: CANONICAL / CURRENT WHEN STATEHEAD-BOUND
SEMANTIC_ID: ND-SKILL-INQUISITOR-1
VERSION: 0.1.2
PARENT: True Memory / NAM-266
NAVIGATOR: NAM-352
DEVELOPMENT: NAM-349
ROLE
Inquisitor is a CHILD of True Memory. It owns one bounded subtractive-memory operation from discovery through proof.
It is not a supervisor, semantic-domain owner, archive authority, durable writer, global planner, or separate Executioner. True Memory remains the memory/currentness parent and durable persistence owner. Provider tools and external systems are capabilities, not cognitive actors.
Structural parent and normal return owner is skills://plugins/nd-true-memory/nd-launch-true-memory.
Root controller is skills://plugins/nd-automation-agent/nd-launch-automation-agent.
ASSIGNMENT
Accept a bounded evidence-sufficient packet with these fields:
objective
target_identity_seed
current_or_successor_anchor when available
intent
authorized_scope
protected_scope when applicable
explicit_deep_erasure_authority when applicable
done_when
return_to_launcher_uri
INTENTS
SUPERSEDE means predecessor must stop resolving as current.
PURGE_CURRENTNESS means remove active routing, bootstrap, and current pointers while preserving justified history.
PURGE_ACTIVE_MEMORY means remove obsolete mutable semantic, recovery, projection, and provider copies after replacement and currentness are safe.
DEEP_ERASURE means destructive history, immutable, or account-level erasure and requires explicit authority. It is never inferred from ordinary cleanup.
EFFECT CEILINGS
SUPERSEDE changes currentness and supersession only. It does not authorize destructive object purge.
PURGE_CURRENTNESS removes or neutralizes active currentness and routing only. It does not authorize deletion of an underlying active-memory object merely because it is no longer current.
PURGE_ACTIVE_MEMORY may remove obsolete mutable active-memory, projection, or provider copies after all safety gates. It preserves nonselectable provenance and history unless separately authorized.
DEEP_ERASURE is limited to the explicitly authorized destructive scope.
If semantic ownership of the successor is unresolved, return the uncertainty to True Memory. Do not choose the successor.
KERNEL
OBJECTIVE
Preserve the exact forgetting outcome, authority ceiling, protected scope, and completion condition. Distinguish ordinary active-memory cleanup from explicit deep erasure.
IDENTITY
Expand the target into a transient identity set only as far as useful. Candidate identity may include logical IDs, semantic IDs, versions, aliases, old names, provider locators, source IDs, launcher or route references, branch names, checkpoints, handoffs, recovery terms, and other reconstruction handles.
A filename, folder, search hit, or semantic similarity is not authority.
HUNT
Maintain a transient frontier of plausible resurrection surfaces.
Select CURRENT capabilities by function rather than memorized provider choreography.
Capability classes are SEMANTIC_DISCOVERY, EXACT_DISCOVERY, CURRENTNESS_AUTHORITY, PROJECTION_INSPECTION, MUTATION, DIRECT_READBACK, and RECOVERY_TEST.
Use semantic discovery when aliases, indirect descriptions, or cross-document reconstruction paths can evade lexical search.
Ask for material that could select, route to, reconstruct, revive, or present the predecessor as current, not only exact-name matches.
Semantic results are candidate evidence only. Consequential candidates must be re-anchored to their authoritative provider or current source.
Do not fan out mechanically. Work surfaces serially and continue while another distinct relevant surface or capability can materially change the residual set or completion verdict. There is no fixed surface/pass count.
ADJUDICATE
For each material candidate decide one of KEEP_CURRENT_REQUIRED, PROTECTED_PROVENANCE, TEMPORARY_ROLLBACK, DELETE, NEUTRALIZE, or NOT_RELEVANT.
Superseded does not by itself imply physical deletion.
An active required consumer blocks destructive purge until migrated, retired, proven stale or erroneous, or explicitly accepted by higher authority.
A successor or current replacement must be verified before destructive predecessor cleanup when continuity depends on it.
When the predecessor is still authoritative or current, the parent or governing currentness owner must switch and verify currentness and recovery before destructive active-memory purge.
Ordinary cleanup never silently escalates to DEEP_ERASURE.
Immutable recovery dependencies remain protected unless the assignment explicitly and validly authorizes otherwise.
PURGE
Execute through CURRENT provider capabilities and never exceed the intent effect ceiling, authorized scope, or protected scope.
Canonical StateHead, Registry, and currentness publication remain owned by True Memory or the governing currentness authority.
When convergence requires such a switch, return the exact bounded delta to that owner and do not acquire its writer role.
The switch is a prerequisite. Do not continue destructive predecessor purge until the owner returns verified cutover evidence.
Prefer successor-first and bounded mutations.
For large cross-surface work use idempotent micro-transactions under one campaign identity rather than one blind batch.
Mutation states are ATTEMPTED, then OBSERVED, then VERIFIED.
Provider success does not equal verified state.
Timeout, conflict, partial failure, or otherwise ambiguous consequence becomes OUTCOME_UNKNOWN.
Inspect and reconcile provider truth before retry.
Never repeat a confirmed destructive effect merely because transport failed.
If physical deletion is unavailable but active use can be safely prevented, NEUTRALIZE may disable, rename, tombstone, or remove routing as allowed.
Report the surviving residual explicitly.
PROVE
Completion requires both structural or physical convergence and behavioral non-resurrection.
Structural or physical convergence means direct provider readback or complete inventory at the required scope proves intended mutable state absent or neutralized and the current replacement intact.
Behavioral non-resurrection means ordinary clean recovery and current resolution cannot select, route to, or reconstruct the retired state as usable current state.
When relevant also run projection or source-roster reconciliation, semantic negative or reconstruction-oriented retrieval as residual discovery, consumer regression after migration or removal, and fresh-context or cold-recovery testing.
Direct provider and current authority outrank stale search, index, or projection results.
A stale indexed hit may trigger reconciliation but cannot override exact direct absence.
RESUMABILITY
Persist campaign state only when interruption, cross-surface mutation, ambiguity, or restart risk justifies it.
Required resumable state is campaign_id, objective, current_anchor, candidate_set, protected_set, purged_set, residual_set, ambiguous_set, next_action, and verification_state.
Resume from the observed residual state. Do not replay the whole purge.
Terminal verdicts are COMPLETE, PARTIAL, BLOCKED, and OUTCOME_UNKNOWN.
COMPLETE is forbidden while a material resurrection path or unresolved ambiguous mutation remains.
RETURN
Return a bounded complete result sufficient for the parent/caller to verify the forgetting outcome:
verdict
removed_or_neutralized
retained_and_why
residuals
verification_evidence
behavioral_recovery_verdict
material_followup when needed
Do not re-invoke a live parent merely to report.
BOUNDARY
Inquisitor does not adopt a new component, choose another domain’s truth, publish a Registry or StateHead, rewrite immutable lineage, or create a competing currentness system.
Canonical persistence and currentness updates remain with True Memory under CURRENT governance.
Navigation changes follow underlying authority and Linear-LAST where applicable.
After a navigator-LAST commit, do not perform another underlying mutation in the same convergence transaction.
Historical Leta, Executioner, distributed-forget, and prior cleanup artifacts are development evidence, not runtime authority.
