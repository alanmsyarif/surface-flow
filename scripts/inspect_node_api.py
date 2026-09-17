"""Small Blender-side helper for reporting socket names after API changes."""
import bpy

NODE_TYPES = [
    "GeometryNodeRepeatInput",
    "GeometryNodeRepeatOutput",
    "GeometryNodeSampleNearestSurface",
    "GeometryNodeProximity",
    "GeometryNodePointsToCurves",
]

tree = bpy.data.node_groups.new("SF_API_INSPECT", "GeometryNodeTree")
for node_type in NODE_TYPES:
    try:
        n = tree.nodes.new(node_type)
        print("\n", node_type)
        print(" inputs :", [s.name for s in n.inputs])
        print(" outputs:", [s.name for s in n.outputs])
    except Exception as exc:
        print(node_type, "FAILED", exc)

bpy.data.node_groups.remove(tree)
