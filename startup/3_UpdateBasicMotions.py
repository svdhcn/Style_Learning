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
		items=[ ('ChayDan', "Chay Dan", ""),
				('HoaSenNo', "Hoa Sen No", ""),
				('LePhat', "Le Phat", ""),
				('QuaySoi', "Quay Soi", ""),
				('BatQuyet', "Bat Quyet", ""),
				('DangHoa', "Dang Hoa", ""),
				('Bay', "Bay", ""),
				('DungTay', "Dung Tay", ""),
				('DangLenCao', "Dang Len Cao", ""),
				('PhayTay', "Phay Tay", ""),
				('ChongSuon', "Chong Suon", ""),
				('DuaThoi', "Dua Thoi", ""),
				('VunGon', "Vun Gon", ""),
				('DangRuou', "Dang Ruou", ""),
				('Vay', "Vay", ""),
				('SoiBong', "Soi Bong", ""),
				('RotRuou', "Rot Ruou", ""),
				('CheoDo', "Cheo Do", ""),
				('RacDau', "Rac Dau", ""),
				('DayThuyen', "Day Thuyen", ""),
				('XeTo', "Xe To", ""),
				('CuopBong', "Cuop Bong", ""),
				('DeTho', "De Tho", ""),
				('PhuiTayAo', "Phui Tay Ao", ""),
				('LanTayAo', "Lan Tay Ao", ""),
				('GatLua', "Gat Lua", ""),
				('TauNhac', "Tau Nhac", ""),
				('VuotToc', "Vuot Toc", ""),
				('Ganh', "Ganh", ""),
				('XeTo', "Xe To", ""),
				('Nem', "Nem", ""),
				('ChanChuV', "Chan Hinh Chu V", ""),
				('ChanChi', "Chan Chu Chi", ""),
				('ChanTram', "Chan Qua Tram", ""),
				('ChanDinh', "Chan Chu Dinh", ""),
				('ChanDem', "Chan Dem Got", ""),
				('ChanChongQuy', "Chan Chong Chan Quy", ""),
				('HaiChanQuy', "Hai Dau Goi Cung Quy", ""),
				('NgoiMotBen', "Ngoi Hai Chan Co Ve Mot Ben", ""),
				('DuoiHaiChan', "Duoi Thang Hai Chan", ""),
				('ChanBatCheo', "Hai Chan Bat Cheo", ""),
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