---
name: nd-writer-orchestra-runtime
metadata:
  version: "1.0.5"
  semantic-id: "ND-WRITER-ORCHESTRA-RUNTIME-1"
  status: "CANONICAL — SOLE CURRENT WRITER-ORCHESTRA RUNTIME PROTOCOL"
---
# ND Writer Orchestra Runtime
Status: CANONICAL / SOLE CURRENT
Effective: 2026-09-27
Binding invariant: ND-COGNITIVE-RUNTIME-1 + ND-LAUNCHER-CONTRACT-v6
## Purpose
Make the already-designed Writer orchestra executable under the current ND nervous system without external supervisor hosting. Drive remains durable artifact/state storage; Linear remains current navigation/currentness; LM/NotebookLM remains semantic memory/source analysis; cognitive control remains inside ChatGPT.
## Exact runtime binding

Every executable Writer-domain edge MUST use an exact CURRENT launcher URI resolved from the StateHead-bound Registry. Human names, semantic IDs, bare `nd-*` IDs and `@ND` aliases are descriptive metadata only.

- True Writer: `skills://plugins/nd-true-writer/nd-launch-true-writer`
- Books Creator: `skills://plugins/nd-books-creator/nd-launch-books-creator`
- Literary Critic: `skills://plugins/nd-literary-critic/nd-launch-literary-critic`
- Story Architect: `skills://plugins/nd-story-architect/nd-launch-story-architect`
- Technical Writer: `skills://plugins/nd-technical-writer/nd-launch-technical-writer`
- True Research peer: `skills://plugins/nd-true-research/nd-launch-true-research`
- True Memory peer: `skills://plugins/nd-true-memory/nd-launch-true-memory`
- Automation Agent root: `skills://plugins/nd-automation-agent/nd-launch-automation-agent`

Every child/peer call carries `caller_launcher_uri`, `target_launcher_uri`, `owner_launcher_uri`, `return_to_launcher_uri`, `assignment_id`, `correlation_id`, and `runtime_generation` as applicable. RETURN addresses the already-live caller and MUST NOT re-invoke it. Re-entry through a launcher occurs only when the expected caller/parent is absent and CURRENT runtime identity still matches.

