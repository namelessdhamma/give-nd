# Stage 02 — Core Runtime + External Connecting

ROLE: TARGET BOOTSTRAP EXECUTOR  
TARGET STATE: NONAUTHORITATIVE  
NOTEBOOKLM: MUST NOT BE REQUIRED YET

## Objective

Install the minimum target-owned ND control/recovery runtime needed before semantic memory is connected.

## Required source bundles

Rebuild target-owned private plugins from these exact functional bundles:

- `plugin-export-current/nd-anti-hang.json`
- `plugin-export-current/nd-true-memory.json`
- `plugin-export-current/nd-inquisitor.json`
- `plugin-export-current/nd-true-developer.json`
- `plugin-export-current/nd-developer-critic.json`
- `plugin-export-current/nd-true-doctor.json`
- `plugin-export-current/nd-generation.json`
- `plugin-export-current/nd-external-connecting.json`
- `plugin-export-current/nd-automation-agent.json`

Source Plugin Creator IDs/releases are provenance only. Ksyusha's plugins must be owned by Ksyusha's account.

## Execution

1. Recover Stage 01 from target Drive `TARGET_INSTALL_STATE.json` + provider readbacks. If Stage 01 is already PASS, do not recreate its objects.
2. Verify target Plugin Creator authorization.
3. Before building plugins, create/rebind the target Linear operational navigators required by this core set, using source CURRENT semantics and target-owned IDs. Stage 01 already created the target BOOTSTRAP StateHead. Create the target equivalents for Agent, Anti-Hang, True Memory, Inquisitor, True Developer, True Doctor and the Generation / external-integration navigation surfaces as defined by source CURRENT. Do not invent extra navigators.
4. Populate the working binding map's `literal_replacements` with exact source-provider literal -> target-provider literal substitutions needed by these plugin sources (for example source Linear StateHead/KERNEL URLs -> Ksyusha target navigator URLs). Only substitutions allowed by `ALLOWED_DIFFERENCES.json` are permitted.
5. Build target plugin packages with `build_target_plugin.py <plugin-export-current/<plugin>.json> <target-binding-map.json> <output-dir>`. The builder is qualified by `BUILD_TARGET_PLUGIN_TEST_RECEIPT.json`. It applies ONLY verified plugin-local target-provider substitutions, permits unrelated future-stage placeholders, fails closed on any binding actually required by the current plugin, preserves the `skills://` identity set, and rejects remaining source Linear executable URLs. Do not byte-copy source-account Linear/Drive/provider IDs into target runtime launchers. Generated binary caches such as `__pycache__/*.pyc` are not required.
6. Preserve exact stable skill identities and relationships:
   - Automation Agent ROOT;
   - Anti-Hang cross-cutting runtime;
   - True Memory Supervisor;
   - Inquisitor Child of True Memory;
   - True Developer Supervisor;
   - Developer Executor inside the True Developer plugin;
   - Developer Critic Child;
   - True Doctor Supervisor;
   - Generation SUPPORT;
   - External Connecting RECOVERY_SKILL.
7. Use `LAUNCHER_GRAPH_CURRENT.txt` and the Registry recovery-skill binding. Do not invent alternate names or flatten roles. If the platform makes an exact `skills://` identity impossible, fail closed unless an allowed namespace remap is explicitly proven semantically equivalent.
8. Verify callable target surfaces for:
   - `@ND Automation Agent`
   - `@ND Anti-Hang`
   - `@ND True Memory`
   - `@ND Inquisitor`
   - `@ND True Developer`
   - Developer Executor launcher
   - `@ND Developer Critic`
   - `@ND True Doctor`
   - `@ND Generation`
   - `@ND External Connecting`
9. Record target plugin IDs/releases, navigator IDs and applied provider-literal replacements into the target binding working copy.
10. Provider-read back all installed releases and exact skill paths. Spot-check launcher bodies to prove they resolve Ksyusha's target StateHead/navigators rather than Savva's source Linear objects.

## Important bootstrap boundary

Even if `@ND Automation Agent` is now visible, the target StateHead is still BOOTSTRAP/NONAUTHORITATIVE. Do not claim target CURRENT and do not force production True Memory TEMP_TASK rules before Stage 03 has connected NotebookLM. These stages are bootstrap construction, not normal target production execution.

## Completion

Write `migration/receipts/STAGE_02_CORE_RUNTIME_RECEIPT.json` and update `TARGET_INSTALL_STATE.json`.

PASS requires exact core/runtime plugin readbacks plus an OPERATION_QUALIFIED External Connecting skill.

Then stop this stage and instruct Ksyusha to run `03_NOTEBOOKLM_SEMANTIC_MEMORY.md`.
