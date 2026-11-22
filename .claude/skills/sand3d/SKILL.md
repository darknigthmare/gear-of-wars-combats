---
name: sand3d
description: Optional Sand3D Python procedural 3D modeling guidance for agents.
---

# Sand3D

Use this skill for approved procedural 3D tasks in the project's existing asset pipeline. This guide complements, and never replaces, project instructions and other agent skills.

Official project: https://github.com/Sandflow-ai/sand3d
Documentation for stable v1.6.3: https://github.com/Sandflow-ai/sand3d/blob/v1.6.3/docs/api.md
License: Apache-2.0.

When a task needs Sand3D, use an isolated Python 3.13 (or 3.11) environment, then install `sand3d==1.6.3` and verify `import sand3d`. Python 3.12 is not supported by the required Blender bpy wheels.

Read the official API before modeling. Build named shapes and parts with the documented methods, export only task-approved files, and inspect generated results. Do not add a runtime dependency or claim that a tool ran unless independently verified.
