# Testing

## Pure Python

```bash
python -m pytest
```

This validates reference math only; it does not validate Blender nodes.

## Blender smoke test

Run with Blender 5.2+:

```bash
blender --background --factory-startup --python scripts/smoke_test_blender.py
```

The test creates a UV sphere, builds the node graph, forces depsgraph evaluation, saves `surface_flow_smoke_test.blend`, and prints:

```text
SURFACE_FLOW_SMOKE_TEST_OK ...
```

## Visual regression meshes

Always test algorithm changes on:

1. sphere — baseline curvature
2. bottle — shoulder and rim
3. head — convex/concave complexity
4. concave shape — nearest-surface ambiguity
5. sharp edge — future support/detachment behavior

## Debug order

When paths look wrong:

1. set Randomness to 0
2. reduce Seed Density
3. reduce Steps
4. visualize source mask
5. inspect tangent gravity
6. inspect projected positions
7. only then re-enable noise
