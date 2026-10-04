# ND SEMANTIC CORE RUNTIME — v1.1.2

Status: ADOPTION_READY / CURRENT WHEN NAM-143-BOUND / CROSS-CUTTING RUNTIME POLICY
Role: shared semantic-working-context protocol for Nameless Dhamma cognitive units.
This is not a cognitive actor, not a StateHead, not a durable-memory authority, and not a substitute for canonical provider readback.

## Core topology

Authoritative currentness remains:

`NAM-143 -> bound CURRENT Capability Registry -> exact component/launcher binding`

Google Drive remains canonical durable artifact/memory storage.

Gemini Notebook LM is the routine semantic-working layer used to reduce repeated raw-context reconstruction and enable cross-source reasoning.

Primary semantic core notebook:
- notebook id: `cbb71f68-48e3-439b-acb0-b52a655481ba`
- title: `ND — Semantic Core — CURRENT — CLEAN`

NotebookLM is NONAUTHORITATIVE. It may orient, retrieve, compare, synthesize, critique, and hold bounded working context. It must never select CURRENT, authorize a consequential mutation, or overrule canonical Linear/Drive/GitHub/provider truth.

## Mandatory material-task behavior

For every material ND task where prior ND context, project state, corpus knowledge, architecture, canon, research history, writing continuity, implementation history, or incident history can materially affect the result:

1. Resolve CURRENT through NAM-143 and its bound Registry.
2. Identify the relevant semantic workspace:
   - always the global Semantic Core when system/global/currentness context matters;
   - an ACTIVE_PROJECT notebook when the task belongs to a continuing project;
   - a TEMP_TASK notebook only when a bounded multi-source workspace materially improves the task.
3. Ask NotebookLM a task-oriented semantic question before performing broad raw-source traversal. Request the smallest useful orientation packet: current objective/state, related components/projects, relevant sources, constraints, unresolved questions, and known conflicts.
4. Use NotebookLM actively during work when synthesis, cross-source comparison, contradiction discovery, continuity checking, or source-grounded questioning can reduce repeated GPT reconstruction.
5. Verify consequential/currentness/provider claims against their canonical source before mutation or publication.
6. Persist only justified durable deltas through the owning semantic unit / True Memory. Do not dump raw chat transcripts into semantic memory.
7. At completion, reconcile the notebook lifecycle:
   - CORE persists;
   - ACTIVE_PROJECT persists only while the project is active and materially useful;
   - TEMP_TASK is deleted after durable outputs are safely persisted and no continuation dependency remains;
   - completed project notebooks are deleted unless explicitly retained as useful nonauthoritative reference;
   - obsolete sources inside persistent notebooks are removed or neutralized so they cannot masquerade as CURRENT.
8. A route failure must not silently disable semantic-core use: `FAILED_ROUTE != FAILED_CAPABILITY`. Use another qualified Gemini Notebook LM route when appropriate. If NotebookLM itself is unavailable, fall back to canonical sources and continue in degraded semantic continuity mode.


## Long-lived project bootstrap — mandatory

When the user creates, adopts, or clearly begins a long-lived ND project whose state will matter across sessions, Automation Agent MUST bootstrap project memory before treating the project as normally operational. A manual Linear object alone is not sufficient.

Classification:
- Use ACTIVE_PROJECT when the work is expected to continue across sessions, accumulate canon/decisions/artifacts, or require cross-chat continuity.
- Use TEMP_TASK instead for bounded work that should disappear after durable convergence.
- Do not create persistent project machinery for trivial or one-shot tasks.

