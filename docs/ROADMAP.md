# Roadmap

## v0.0.1 — path feasibility — implemented

- source mask
- tangent gravity
- Repeat Zone integration
- nearest-surface attachment
- deterministic path history
- curve reconstruction

Exit test: sphere, bottle, and head should produce stable downward paths.

## v0.0.2 — convergence

- compute proximity to established trail network
- derive channel-attraction direction
- steer weak tips toward strong nearby channels
- avoid immediate self-attraction where possible

Exit test: independent streams visibly converge instead of staying parallel.

## v0.0.3 — explicit merging

- detect tip within merge radius
- steer to parent channel
- stop child tip once connected
- transfer `sf_weight`

## v0.0.4 — accumulation

- `sf_weight` transport
- wider channels after merges
- consistent, conservation-like visual rules

## v0.0.5 — wetness field

- distance-from-flow field on a surface proxy
- blur/spread
- export `sf_wetness`
- material-only wetness preview

## v0.0.6 — film

- thin offset coating from wetness
- channel/film transition
- Preview and Final resolution modes

## v0.0.7 — support + detachment

- predict future position
- measure nearby surface support
- adhesion-adjusted threshold
- switch unsupported tips to free-space integration

## v0.0.8 — reveal animation

- use `sf_age` with Scene Time
- reveal precomputed network without rebuilding the network each frame

## v0.1.0 — first complete system

- clean UX
- presets
- bottle/head hero demos
- benchmarks
