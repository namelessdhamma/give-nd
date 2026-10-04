# Stage 07 — Publish Ksyusha StateHead LAST

ROLE: TARGET AUTHORITY CUTOVER EXECUTOR  
TARGET STATE TRANSITION: BOOTSTRAP/NONAUTHORITATIVE -> CURRENT/AUTHORITATIVE

## Objective

Perform the single authority cutover only after the target clone is fully provisioned and prequalified.

## Preconditions

Stage 06 receipt = PASS.  
Target Registry has exact provider readback/hash.  
No unresolved material target mutation remains.

## Execution

1. Recover Stage 06 from target Drive + direct provider readback. Do not trust chat memory.
2. Re-run a compact precommit check:
   - exact target Registry readable;
   - exactly one intended target StateHead issue;
   - 22/22 launchers present;
   - External Connecting recovery skill present;
   - target NotebookLM semantic core ready;
   - no unresolved ambiguous write;
   - no pending architecture/provider object creation.
3. Before authority mutation, write any final precommit migration receipt/projection needed for resumability and set the install state to `PUBLICATION_PENDING`.
4. Prepare the final target Linear StateHead content:
   - CURRENT / AUTHORITATIVE;
   - sole target currentness root;
   - binds exactly one target CURRENT Registry;
   - target-owned provider IDs only;
   - source NAM-143 and source Registry identifiers are provenance, not target authority.
5. Publish/update the target Linear StateHead LAST.
6. Read back the Linear StateHead and verify exact target Registry binding and sole-authority semantics.
7. After this successful StateHead readback, perform NO further underlying architecture/provider mutation in this convergence transaction.

## Completion

Do not write another underlying provider checkpoint after the final StateHead commit. The verified StateHead itself is the completion anchor.

Return only:
- target StateHead identifier/URL;
- target Registry ID/hash;
- publication PASS/FAIL;
- exact blocker if any;
- instruction to open a NEW clean chat and run `08_COLD_QUALIFICATION.md`.

Do not run cold qualification in this chat.
