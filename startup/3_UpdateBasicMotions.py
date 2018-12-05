bl_info = {
	"name": "Add-on Template",
	"description": "",
	"author": "",
	"version": (0, 0, 1),
	"blender": (2, 70, 0),
	"location": "3D View > Tools",
	"warning": "", # used for warning icon and text in addons panel
	"wiki_url": "",
	"tracker_url": "",
	"category": "Development"
}

import bpy

from bpy.props import (StringProperty,
					   BoolProperty,
					   IntProperty,
					   FloatProperty,
					   EnumProperty,
					   PointerProperty,
					   )
from bpy.types import (Panel,
					   Operator,
					   PropertyGroup,
					   )


# ------------------------------------------------------------------------
#    store properties in the active scene
# ------------------------------------------------------------------------

class MySettings(PropertyGroup):

	Start_Frame = IntProperty(
		name = "Start Frame",
		description="A integer property",
		default = 0,
		min = 0
		)
	End_Frame = IntProperty(
		name = "End Frame",
		description="A integer property",
		default = 100,
		min = 1
		)

	my_enum = EnumProperty(
		name="Basic Motions:",
		description="Apply Data to attribute.",
		items=[ ('OP01', "Chay Dan", ""),
				('OP02', "Hoa Sen No", ""),
				('OP03', "Le Phat", ""),
				('OP04', "Quay Soi", ""),
				('OP05', "Bat Quyet", ""),
				('OP06', "Dang Hoa", ""),
				('OP07', "Bay", ""),
				('OP08', "Dung Tay", ""),
				('OP09', "Dang Len Cao", ""),
				('OP10', "Phay Tay", ""),
				('OP11', "Chong Suon", ""),
				('OP12', "Dua Thoi", ""),
				('OP13', "Vun Gon", ""),
				('OP14', "Dang Ruou", ""),
				('OP15', "Vay", ""),
				('OP16', "Soi Bong", ""),
				('OP17', "Rot Ruou", ""),
				('OP18', "Cheo Do", ""),
				('OP19', "Rac Dau", ""),
				('OP20', "Day Thuyen", ""),
				('OP21', "Xe To", ""),
				('OP22', "Cuop Bong", ""),
				('OP23', "De Tho", ""),
				('OP24', "Phui Tay Ao", ""),
				('OP25', "Lan Tay Ao", ""),
				('OP26', "Gat Lua", ""),
				('OP27', "Tau Nhac", ""),
				('OP28', "Vuot Toc", ""),
				('OP29', "Ganh", ""),
				('OP30', "Xe To", ""),
				('OP31', "Nem", ""),
				('OP32', "Chan Hinh Chu V", ""),
				('OP33', "Chan Chu Chi", ""),
				('OP34', "Chan Qua Tram", ""),
				('OP35', "Chan Chu Dinh", ""),
				('OP36', "Chan Dem Got", ""),
				('OP37', "Chan Chong Chan Quy", ""),
				('OP38', "Hai Dau Goi Cung Quy", ""),
				('OP39', "Ngoi Hai Chan Co Ve Mot Ben", ""),
				('OP40', "Duoi Thang Hai Chan", ""),
				('OP41', "Hai Chan Bat Cheo", ""),
			   ]
		)

# ------------------------------------------------------------------------
#    operators
# ------------------------------------------------------------------------

class UpdateMotionOperator(bpy.types.Operator):
	bl_idname = "wm.update_motions"
	bl_label = "Update Basic Motions"

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		# print the values to the console
		print("Hello World")
		#print("bool state:", mytool.my_bool)
		print("int value:", mytool.Start_Frame)
		print("int value:", mytool.End_Frame)
		#print("float value:", mytool.my_float)
		#print("string value:", mytool.my_string)
		print("enum state:", mytool.my_enum)

		return {'FINISHED'}

# ------------------------------------------------------------------------
#    my tool in objectmode
# ------------------------------------------------------------------------

class OBJECT_PT_my_panel(Panel):
	bl_idname = "OBJECT_PT_my_panel"
	bl_label = "Update Basic Motions"
	bl_space_type = "VIEW_3D"   
	bl_region_type = "TOOL_PROPS"    
	bl_category = "Tools"
	bl_context = "objectmode"   

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		mytool = scene.my_tool

		layout.prop(mytool, "my_enum", text="") 
		layout.prop(mytool, "Start_Frame")
		layout.prop(mytool, "End_Frame")
		layout.operator("wm.update_motions")

# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------

def register():
	bpy.utils.register_module(__name__)
	bpy.types.Scene.my_tool = PointerProperty(type=MySettings)

def unregister():
	bpy.utils.unregister_module(__name__)
	del bpy.types.Scene.my_tool

if __name__ == "__main__":
	register()