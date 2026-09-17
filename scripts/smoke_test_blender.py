"""Run with Blender 5.2+:

blender --background --factory-startup --python scripts/smoke_test_blender.py
"""
import os
import sys

import bpy

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from surface_flow.build_nodes import build_surface_flow_group
from surface_flow.constants import MODIFIER_NAME, NODE_GROUP_NAME

# reset
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, radius=1.0)
obj = bpy.context.active_object
obj.name = "SF_TestSphere"

tree = build_surface_flow_group(force_rebuild=True)
assert tree.name == NODE_GROUP_NAME

mod = obj.modifiers.new(MODIFIER_NAME, 'NODES')
mod.node_group = tree

# Force depsgraph evaluation. This catches a large class of invalid-node links.
depsgraph = bpy.context.evaluated_depsgraph_get()
eval_obj = obj.evaluated_get(depsgraph)
mesh = eval_obj.to_mesh()
assert mesh is not None
print("SURFACE_FLOW_SMOKE_TEST_OK", len(mesh.vertices), len(mesh.edges), len(mesh.polygons))
eval_obj.to_mesh_clear()

out = os.path.join(ROOT, "surface_flow_smoke_test.blend")
bpy.ops.wm.save_as_mainfile(filepath=out)
print("Saved", out)
