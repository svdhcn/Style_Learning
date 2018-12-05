#----------------------------------------------------------
# File layout.py
#----------------------------------------------------------
import bpy
 

# Class Creat Basic Motions
class BvhFileManagement(bpy.types.Panel):
	bl_label = "Import Export BVH file"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOL_PROPS"

	@classmethod
	def poll(self,context):
		return context.object is not None
 
	def draw(self, context):
		layout = self.layout		
		# Creat Basic motions
		row = layout.row()
		row.alignment = 'LEFT'
		row.operator("my.button", text="Import BVH file", icon = 'IMPORT').number=1
		row.operator("my.button", text="Export BVH file", icon = 'EXPORT').number=2


#   Button
class OBJECT_OT_Button(bpy.types.Operator):
	bl_idname = "my.button"
	bl_label = "Button"
	number = bpy.props.IntProperty()
	row = bpy.props.IntProperty()
	loc = bpy.props.StringProperty()
 
	def execute(self, context):
		if self.loc:
			words = self.loc.split()
			self.row = int(words[0])
			self.number = int(words[1])
		print("Row %d button %d" % (self.row, self.number))
		return{'FINISHED'}    
 
#    Registration
bpy.utils.register_module(__name__)

def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
	register()