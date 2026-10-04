# Stage 04 — Research / Analysis Stack

ROLE: TARGET BOOTSTRAP EXECUTOR  
TARGET STATE: NONAUTHORITATIVE

## Objective

Install and qualify the target-owned research stack against Ksyusha's already-created True Research semantic workspace.

## Required source bundles

- `plugin-export-current/nd-true-research.json`
- `plugin-export-current/nd-research-critic.json`
- `plugin-export-current/nd-pcpa.json`
- `plugin-export-current/nd-dae.json`
- `plugin-export-current/nd-pae.json`

## Execution

1. Recover Stages 01-03 from target readbacks and receipts.
2. Create/rebind any stable target Linear navigator required by the research stack before packaging launcher source. Populate only the corresponding allowed provider-literal replacements in the target binding map.
3. For each bundle, use `build_target_plugin.py <plugin-export-current/<plugin>.json> <target-binding-map.json> <output-dir>` and then recreate/install the target-owned plugin from the built output. Apply only verified target-provider substitutions. No source Linear/Drive/provider literal may remain runtime-selectable.
4. Preserve the exact Launcher Contract v6 relationships from `LAUNCHER_GRAPH_CURRENT.txt`:
   - True Research = Supervisor;
   - Research Critic = Child;
   - PCPA = Child;
   - Dhamma Analysis Engine = Child;
   - PAE = Child.
5. Do not invent one Linear issue per Child merely for symmetry; create only stable navigation source CURRENT actually defines.
6. Bind True Research to the target True Research semantic workspace created in Stage 03.
7. Perform a bounded bootstrap smoke qualification without publishing CURRENT:
   - invoke True Research;
   - invoke at least one appropriate owned Child/helper;
   - invoke Research Critic;
   - if Critic finds a material defect, repair and targeted recheck.
8. Verify exact skill URIs are callable and no source provider IDs are required at runtime. Spot-check target launcher bodies for target navigator resolution.
9. Record target plugin IDs/releases and any navigator/binding updates.

## Forbidden

- No source research project payload.
- No Nibbāna-conditions/GRC project activation.
- No StateHead publication.
- No bypass of Research Critic.

## Completion

Write `migration/receipts/STAGE_04_RESEARCH_RECEIPT.json` and update `TARGET_INSTALL_STATE.json`.

PASS requires all five research plugins installed/read back and one bounded Supervisor -> Child -> Critic chain working against target semantic memory.

Then stop this stage and instruct Ksyusha to run `05_WRITING_VISUAL_STACK.md`.
