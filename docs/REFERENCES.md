# References

## Primary visual/technical inspiration

Alexey Stomakhin, Andrew Moffat, Gary Boyle. **A Practical Guide to Thin Film and Drips Simulation.** SIGGRAPH 2019 Talks. DOI: 10.1145/3306307.3328141.

The paper studies close-up water interaction with characters and discusses surface tension, viscosity, contact-angle adhesion, and moving collision geometry using a FLIP/APIC pipeline.

Surface Flow uses the paper as a *phenomena reference*, not as an implementation specification. The repository's current algorithm is procedural path integration over an existing mesh.

## Blender features used by the MVP

- Geometry Nodes Repeat Zone
- Geometry Proximity
- Sample Nearest Surface
- Distribute Points on Faces
- Points to Curves
- named attributes
