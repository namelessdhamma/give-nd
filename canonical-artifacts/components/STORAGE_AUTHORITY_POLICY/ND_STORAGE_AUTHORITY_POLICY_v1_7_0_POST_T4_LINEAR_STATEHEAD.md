# Nameless Dhamma — Storage Authority and Recovery Policy

**Policy ID:** `ND-PRECORE-STORAGE-1`  
**Version:** `1.7.0`  
**Status:** `ADOPTION_READY — POST-T4 LINEAR STATEHEAD / DRIVE DURABLE MEMORY / SERIALIZED SINGLE WRITER`  
**Date:** `2026-10-02`  
**Governing root:** `NAM-143 -> bound CURRENT Registry`  
**Supersedes:** `ND-PRECORE-STORAGE-1 v1.6.0`

## 1. Purpose

Maintain one recoverable authoritative Nameless Dhamma currentness root after the T4 migration while keeping Google Drive as canonical durable memory and preserving the immutable pre-T4 recovery lineage.

This policy changes currentness/publication routing only. It does not create a new cognitive owner, semantic owner, memory store, research truth authority, or second StateHead.

True Memory `skills://plugins/nd-true-memory/nd-launch-true-memory` remains the sole durable persistence/currentness executor for authorized deltas. Domain owners retain semantic truth/admission authority.

## 2. Current-authority chain

Current production identity is resolved only as:

```text
NAM-143 (authoritative Linear StateHead)
-> bound CURRENT ND_CAPABILITY_REGISTRY
-> exact component / launcher binding
-> exact canonical Drive artifact when the binding names one
```

The former Google Docs StateHead `18B01NY0Onztvs4fKXTfo5yqtMw7Ut081QpCEUSytNnE` is **NONSELECTABLE** after T4. It and its revision history remain protected provenance/recovery evidence only. It must never be inserted as an authority hop between `NAM-143` and the Registry.

Conversation history, filenames, timestamps, version labels, NotebookLM answers, GitHub/Obsidian projections, project checkpoints, and copied tables never override `NAM-143` plus its bound Registry.

## 3. Authority layers

### Linear

`NAM-143` is the sole mutable currentness StateHead and root navigator.

Its publication contract is:

`SERIALIZED_SINGLE_WRITER / TRUE_MEMORY / EXACT_OLD_ANCHOR_OR_TOKEN / PROVIDER_READBACK`

True Memory must:
1. fresh-read `NAM-143`;
2. verify head token/unique old-state anchor;
3. create and exact-read all required canonical Drive successors first;
4. perform one serialized conditional NAM-143 mutation;
5. exact-read `NAM-143` after the attempt;
6. on ambiguous transport outcome, reconcile provider truth before any retry;
7. on stale anchor/token, abort and re-resolve.

Provider-native Linear revision CAS is **not claimed** and is not required by this qualified T2/T4 contract.

### Google Drive

Google Drive is the canonical durable artifact/memory store.

Drive carries immutable component artifacts, Registry successors, evidence, reports, protected historical schemas/bundles, and other authorized durable records. Presence in Drive does not by itself make an artifact CURRENT; currentness is selected only by `NAM-143 -> bound Registry`.

### NotebookLM

NotebookLM is a disposable/non-authoritative semantic workspace over one corpus. `READY`, grounded chat, or a CURRENT-looking title does not confer currentness.

### GitHub / Obsidian / other projections

These are non-authoritative technical, recovery, source-control, or human-view surfaces. They may retain structurally nonselectable history.

## 4. Post-T4 publication model

For a material component/configuration currentness transition:

```text
authorized delta
-> create immutable/current canonical successor artifact(s) in Drive
-> exact provider readback + exact hash validation
-> create exact successor ND_CAPABILITY_REGISTRY in Drive
-> exact Registry readback + hash validation
-> fresh NAM-143 old-anchor/token verification
-> one serialized NAM-143 publication
-> exact NAM-143 readback
-> cold recovery through NAM-143
-> reconcile derived projections
```

The authority commit point is the successful `NAM-143` readback. Candidate Drive artifacts written before that commit are non-current candidates unless and until NAM-143 binds them.

A failed projection update creates SyncDebt and never rolls authority backward.

## 5. Pre-T4 durable-bundle lineage

`ND_DURABLE_STATE_SCHEMA_BUNDLE 1.7.0`, the immutable transaction-bundle chain, and the former Google Docs StateHead remain protected pre-T4 lineage/recovery evidence.

They are **not** a second post-T4 currentness root and are **not** used to fabricate a new Google-Docs StateHead publication after T4.

Schema 1.7.0 remains the canonical validator for the historical bundles created under that contract. Existing bundles, Registries, StateHeads, recovery manifests, and hashes remain byte-identical provenance.

