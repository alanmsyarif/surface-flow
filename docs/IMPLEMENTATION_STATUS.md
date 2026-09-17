# Implementation Status

## Implemented now

The generated Geometry Nodes graph covers the feasibility core:

- automatic gravity-relative source mask
- seed distribution
- per-seed path identity
- Repeat Zone integration
- nearest-surface normal sampling
- tangent-gravity direction
- deterministic tangent noise
- step advance
- closest-face re-projection
- trail point accumulation
- point-history to curve reconstruction
- preview tube mesh and material

## Runtime validation status

The Python source has been syntax-checked and the pure reference math tests pass in the generation environment.

A Blender executable is not available in that environment, so the Geometry Nodes builder has **not** been executed against a live Blender 5.2 process here. The repository includes:

- `scripts/smoke_test_blender.py` — live Blender validation
- `scripts/inspect_node_api.py` — socket/API inspection helper

Run the smoke test first. If Blender reports a changed socket name, use the inspection script and update the defensive socket aliases in `build_nodes.py`.

## Definition of done for v0.0.1

1. smoke test prints `SURFACE_FLOW_SMOKE_TEST_OK`
2. sphere paths remain attached for 48 steps
3. zero-randomness paths move consistently downhill
4. bottle shoulder does not cause widespread projection jumps
5. head test does not produce large cross-surface shortcuts

The last two are visual algorithm tests, not just API tests.
