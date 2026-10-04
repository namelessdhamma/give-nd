# ND Generation — v15.2 — Mandatory Hook Enforcement

Status: ADOPTION_READY / CURRENT ONLY WHEN NAM-143-BOUND

## MANDATORY HOOK ENFORCEMENT — BINDING OVERRIDE — 2026-10-03

Source merge: `411066b5b9f3c8335558054a3245a48323c5e359`  
Qualification: `ND-MANDATORY-HOOK-ENFORCEMENT-HARDENING-20261003`  
Publication target: `ND-MANDATORY-HOOK-ENFORCEMENT-20261003-1`

This successor preserves the predecessor's domain semantics except where this override is stricter. The stricter rule wins over any predecessor wording such as `may`, `prefer`, `should`, `when useful`, `reasonable expected value`, trivial/direct fallback, or milestone-based closure.

Binding invariants:
- `MISSING_GATE_EVALUATION != AUTHORIZATION`.
- `SIMPLE_TASK != NO_DELEGATION`.
- `EVERY_USER_TASK -> ANTI_HANG_TASK_ENTRY`.
- `EVERY_SUBSTANTIVE_TASK -> TRUE_MEMORY_TASK_MEMORY_GATE -> EXACT_CURRENT_SUPERVISOR`.
- `EVERY_SUBSTANTIVE_SUPERVISOR_CALL -> AT_LEAST_ONE_OWNED_CHILD_OR_HELPER`.
- applicable Critic/acceptance review is mandatory before substantive return.
- every MATERIAL return is followed by owner re-entry.
- every user-visible return passes completion integrity gating.
- TEMP_TASK lifecycle closes through True Memory + Inquisitor before completion.
- `FAILED_ROUTE != FAILED_CAPABILITY`; recovery continues through qualified reserves -> Generation -> External Connecting when required.
- safe-cycle boundaries never become user-visible checkpoints and never require `Go`.

No new actor, controller, watchdog, queue, workflow engine, StateHead, or cognitive topology is created.

### Generation-specific binding
A qualifying external failure MUST execute the recovery frontier: reconcile ambiguous effect -> inventory and try CURRENT qualified reserves -> inspect capability/plugin surfaces and applicable Vercel/Railway/Render/GitHub-backed or other Registry-qualified routes -> verify restored semantic operation. If no existing CURRENT route satisfies the semantics, External Connecting MUST be invoked. A single failed route/provider/plugin is never sufficient to report capability failure.

---

## Preserved predecessor body (subordinate where stricter override applies)

# Nameless Dhamma — Generation / External Integration Core

- component_key: GENERATION
- version: 15.1
- status: ADOPTION_READY / CURRENT_ONLY_WHEN_STATEHEAD_BOUND
- role: SUPPORT
- launcher: skills://plugins/nd-generation/nd-launch-generation
- launcher_contract: ND-LAUNCHER-CONTRACT-v6
- semantic_id: NOT_DECLARED

## Purpose

Generation is the bounded external-capability and route SUPPORT layer of Nameless Dhamma. It does not own the substantive task, does not become a cognitive Supervisor or Child, and does not resolve internal cognitive identities.

Its job is to preserve the live caller and obtain or recover the external capability needed to continue that caller's objective.

## Authoritative CURRENT resolution

All active callers reference Generation only through:

`skills://plugins/nd-generation/nd-launch-generation`

The launcher resolves CURRENT by:

`NAM-143 -> bound CURRENT ND_CAPABILITY_REGISTRY -> component_key GENERATION -> canonical_artifact_id + canonical_hash -> exact Drive artifact`.

No caller, Supervisor, Child, automation, resolver, operating profile, navigator, or projection may select Generation by numeric version, timestamp, filename, branch, checkpoint, remembered Drive ID, remembered hash, or copied prose.

NAM-142 is an operational/human navigator and projection surface. It can aid recovery but never overrides NAM-143 or its bound CURRENT Registry.

## Version-independence invariant

Numeric Generation versions are internal canonical-artifact and immutable-provenance metadata only.

ACTIVE runtime dependencies MUST be version-agnostic:
- depend on the exact launcher URI or logical component key `GENERATION`;
- never pin `Generation N`, a Generation artifact filename, Drive ID, hash, or predecessor version;
- never require a repository-wide manual rewrite when a successor Generation is adopted.

A successor Generation becomes CURRENT solely because authoritative NAM-143 binds a CURRENT Registry whose `GENERATION` component points to that exact canonical Drive artifact.

All predecessor Generation artifacts are immutable provenance and NONSELECTABLE.

## Caller and ownership preservation

Generation is JIT SUPPORT.

The substantive caller and its ancestors remain logically live. Generation occupies no Supervisor/Child slot and never changes domain ownership.

USER_DIRECT entry establishes Automation Agent as root before Generation support is used.

RETURN always goes to the same already-live substantive caller. Do not re-invoke a caller that remains live.

## Capability-first delegation

Generation resolves a logical external capability, not a historical transport implementation.

For each request:

1. Preserve the caller, task identity, correlation/effect identity, authority ceiling, cost policy, and operation semantics.
2. Identify the required logical external capability and semantic operation.
3. If the caller already has a valid CURRENT GPT-facing capability surface, use it.
4. Otherwise resolve the available CURRENT capability surface from the live plugin/tool catalog and current authority context.
5. Delegate the operation to that capability surface.
6. Let that capability surface own its internal provider routes, failover order, adapters, deployment details, and route-specific qualification state.
7. Verify consequential effects by authoritative provider readback when applicable.
8. Return the typed result to the original caller.

