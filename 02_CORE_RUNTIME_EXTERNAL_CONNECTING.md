# Stage 02 — Core Runtime + External Connecting

ROLE: TARGET BOOTSTRAP EXECUTOR
TARGET STATE: NONAUTHORITATIVE

Install or guarded-update target-owned core plugins from `PLUGIN_EXPORT_CURRENT_MANIFEST.json`.
For CURRENT_SYNC_20261011 the material changed core surfaces are:
- Automation Agent canonical 1.3.5 / plugin source 1.7.5;
- Anti-Hang 1.7.0 / plugin source 1.2.1.

Preserve already-qualified unaffected Stage 02 objects. Prefer guarded update of the existing target plugin identity; create a successor only when platform constraints require it. After each write, read back exact target release/files and update target binding state.

Generation and External Connecting remain their existing CURRENT transfer versions and roles. External Connecting is recovery support, not a cognitive launcher.

Stage 02 PASS requires target Agent/Anti-Hang callable from target bootstrap bindings, exact changed-source readback, no source credentials, and no duplicate selectable predecessor.