Mandatory NEW_PROJECT_BOOTSTRAP for ACTIVE_PROJECT:
1. Resolve CURRENT through NAM-143 -> bound CURRENT Registry and check whether the project already exists by stable project identity/name; never create a duplicate project root or duplicate notebook.
2. Create or identify one stable Linear Project Navigator issue for the project. A separate Linear Project container is OPTIONAL and is created only when a multi-issue backlog/roadmap materially helps execution.
3. Create or identify a canonical Google Drive project root plus a compact durable project-state/charter artifact sufficient for cross-chat recovery. Drive is durable storage, not currentness authority.
4. Create exactly one NotebookLM ACTIVE_PROJECT notebook while the project is active/useful.
5. Seed the notebook with the minimum useful curated corpus: project state/charter plus authoritative or clearly-labelled nonauthoritative sources. Do not dump raw chat transcripts.
6. Record the Drive pointers, ACTIVE_PROJECT notebook ID/title, current owner/frontier, and authority caveats in the Project Navigator.
7. Publish the project as one compact active-workstream entry in NAM-143 LAST, after provider readback of the Drive and NotebookLM effects.
8. Cold-qualify recovery: a fresh Automation Agent must be able to resolve NAM-143 -> project navigator -> ACTIVE_PROJECT notebook -> correct substantive Supervisor and recover the current objective/frontier without reconstructing chat history.
9. If NotebookLM is unavailable, keep Linear + Drive canonical state valid, mark semantic continuity DEGRADED_PENDING_BOOTSTRAP, use another qualified NotebookLM route when possible, and reconcile the ACTIVE_PROJECT workspace before claiming bootstrap completion. FAILED_ROUTE != FAILED_CAPABILITY.
10. At project completion, True Memory reconciles lifecycle: remove it from active NAM-143 workstreams; delete the ACTIVE_PROJECT notebook unless explicit continuing reference value justifies retention; preserve canonical Drive artifacts according to their own retention policy.

Google Workspace routing inside a project:
- Google Drive is the file/folder lifecycle and durable-artifact entrypoint: discovery, metadata, folders, raw files, moves/renames, canonical project-root organization and readback.
- Native Google Docs content work uses the current Docs-capable Drive route / Docs AI structural editing surface; Drive remains the durable container.
- Sheets and Slides use their current specialized Google Workspace routes when the artifact type requires them.
- Soluvery is inspection-only for Drive ACL/sharing/public-access audit and never becomes memory/currentness authority.
- NotebookLM is populated from curated project sources and used repeatedly for orientation, synthesis, continuity and contradiction discovery; it never replaces canonical provider verification.
- True Memory owns persistence/currentness/lifecycle coordination; domain Supervisors own domain truth and substantive decisions.

Bootstrap completion invariant:
NEW_PROJECT_BOOTSTRAP is complete only after Drive readback, NotebookLM source readiness, Project Navigator readback, NAM-143 final publication, and a cold recovery test. Provider success without these readbacks is not completion.

## Unit behavior

### Automation Agent
- For material ND work, perform semantic orientation before wide context reconstruction.
- Select relevant project/core notebook(s) and pass task-focused semantic findings to the substantive Supervisor.
- For a newly-created or newly-adopted long-lived project, execute NEW_PROJECT_BOOTSTRAP before normal multi-session work proceeds.
- Re-query the semantic workspace after material state changes, cross-domain handoffs, or before final integration when it can reveal conflicts or missing context.
- Do not turn NotebookLM into a second controller.

### True Memory
- Own semantic-corpus currentness, provenance discipline, notebook lifecycle, stale-source cleanup, project-memory bootstrap persistence, and promotion of durable deltas.
- Keep the Semantic Core compact, current, and useful.
- Maintain explicit NONSELECTABLE / NONAUTHORITATIVE labeling for retained historical material.
- Delete temporary notebooks after successful durable convergence and completion.
- Do not treat NotebookLM retrieval as authority.

### True Research
- Before broad external retrieval, ask the relevant semantic workspace what ND already knows, what sources/claims are already present, what uncertainties remain, and what would have highest information value.
- During research, use NotebookLM for cross-source synthesis, contradiction mapping, source-grounded questions, and continuity across research passes.
- For long-running research projects, maintain a project notebook with curated sources/results rather than forcing each GPT turn to reconstruct the corpus from raw files.
- Fresh external evidence still comes from qualified research tools; NotebookLM does not replace fresh retrieval.