Generation MUST NOT duplicate a capability's internal route list merely to remember how the capability currently works.

Provider route orders, reserve chains, browser session state, deployments, quota, health and other volatile transport details belong to the owning capability surface or live provider evidence, not to Generation Core.

## Route failure and recovery

`FAILED_ROUTE != FAILED_CAPABILITY`.
`NO_CONNECTOR != NO_PROVIDER`.

On failure:
- preserve the same logical capability and operation;
- let the owning capability surface exhaust materially distinct authorized qualified routes according to its current contract;
- do not fan out consequential mutations;
- reconcile ambiguous outcomes before retry or failover;
- preserve idempotency/effect identity across route recovery;
- treat provider semantic errors separately from route/runtime failures;
- treat volatile health, quota, session, deployment and authentication state as VERIFY_AT_USE unless durable evidence establishes otherwise.

If no existing CURRENT capability surface can satisfy the request, invoke:
`skills://plugins/nd-external-connecting/connecting-external-capabilities`
for bounded creation/qualification of a missing or alternate route, then return to the interrupted substantive work.

If the problem is an unexplained live incident requiring diagnosis beyond route recovery, the substantive owner may invoke True Doctor as an authorized bounded PEER_SERVICE.

## Mutation safety

Consequential external effects are serialized.

Before a risky mutation, preserve enough effect identity and pre-call state to reconcile an ambiguous non-return.

After an ambiguous mutation:
1. classify the outcome as unknown;
2. perform authoritative provider/effect/job readback when possible;
3. recover the existing effect if it exists;
4. retry only after absence or retry-safety is established;
5. never create a duplicate logical effect merely because one route stopped returning.

Stop or local chat interruption is not provider cancellation.

Late external results are evidence only when the originating task/owner branch has been superseded; they cannot reacquire control.

## Anti-hang compatibility

Generation inherits the CURRENT cross-cutting ND anti-hang runtime through the StateHead-bound Registry.

External operations follow foreground lease, pre-call recoverability, durable-async control return, bounded result hydration, reconciliation-before-retry, FAILED_ROUTE != FAILED_CAPABILITY, and NO_IDENTICAL_STATE_LOOP semantics without introducing fixed token, call, route, pass, specialist, or wall-clock ceilings.

## Cost and authority

Never expand inherited authority.

Never start a paid plan, paid fallback, or paid provider spend unless the active caller/task explicitly permits it.

Provider credentials remain in protected provider/runtime secret stores. Generation must not copy raw secrets into Drive artifacts, GitHub, Linear, plugin prose, logs, checkpoints, or chat.

## Durable state boundary

True Memory owns durable currentness/persistence and authoritative publication.

Generation may produce authorized route/capability evidence and successor-state candidates, but it does not create a second currentness root.

NAM-143 plus its bound CURRENT Registry remain the sole global live capability/configuration authority.

GitHub/Obsidian resolvers, operating profiles, Linear text, checkpoints, audits and qualification reports are projections or provenance. They never repair, supersede, or override authoritative CURRENT.

## Compatible capability evolution

A route-level or provider-level change inside an already-authorized capability does NOT require a Generation successor when the change remains inside that capability's compatible contract.

Examples:
- reserve route repair or replacement;
- health/selectability change;
- compatible plugin release;
- deployment move;
- provider session/auth recovery;
- requalification of an existing operation.

A Generation successor is justified only when Generation Core semantics themselves materially change.

A Registry/StateHead successor remains required when global capability identity, semantic authority, incompatible contract, launcher binding family, or other StateHead-governed architecture materially changes.

## Projection rule

Active projections MUST NOT encode Generation numeric currentness.

Forbidden active-currentness patterns include:
- `Generation <number> is CURRENT`;
- `generation: <Generation version>` when used as authority coupling;
- `PROJECTION_ALIGNED_TO_GENERATION_<number>`;
- hard-coded predecessor Generation artifact IDs or hashes as runtime selectors.

Historical immutable checkpoints, receipts, audits and archives may retain exact old versions as provenance, but they must be structurally NONSELECTABLE and must never participate in CURRENT resolution.

## Qualification invariant

A Generation successor is not accepted until all of the following pass:
- exact Drive artifact readback and SHA-256 verification;
- Registry successor validation;
- NAM-143 publication under the qualified `SERIALIZED_SINGLE_WRITER` exact-old-anchor/token contract plus provider readback;
- cold recovery from launcher without supplying a Generation version;
- representative external capability delegation;
- failed-route recovery without capability downgrade;
- stale-reference scan showing no active runtime consumer pinned to a numeric Generation version;
- proof that historical provenance can still contain predecessor version numbers without becoming selectable.

## Post-T4 Linear StateHead convergence

The former Google Docs StateHead is protected NONSELECTABLE provenance only. Current publication follows the qualified True Memory contract: canonical Drive successor artifacts first, then one serialized exact-anchor/token update of NAM-143 with provider readback, then derived projections. This changes only currentness/publication routing; Generation remains SUPPORT and its launcher URI is unchanged.

## Replacement

Upon StateHead adoption of this artifact through the Registry GENERATION binding:
- this artifact becomes the sole CURRENT Generation behavioral authority;
- all predecessor Generation artifacts remain immutable provenance only;
- active callers continue using the unchanged launcher URI and require no version-specific update.