A future need to resume schema-governed transactional bundles under the Linear StateHead requires a separately qualified schema extension that models the Linear publication contract. This migration does not silently reinterpret Schema 1.7.0 or forge a bundle that claims a Google Docs CAS which did not occur.

## 6. Canonical-byte and hash integrity

Raw JSON canonical component/Registry artifacts keep their declared exact-byte SHA-256 contracts. When a Registry binding declares `EXACT_FILE_BYTES` or `EXACT_UTF8_FILE_BYTES`, exact provider bytes must reproduce the recorded lowercase SHA-256.

Historical `DurableTransactionBundle` artifacts keep their original Unicode-NFC -> RFC 8785 JCS -> UTF-8 canonical-byte contract with no BOM or trailing bytes.

No predecessor artifact is rewritten to make a successor appear historically valid.

## 7. Parent-authorized writes

A successor cannot authorize its own adoption. The execution authority for a currentness transition is the fresh pre-write `NAM-143` state plus its currently bound Registry and the user's/governing authorization.

Architecture-only maintenance:
- changes only the exact authorized currentness/configuration scope;
- preserves unrelated component bindings byte-for-byte at the semantic level;
- preserves owner topology and permissions unless separately authorized;
- keeps immutable predecessor lineage available as provenance;
- does not infer DEEP_ERASURE authority from ordinary cleanup.

## 8. Ambiguity and concurrency

Consequential writes are serialized.

`OUTCOME_UNKNOWN` means read provider state before retry. A timeout, client Stop, 5xx, or missing local response does not prove provider failure. Exact committed state is acknowledged without replay.

A stale exact anchor/token fails closed. Parallel authority writers are prohibited.

## 9. Recovery

Cold recovery after T4:

1. read `NAM-143`;
2. require token `ND-LINEAR-STATEHEAD-CUTOVER-1` or a valid authorized successor token;
3. resolve the bound Registry by exact Drive ID/hash;
4. exact-read required component artifacts and launchers;
5. verify the former Google Docs StateHead remains nonselectable;
6. use canonical Drive records for durable content;
7. use NotebookLM only as an optional semantic accelerator;
8. if NotebookLM is unavailable, continue through direct canonical Drive/provider reads;
9. use pre-T4 immutable bundle lineage only as bounded recovery/provenance evidence, never as a competing currentness root.

A missing/mismatched bound Registry or material canonical artifact is fail-closed for affected consequential decisions.

## 10. Cleanup and rollback

`PUBLISHED_STATE_REFERENCED_ARTIFACT_IS_IMMUTABLE_PROVENANCE` remains normative for protected lineage.

Ordinary migration cleanup may:
- remove/neutralize obsolete mutable projections;
- remove old semantic sources after verified replacements;
- remove active routing aliases to superseded currentness;
- leave immutable historical literals when structurally NONSELECTABLE.

Ordinary cleanup does not authorize deep erasure of historical bundles, predecessor Registries, or recovery evidence.

Rollback means a new authorized successor publication from the then-CURRENT NAM-143 state; it does not mean making the former Google Docs StateHead selectable again.

## 11. Historical NAM-267 recovery boundary

The previously authorized recovery boundary `ND-NAM267-RECOVERY-BOUNDARY-35AF-20260927` remains valid only for the historical pre-T4 lineage for which it was approved.

Protected identifiers remain:
- recovery manifest: GitHub commit `8cefcc687509c7910fac0a1032a7f678aee98c9f`;
- governance decision Drive `1uLjHk6jjl5ENw3RyjR0DpGmvNnI2458m`, SHA-256 `f503ae7f69ef61366d5c70d292ce1f943870f884253d4f23a57e3ab89a3fe6f6`;
- admission ledger commit `5b4217054fcf16d0bf6350260c89293a2c1e528d`;
- validated recovery snapshot `ND-SNAPSHOT-FULL-INTEGRITY-35AF22A5A81D`, hash `e222d83dd781a9c5c9748f5246dcea2fc659f9eab05217e3fba21789f5dfc234`;
- checkpoint `ND-MAINT-CHECKPOINT-INTEGRITY-35AF22A5A81D`, hash `8980a29997b548454110b6287b01862f041cf8450f181e8b05eaf3afccb1616c`;
- carrier bundle `1Alieb-HS6uawYNpv3GvK7WXkrPiGFT-W`, SHA-256 `707a43c02f563c7e722de68e1d23194f069281d52d25ade0a38e2b5a2f10e783`.

This historical authorization is non-generalizable.

## 12. Migration convergence note

T4 moved the sole currentness root from the Google Docs StateHead to Linear `NAM-143`. This v1.7.0 policy is the minimal post-T4 convergence of the storage/currentness contract to that already-completed authority cutover.

No ownership topology changes. No second StateHead. No mandatory NotebookLM dependency. No GitHub-as-general-memory dependency.
