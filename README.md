# Surface Flow

Experimental procedural surface drainage for **Blender 5.2 LTS Geometry Nodes**.

> Mesh in → coating source → surface-following paths out.

This repository implements the first feasibility slice of the Surface Flow project. It is **not a fluid solver**. The current MVP generates deterministic flow paths that start near the highest part of a mesh relative to gravity, move along tangent gravity, re-project to the closest surface, and rebuild the recorded point history as curves.

## What is implemented in v0.0.1

- automatic source region derived from mesh height along gravity
- seed distribution on the source region
- tangent-gravity flow direction
- stable random directional perturbation
- Repeat Zone iterative propagation
- Geometry Proximity surface re-attachment
- per-path `sf_id`, `sf_age`, and `sf_normal` attributes
- Points to Curves reconstruction
- preview tube geometry + material
- a small sidebar panel that builds/rebuilds the node group
- Blender background smoke-test script
- pure-Python reference math tests

## Not implemented yet

- channel attraction / convergence
- explicit path merging
- flow-weight accumulation
- continuous wetness field
- film/sheet geometry
- support estimation and detachment
- age-based animation reveal
- moving/deforming surfaces

Those are intentionally deferred until path propagation is reliable.

## Install for development

1. Open Blender 5.2 LTS.
2. Open the **Scripting** workspace.
3. Open `scripts/install_dev.py` from this repository and run it.
4. Select a mesh.
5. Open **3D View → Sidebar → Surface Flow**.
6. Click **Build Surface Flow**.
7. Tune values in the Geometry Nodes modifier.

## Install as a Blender extension

An installable package can be built from `extension/` with:

```bash
blender --command extension build --source-dir extension
```

Or use the prebuilt `surface_flow-0.0.1.zip` included with the generated project package.

## First test settings

For a unit sphere of radius 1 m:

```text
Gravity          (0, 0, -1)
Source Start      0.72
Source Softness   0.08
Seed Density      35
Steps             48
Step Length       0.025
Randomness        0.10
Flow Radius       0.006
Surface Offset    0.002
```

Start with `Randomness = 0` when debugging propagation.

## MVP algorithm

```text
INPUT MESH
   ↓
height along -gravity
   ↓
automatic source mask
   ↓
distribute seed points
   ↓
Repeat Zone
   ├─ sample nearest surface normal
   ├─ project gravity to tangent plane
   ├─ add deterministic tangent noise
   ├─ advance one step
   ├─ project to nearest surface
   └─ append tip to trail history
   ↓
Points to Curves (group = sf_id, weight = sf_age)
   ↓
preview tubes
```

Tangent gravity is:

```text
G_t = normalize(G - dot(G, N) * N)
```

## Reference scope

The visual inspiration is Stomakhin, Moffat, and Boyle, *A Practical Guide to Thin Film and Drips Simulation* (SIGGRAPH 2019). Their production method uses FLIP/APIC, surface tension, viscosity, contact-angle handling, and moving-boundary treatment. Surface Flow deliberately does **not** reproduce that solver; it explores a much lighter procedural approximation for attached coating/drainage patterns.

## Current technical risk

The node graph is generated through Blender's Python API and targets Blender 5.2. The repository includes `scripts/inspect_node_api.py` because socket names can change between Blender versions. Run the smoke test before treating a build as release-ready.

## License

MIT.
