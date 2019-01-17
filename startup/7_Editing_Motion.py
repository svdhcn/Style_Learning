bl_info = {
	"name": "Add-on Editing Motions",
	"description": "",
	"author": "Huan Vu Huu",
	"version": (0, 0, 1),
	"blender": (2, 79, 0),
	"location": "3D View > Tools",
	"warning": "", # used for warning icon and text in addons panel
	"wiki_url": "",
	"tracker_url": "",
	"category": "Development"
}

import bpy, IPython
#from SQL_Motions import add_new_base_pose, add_new_basic_movement, create_connection, select_basic_movement_by_base, select_all_basics
import os.path
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

import Setting
from HMI_Motions import EditMoverment, Get_Data_Rotation_BVH_File
from SQL_Motions import *
# ------------------------------------------------------------------------
#    store properties in the active scene
# ------------------------------------------------------------------------

class EditingSettings(PropertyGroup):

	path = StringProperty(
        name="Path",
        description="Path to Directory",
        default="/home/",
        maxlen=1024,
        subtype='FILE_PATH')

	Start_Frame = IntProperty(
		name = "Start Frame",
		description="A integer property",
		default = 1,
		min = 1
		)
	End_Frame = IntProperty(
		name = "End Frame",
		description="A integer property",
		default = 100,
		min = 1
		)

	Basic_Motions = EnumProperty(
		name="Basic Motions:",
		description="Apply Data to attribute.",
		items=[ ('ChanBatCheo', "Hai Chan Bat Cheo", ""),
				('DuoiHaiChan', "Hai Chan Duoi Thang", ""),
				('NgoiMotBen', "Ngoi Hai Chan Co Ve Mot Ben", ""),
				('HaiChanQuy', "Hai Dau Goi Cung Quy", ""),
				('ChanChongQuy', "Chan Chong Chan Quy", ""),
				('ChanDem', "Chan Dem Got", ""),
				('ChanDinh', "Chan Chu Dinh", ""),
				('ChanTram', "Chan Qua Tram", ""),
				('ChanChi', "Chan Chu Chi", ""),
				('ChanChuV', "Chan Hinh Chu V", ""),
				('Nem', "Tay Nem", ""),
				('XeTo5', "Tay Xe To The 5", ""),
				('Ganh', "Ganh", ""),
				('VuotToc', "Tay Vuot Toc", ""),
				('TauNhac', "Tau Nhac", ""),
				('GatLua', "Tay Gat Lua", ""),				
				('LanTayAo', "Lan Tay Ao", ""),
				('PhuiTayAo', "Phui Tay Ao", ""),
				('DeTho', "Tay De Tho", ""),
				('CuopBong', "Tay Cuop Bong", ""),
				('XeTo3', "Tay Xe To The 3", ""),
				('DayThuyen', "Tay Day Thuyen", ""),
				('RacDau', "Tay Rac Dau", ""),
				('CheoDo', "Tay Cheo Do", ""),
				('RotRuou', "Tay Rot Ruou", ""),
				('SoiBong', "Soi Bong", ""),
				('Vay', "Tay Vay", ""),
				('DangRuou', "Tay Dang Ruou", ""),
				('VunGon', "Tay Vun Gon", ""),
				('DuaThoi', "Tay Dua Thoi", ""),
				('ChongSuon', "Tay Chong Suon", ""),
				('PhayTay', "Phay Tay", ""),
				('DangLenCao', "Tay Dang Len Cao", ""),
				('RungTay', "Rung Tay", ""),
				('Bay', "Tay Bay", ""),
				('DangHoa', "Tay Dang Hoa", ""),
				('BatQuyet', "Tay Bat Quyet", ""),
				('QuaySoi', "Tay Quay Soi", ""),
				('LePhat', "Tay Le Phat", ""),
				('HoaSenNo', "Tay Hoa Sen No", ""),
				('ChayDan', "Tay Chay Dan", "")
			   ]
		)

# ------------------------------------------------------------------------
#    operators
# ------------------------------------------------------------------------

class EditingMotionOperator(bpy.types.Operator):
	bl_idname = "wm.editing_motions"
	bl_label = "Editing Motions"

	List_Bones_UpperBody = ['Chest', 'Chest2', 'Chest3', 'Chest4', 'Neck', 'Head', 'RightCollar', 'RightShoulder', 'RightElbow', 'RightWrist', 'LeftCollar', 'LeftShoulder', 'LeftElbow', 'LeftWrist']
	List_Bones_Lower_Body = ['RightHip', 'RightKnee', 'RightAnkle', 'RightToe', 'LeftHip', 'LeftKnee', 'LeftAnkle', 'LeftToe']

	def execute(self, context):
		scene = context.scene
		edittool = scene.editing_tool
		divide_body = 0
		database = Setting.path_database
		conn = create_connection(database)
		with conn:
			list_basic_motion = select_basic_movement_by_name(conn, edittool.Basic_Motions)
		path_basic_motion = list_basic_motion[0][4]
		name_basic_motion = list_basic_motion[0][3]
		if name_basic_motion in Setting.List_Motion_Upper:
			divide_body = 0
		elif name_basic_motion in Setting.List_Motion_Lower:
			divide_body = 1

		dataRotationMoverment = Get_Data_Rotation_BVH_File(path_basic_motion, divide_body, edittool.End_Frame - edittool.Start_Frame + 1)
		EditMoverment(dataRotationMoverment, divide_body, edittool.path, edittool.Start_Frame, edittool.End_Frame)
		bpy.ops.object.mode_set(mode='OBJECT')
		print("Basic Motion:", edittool.Basic_Motions,"path motions need to edit:", edittool.path, "Start_Frame:", edittool.Start_Frame, "End_Frame:",edittool.End_Frame)
		print ("Editing Moverment done.")
		return {'FINISHED'}
	
# ------------------------------------------------------------------------
#    my tool in objectmode
# ------------------------------------------------------------------------

class OBJECT_PT_Editing_panel(Panel):
	bl_idname = "OBJECT_PT_editing_panel"
	bl_label = "Editing Motion"
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
		editingtool = scene.editing_tool
		layout.label("Basic Motions")
		layout.prop(editingtool, "Basic_Motions", text="")
		layout.label("Motions need to edit")
		layout.prop(editingtool, "path", text="")
		layout.prop(editingtool, "Start_Frame")
		layout.prop(editingtool, "End_Frame")
		layout.operator("wm.editing_motions")

# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------

def register():
	bpy.utils.register_class(OBJECT_PT_Editing_panel)
	bpy.utils.register_module(__name__)
	bpy.types.Scene.editing_tool = PointerProperty(type=EditingSettings)

def unregister():
	bpy.utils.unregister_class(OBJECT_PT_Editing_panel)
	bpy.utils.unregister_module(__name__)
	del bpy.types.Scene.editing_tool

if __name__ == "__main__":
	register()