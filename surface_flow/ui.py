import bpy
from bpy.types import Panel


class SF_PT_panel(Panel):
    bl_label = "Surface Flow"
    bl_idname = "SF_PT_surface_flow"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Surface Flow"

    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        if obj is None or obj.type != 'MESH':
            layout.label(text="Select a mesh object.", icon='INFO')
            return

        layout.operator("surface_flow.build", icon='NODETREE')
        layout.operator("surface_flow.rebuild", icon='FILE_REFRESH')
        layout.separator()
        layout.label(text="MVP: source → surface paths")
        layout.label(text="Tune parameters in the modifier.")