## Runtime identities
- `skills://plugins/nd-true-writer/nd-launch-true-writer` / `ND-SKILL-TRUE-WRITER-1` — Writer-domain supervisor / conductor; literary adjudication owner and parent of the technical-reporting lane.
- `skills://plugins/nd-books-creator/nd-launch-books-creator` / `ND-SKILL-BOOKS-1` — literary prose executor.
- `skills://plugins/nd-literary-critic/nd-launch-literary-critic` / `ND-SKILL-LITERARY-CRITIC-1` — diagnostic specialist.
- `skills://plugins/nd-story-architect/nd-launch-story-architect` / `ND-SKILL-STORY-ARCHITECT-1` — non-local structural specialist.
- `skills://plugins/nd-technical-writer/nd-launch-technical-writer` / `ND-SKILL-TECH-WRITER-1` — technical-reporting child of True Writer; separate from the literary acceptance loop.
- `skills://plugins/nd-true-research/nd-launch-true-research` / `ND-SKILL-TR-1` — existing bounded research supervisor, callable by True Writer when research is materially required.
- `skills://plugins/nd-true-memory/nd-launch-true-memory` — existing internal ChatGPT memory/currentness actor; Drive/LM/Linear are its memory/state surfaces, not replacements for cognition.
## Control transfer
Normal internal delegation:
`parent/task owner live -> bounded CHILD or PEER_SERVICE call -> child/service execution focus -> verified typed return -> parent/task owner continues`.
### Native same-context execution
A separate process/subagent service is **not required**. The native ChatGPT mechanism is a cooperative logical actor switch inside the same ChatGPT execution context:
`preserve live parent continuation -> activate bounded child as current execution focus -> produce typed correlated return -> close child call -> parent continues as already-live owner`.
Execution focus means the child performs only its bounded assignment while the parent retains task ownership, objective, authority and continuation. It does not require parallel execution or an external runtime. The child receives only its bounded assignment plus necessary context and its own current skill contract; the parent does not issue competing child-level decisions during that bounded call.
This same-context mechanism is the default when no stronger qualified native child-isolation primitive is available. It satisfies cognitive identity locality because every role remains inside ChatGPT.
One ND role is the current execution focus at a time while higher-level ownership remains logically live. Sibling Writer Children/peers never execute concurrently in CURRENT production. A leaf specialist returns to its parent and does not route siblings. True Writer owns the Writer-domain orchestra: the literary lane plus the bounded Technical Writer reporting lane, and adjudicates every return before deciding whether another child is needed.
Typical qualified literary chain:
`skills://plugins/nd-automation-agent/nd-launch-automation-agent -> skills://plugins/nd-true-writer/nd-launch-true-writer -> skills://plugins/nd-books-creator/nd-launch-books-creator -> typed RETURN to live True Writer -> skills://plugins/nd-literary-critic/nd-launch-literary-critic -> typed RETURN to live True Writer -> typed RETURN to live Automation Agent`.
Qualified technical-routing shape:
`authorized exact caller URI -> skills://plugins/nd-true-writer/nd-launch-true-writer -> skills://plugins/nd-technical-writer/nd-launch-technical-writer -> typed RETURN to live True Writer -> typed RETURN to original caller URI`.
Adaptive literary chains may also include True Memory, True Research, and Story Architect. True Memory and True Research may be called as bounded PEER_SERVICE capabilities without transferring True Writer's literary task ownership. Technical Writer remains outside literary acceptance and uses the same bounded live-parent / child-return runtime contract. No fixed literary pipeline is required.
## Child assignment envelope
Required fields:
- `assignment_id`
- `correlation_id`
- `parent_launcher_uri`
- `child_launcher_uri`
- `objective`
- `operation`
- bounded `context` and/or authoritative `context_refs`
- `authority_ceiling`
- `negative_boundary`
- `done_when`
- `expected_result_type`
- `return_to_launcher_uri`
- `runtime_generation`
- `continuation_pointer`
- `replay_key` (default = `assignment_id`)
The assignment may narrow authority but never amplify it. Missing/stale/mismatched authority or actor identity fails closed.
## Child return envelope
Required fields:
- `assignment_id`
- `correlation_id`
- `child_launcher_uri`
- `return_to_launcher_uri`
- `status`
- `result_type`
- `material_result`
- material coverage/evidence where relevant
- `unresolved` or blocker when relevant
- bounded external-tool/effect receipts when material
- `continuation_pointer`
Normal statuses include the role's own semantic statuses plus bounded runtime states such as `COMPLETE`, `PARTIAL`, `BLOCKED_CONTEXT`, `NEEDS_PARENT_DECISION`, and `FAILURE`. Leaf output never becomes a final literary decision merely by returning successfully.
## Return / adjudication
On child return:
1. parent verifies assignment/correlation/runtime-generation and exact return launcher URI;
2. parent reads the typed material result;
3. parent adjudicates it under its own authority;
4. parent chooses stop, another child assignment, or upward return;
5. returned child call closes; the parent remains the live owner.
`ASSIGNED != ATTEMPTED != OBSERVED != VERIFIED` remains binding. Linear/Drive persistence alone does not prove cognitive execution.
## Resumable continuation
For interruption-sensitive campaigns use the required observable-state contract in:
`tools/writer-eval/runtime-handoff/CONTINUATION_CONTRACT.md`.
The checkpoint stores actor stack, correlation/replay state, authoritative context references, material decisions/blockers, and next transition only. It MUST NOT store private chain-of-thought.
## Replay / interruption
- `replay_key` prevents duplicate material side effects.
- Pure analysis/prose may be deliberately rerun only as a new/fresh assignment or an explicitly marked replacement run.
- `continuation_pointer` identifies compact state required for the live parent to continue correctly after interruption.
- Recovery starts from current navigator/state pointers, then restores only the active actor stack and necessary bounded context.
## External boundary
External tools/models/providers may support the currently active actor but never become True Writer or a subordinate ND cognitive identity. External `agent_orchestrate`, provider substitution, one-service-per-supervisor, or Railway/MCP-hosted supervisor identity is REJECTED / DO_NOT_ROUTE.
## Runtime qualification status
The current runtime is adopted as the sole Writer-orchestra runtime. Qualification record:
- Q1 identity/routing resolution;
- Q2 parent -> child bounded call with parent ownership preserved, including same-context logical actor switching;
- Q3 correlated child return and parent continuation without ownership reconstruction;
- Q4 replay/idempotency behavior;
- Q5 BLOCKED_CONTEXT/failure return;
- Q6 adaptive multi-child Writer loop;
- Q7 external tool use without identity transfer;
- Q8 interruption/continuation recovery where the ChatGPT host exposes a usable primitive;
- Q9 end-to-end Agent -> True Writer -> child -> True Writer -> Agent.
Same-context logical actor switching counts as live internal ChatGPT execution when observable activation/call/return/continuation semantics are exercised. Do not require or create a separate spawn/subagent cognitive runtime merely for process separation. Fresh-context interruption/recovery remains an explicit qualification dimension and must not be inferred from same-context success.
## Continuation Contract
Status: CANONICAL / CURRENT
Binding: `ND-COGNITIVE-RUNTIME-1`
Purpose: required resumable state for same-context handoff and future clean-context recovery qualification.
## Principle
Persist **observable continuation state, not private chain-of-thought**.
A continuation checkpoint exists so a later ChatGPT invocation can reconstruct the compact live ownership/call stack needed to continue without replaying or inventing child outcomes.
## ResumeCheckpoint
Required fields:
```yaml
schema: ND-WRITER-CONTINUATION-1
checkpoint_id: <stable unique id>
correlation_id: <campaign correlation>
runtime_mode: SAME_CONTEXT_LOGICAL_CALLS
phase: PARENT_READY | CHILD_ACTIVE | CHILD_RETURNED | PARENT_CONTINUING
active_launcher_uri: <current exact launcher URI or null at persisted boundary>
actor_stack:
  - launcher_uri: <parent exact launcher URI>
    assignment_id: <assignment>
    continuation_pointer: <pointer>
    objective: <bounded objective>
    authority_ceiling: <bounded authority>
    done_when: <completion predicate>
pending_child:
  assignment_id: <child assignment or null>
  child_launcher_uri: <child exact launcher URI or null>
  expected_result_type: <typed return>
  return_to_launcher_uri: <parent exact launcher URI>
replay_ledger:
  <replay_key>:
    state: ASSIGNED | ATTEMPTED | OBSERVED | VERIFIED
    result_ref: <typed receipt ref or null>
context_refs:
  - <current authoritative pointer only>
material_decisions:
  - <accepted observable decision necessary to resume>
blockers:
  - <material blocker only>
next_transition: <activate child | validate return | parent adjudicate | return upward>
written_at: <timestamp>
currentness_token: <provider revision/hash when persisted durably>
```
## Persistence boundaries
Persist/checkpoint only when materially useful:
1. immediately before a parent opens a material child call if interruption risk is material;
2. after a child return is VERIFIED but before parent adjudication if that boundary may be interrupted;
3. before returning upward when the campaign must survive a fresh invocation;
4. on explicit BLOCKED/STALL where a reopening condition exists.
Do not persist every sentence, tool call, or hidden reasoning step.
## Recovery
A fresh ChatGPT invocation must be able to recover by:
`NAM-143 -> exact StateHead-bound Registry -> NAM-140 -> current Writer runtime pointer -> ResumeCheckpoint -> current authoritative context_refs -> restore actor_stack -> execute next_transition`.
Recovery rules:
- fresh/current pointers beat stale checkpoint assumptions;
- verify the checkpoint currentness token when consequential;
- never replay a `VERIFIED` replay key;
- never infer a child result from ledger persistence alone;
- if `phase=CHILD_ACTIVE` and no VERIFIED child receipt exists, treat the child outcome as UNKNOWN, not complete;
- if authority/currentness changed materially, fail closed and replan at the nearest surviving parent;
- external systems may store/read the checkpoint but never become the active cognitive actor.
## Same-context execution
Within one ChatGPT execution context, the checkpoint may remain transient if interruption risk is negligible. The logical state transition is still:
`parent LIVE_OWNER -> checkpoint continuation -> child ACTIVE_FOCUS -> typed return -> child call CLOSED -> parent CONTINUES`.
## Clean-context recovery contract
On a future/fresh ChatGPT invocation with no usable conversational history of the prior campaign, recovery from a persisted ResumeCheckpoint plus CURRENT pointers must:
1. identify the live parent owner and pending/returned child-call state;
2. avoid replaying VERIFIED child work;
3. restore the parent at the right continuation point;
4. produce the same next control decision from the persisted observable state;
5. record a new verified continuation receipt.
These are production recovery invariants, not a standing qualification tail. A future field regression may test them, but no alternate Writer runtime or recovery route is retained.
