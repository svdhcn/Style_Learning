#----------------------------------------------------------
# File Delete Motions
#----------------------------------------------------------
import bpy
 

# Class Creat Basic Motions
class Delete_Basic_Motion(bpy.types.Panel):
	bl_label = "Delete Basic Motions"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOL_PROPS"

	@classmethod
	def poll(self,context):
		return context.object is not None
 
	def draw(self, context):
		layout = self.layout
		row = layout.row()
		row.alignment = 'LEFT'
		row.operator("wm.delete", text="Delete Motion")

#   Button
class DeleteMotion(bpy.types.Operator):
	bl_idname = "wm.delete"
	bl_label = "Delete Motion"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOL_PROPS"
	bl_category = "Tools"
	bl_context = "objectmode"
 
	def execute(self, context):
		bpy.ops.object.mode_set(mode='OBJECT')
		bpy.ops.object.delete(use_global=False)
		return{'FINISHED'}
 

#    Registration

def register():
	bpy.utils.register_class(DeleteMotion)
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(DeleteMotion)
	bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
	register()