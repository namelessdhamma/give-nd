# Stage 05 — Writing + Visual + SMM Stack

ROLE: TARGET BOOTSTRAP EXECUTOR  
TARGET STATE: NONAUTHORITATIVE

## Objective

Install and qualify the remaining user-facing cognitive launcher stack.

## Required source bundles

Writing:
- `nd-true-writer.json`
- `nd-technical-writer.json`
- `nd-books-creator.json`
- `nd-literary-critic.json`
- `nd-story-architect.json`

Visual:
- `nd-true-visual.json`
- `nd-visual-creator.json`

SMM:
- `nd-true-smm.json`

All paths are under `plugin-export-current/`.

## Execution

1. Recover the durable target checkpoint through Stage 04.
2. Create/rebind any stable target Linear navigators required by Writer, Visual and SMM before packaging launcher source. Extend the binding map with only allowed provider-literal replacements.
3. For each bundle, use `build_target_plugin.py <plugin-export-current/<plugin>.json> <target-binding-map.json> <output-dir>` and then recreate/install the target-owned plugin from the built output. Apply only verified target-provider substitutions. No source Linear/Drive/provider literal may remain runtime-selectable.
4. Preserve exact Launcher Contract v6 topology:
   - True Writer Supervisor -> Technical Writer / Books Creator / Literary Critic / Story Architect Children;
   - True Visual Supervisor -> Visual Creator Child;
   - True SMM launcher/status exactly as source CURRENT defines.
5. Preserve the source CURRENT SMM adoption state. A callable launcher does not authorize promotion beyond the source Registry/StateHead semantics.
6. Do not invent extra navigators; recreate/rebind only stable Linear navigation actually present in source CURRENT.
7. Run bounded bootstrap smoke qualification:
   - Writer -> appropriate Child -> Literary Critic;
   - True Visual -> Visual Creator -> acceptance/readback.
8. Do not create personal/product projects as test fixtures. Use disposable/system-safe fixtures only.
9. Verify exact target skill URIs, target plugin ownership, target navigator resolution, and absence of source-account runtime dependency.
10. Record target plugin IDs/releases and bindings.

## Completion

Write `migration/receipts/STAGE_05_WRITING_VISUAL_RECEIPT.json` and update `TARGET_INSTALL_STATE.json`.

PASS means the full 22-launcher topology plus the separate External Connecting recovery skill is now materially present in the target account, though target CURRENT is still unpublished.

Then stop this stage and instruct Ksyusha to run `06_REGISTRY_PREPUBLICATION.md`.
