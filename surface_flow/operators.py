from __future__ import annotations

import bpy
from bpy.types import Operator

from .build_nodes import build_surface_flow_group
from .constants import MIN_BLENDER_VERSION, MODIFIER_NAME


class SF_OT_build(Operator):
    bl_idname = "surface_flow.build"
    bl_label = "Build Surface Flow"
    bl_description = "Create/rebuild the Surface Flow Geometry Nodes setup on the active mesh"
    bl_options = {'REGISTER', 'UNDO'}

    force_rebuild: bpy.props.BoolProperty(default=True)

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

    def execute(self, context):
        if bpy.app.version < MIN_BLENDER_VERSION:
            self.report({'ERROR'}, f"Surface Flow requires Blender {MIN_BLENDER_VERSION[0]}.{MIN_BLENDER_VERSION[1]}+")
            return {'CANCELLED'}

        obj = context.active_object
        tree = build_surface_flow_group(force_rebuild=self.force_rebuild)

        modifier = obj.modifiers.get(MODIFIER_NAME)
        if modifier is None or modifier.type != 'NODES':
            modifier = obj.modifiers.new(name=MODIFIER_NAME, type='NODES')
        modifier.node_group = tree

        self.report({'INFO'}, "Surface Flow MVP created. Adjust inputs in the Geometry Nodes modifier.")
        return {'FINISHED'}


class SF_OT_rebuild(Operator):
    bl_idname = "surface_flow.rebuild"
    bl_label = "Rebuild Node Group"
    bl_description = "Rebuild SF_SurfaceFlow from the current implementation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        tree = build_surface_flow_group(force_rebuild=True)
        for obj in bpy.data.objects:
            for mod in obj.modifiers:
                if mod.type == 'NODES' and mod.name == MODIFIER_NAME:
                    mod.node_group = tree
        self.report({'INFO'}, "SF_SurfaceFlow rebuilt")
        return {'FINISHED'}