### True Writer
- For continuing literary work, query the relevant project/book notebook for canon, prior chapters/scenes, character/voice constraints, unresolved setups/payoffs, accepted edits, and current reader-state goals.
- Use NotebookLM during revision to compare variants, check continuity, retrieve prior passages/decisions, and reason across long manuscripts.
- Temporary revision notebooks are deleted after accepted prose and durable state are persisted.
- Literary adjudication remains with True Writer.

### True Developer
- Query the core/project notebook for architecture intent, prior decisions, known failure modes, qualification history, unresolved defects, and operational constraints before broad code/history reconstruction.
- Use NotebookLM for cross-document engineering synthesis, not as source-code authority.
- Current code, deployments, runtime/provider state, and exact configs must be verified from their canonical systems.
- Temporary implementation/incident notebooks are deleted after durable engineering evidence is committed.

### True Doctor
- Use the semantic core/project notebook to recover prior incidents, known failure signatures, mitigations, and system topology.
- For complex incidents, a TEMP_TASK incident notebook may hold bounded logs/reports/diagnostic evidence.
- Delete the incident notebook after the incident is closed and the durable incident report/lessons are safely persisted.

### True Visual
- Query the relevant semantic workspace for current Visual Canon, product/story meaning, accepted representation decisions, and prior visual constraints before reconstruction from scattered files.
- Visual Canon and canonical visual artifacts remain authoritative outside NotebookLM.

### Supervisor -> Child recursive continuity
- A Supervisor receives the Agent's bounded semantic packet and remains responsible for domain-local semantic continuity while it is live.
- Before every MATERIAL Child call, pass the smallest decision-sufficient current packet needed by that Child; do not transfer authority.
- After a MATERIAL Child/Critic/peer RETURN, if accepted findings materially change domain state or can make the current packet stale, the Supervisor re-queries/rebinds the same relevant CORE / ACTIVE_PROJECT / TEMP_TASK workspace before choosing or briefing the next Child.
- The next call may be the same Child AGAIN. Semantic refresh and Child re-entry are independent decisions; neither requires ritual fan-out or ritual NotebookLM use.
- Children inherit the Supervisor's semantic context packet and may query the same relevant notebook when materially useful, but must not create a competing persistent notebook without Supervisor/True Memory lifecycle ownership.
- True Memory remains the only semantic-corpus currentness/lifecycle/persistence owner; Supervisors own domain truth and local orchestration.

## Notebook lifecycle classes

`CORE`
- long-lived semantic system workspace;
- compact, current, curated;
- never a StateHead.

`ACTIVE_PROJECT`
- long-running project/book/research/product workspace;
- persists while the project is active;
- curated and periodically compacted;
- bootstrap requires Linear navigator + Drive durable anchor + NotebookLM workspace + NAM-143 publication + cold recovery;
- deleted when the project ends unless retention has clear ongoing value.

`TEMP_TASK`
- bounded task/incident/revision/qualification workspace;
- created only when it reduces context reconstruction materially;
- must be deleted after task completion and durable convergence.

`LEGACY_PROVENANCE`
- retained only when historical comparison has continuing value;
- explicitly NONSELECTABLE/NONAUTHORITATIVE;
- may be deleted if it has no continuing value and no protected lineage requirement.

## Efficiency objective

The semantic layer exists specifically to reduce repeated GPT effort spent rediscovering ND context. The desired path is:

`Linear map -> Semantic Core / relevant project notebook -> focused canonical verification -> substantive work`

not:

`search every Drive/Linear/GitHub source from scratch on every turn`.

## Completion invariant

ND semantic-core adoption is complete only when observed production behavior shows Agent and major Supervisors actively use NotebookLM for material work, project notebooks follow lifecycle rules, temporary notebooks are deleted at completion, NEW_PROJECT_BOOTSTRAP is cold-qualified for a disposable long-lived project, and cold-start recovery can orient quickly from Linear + Semantic Core without broad manual context reconstruction.
