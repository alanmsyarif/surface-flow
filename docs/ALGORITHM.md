# MVP Algorithm

## 1. Automatic source

Normalize the surface's position along `Up = -normalize(Gravity)`.

```text
h(p) = dot(p, Up)
height01 = remap(h, min(h), max(h), 0, 1)
```

A smooth threshold around `Source Start` creates the initial source/coating region.

## 2. Seed points

`Distribute Points on Faces` uses:

```text
density = Seed Density * source_mask
```

Each seed stores a stable `sf_id` and starts at `sf_age = 0`.

## 3. Tangent gravity

For current surface normal `N` and normalized gravity `G`:

```text
G_t = G - dot(G, N) * N
D = normalize(G_t)
```

On a horizontal top where gravity is parallel to the normal, `G_t` approaches zero. Randomness can break the symmetry, but v0.0.1 does not yet have curvature-aware fallback logic.

## 4. Stable perturbation

A deterministic random vector is generated from path ID, user seed, and Repeat Zone iteration. Its normal component is removed before blending with the tangent-gravity direction.

```text
R_t = R - dot(R, N) * N
D = normalize(D + randomness * R_t)
```

## 5. Integration

```text
candidate = p + D * StepLength
```

The candidate is moved to the closest location on the target surface.

## 6. Trail recording

The projected tip receives:

```text
sf_age = iteration + 1
```

and is joined to the previous trail point cloud.

## 7. Curve reconstruction

At the end:

```text
Points to Curves
Curve Group ID = sf_id
Weight         = sf_age
```

The resulting curves are offset slightly along `sf_normal`, given a radius, and converted to preview tubes.
