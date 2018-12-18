bl_info = {
	"name": "Add-on Update Basic Motions",
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

import bpy
from SQL_Motions import add_new_base_pose, add_new_basic_movement, create_connection, select_basic_movement_by_base, select_all_basics
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

	Posture_Basics = EnumProperty(
		name = "Posture Basics:",
		description = "Apply Data to attribute.",
		items=[ ('TuTheNgoi5', "Hai Chan Bat Cheo", ""),
				('TuTheNgoi4', "Hai Chan Duoi Thang", ""),
				('TuTheNgoi3', "Hai Chan Co Ve Mot Ben", ""),
				('TuTheNgoi2', "Hai Dau Goi Cung Quy", ""),
				('TuTheNgoi1', "Chan Chong Chan Quy", ""),
				('TuTheChan5', "Dem Got", ""),
				('TuTheChan4', "Chan Chu Dinh", ""),
				('TuTheChan3', "Chan Qua Tram", ""),
				('TuTheChan2', "Chan Chu Chi", ""),
				('TuTheChan1', "Chan Chu V", ""),
				('TuTheTay5', "Tau Nhac", ""),
				('TuTheTay4', "Cuop Bong", ""),
				('TuTheTay3', "Dang Ruou", ""),
				('TuTheTay2', "Dang Hoa", ""),
				('TuTheTay1', "Chay Dan", "")
			   ]
		)

	path = StringProperty(
        name="Path",
        description="Path to Directory",
        default="/home/",
        maxlen=1024,
        subtype='FILE_PATH')

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

class UpdateMotionOperator(bpy.types.Operator):
	bl_idname = "wm.update_motions"
	bl_label = "Create Basic Motions"

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool
		file_path = mytool.path

		bpy.context.scene.render.fps = 60
		if os.path.exists(file_path):
			os.remove(file_path)
		bpy.ops.export_anim.bvh(filepath= file_path, global_scale = 1, frame_start= mytool.Start_Frame, frame_end= mytool.End_Frame, rotate_mode='NATIVE', root_transform_only = True)

		Id_Posture = ""
		if mytool.Basic_Motions in ["ChayDan", "HoaSenNo", "LePhat", "QuaySoi", "BatQuyet"]:
			Id_Posture = "T_CHAYDAN"
		elif mytool.Basic_Motions in ["DangHoa", "Bay", "RungTay", "DangLenCao", "PhayTay", "ChongSuon", "DuaThoi", "VunGon"]:
			Id_Posture = "T_DANGHOA"
		elif mytool.Basic_Motions in ["DangRuou", "Vay", "SoiBong", "RotRuou", "CheoDo", "RacDau", "DayThuyen", "XeTo3"]:
			Id_Posture = "T_DANGRUOU"
		elif mytool.Basic_Motions in ["CuopBong", "DeTho", "PhuiTayAo", "LanTayAo", "GatLua"]:
			Id_Posture = "T_CUOPBONG"
		elif mytool.Basic_Motions in ["VuotToc", "Ganh", "XeTo5", "Nem"]:
			Id_Posture = "T_TAUNHAC"
		elif mytool.Basic_Motions in ["ChanChuV"]:
			Id_Posture = "C_CHUV"
		elif mytool.Basic_Motions in ["ChanChi"]:
			Id_Posture = "C_CHUCHI"
		elif mytool.Basic_Motions in ["ChanTram "]:
			Id_Posture = "C_QUATRAM"
		elif mytool.Basic_Motions in ["ChanDinh"]:
			Id_Posture = "C_CHUDINH"
		elif mytool.Basic_Motions in ["ChanDem"]:
			Id_Posture = "C_DEMGOT"
		elif mytool.Basic_Motions in ["ChanChongQuy"]:
			Id_Posture = "C_CHONGQUY"
		elif mytool.Basic_Motions in ["HaiChanQuy"]:
			Id_Posture = "C_QUY"
		elif mytool.Basic_Motions in ["NgoiMotBen"]:
			Id_Posture = "C_COMOTBEN"
		elif mytool.Basic_Motions in ["DuoiHaiChan"]:
			Id_Posture = "C_DUOITHANG"
		elif mytool.Basic_Motions in ["ChanBatCheo"]:
			Id_Posture = "C_BATCHEO"

		database = "/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/HumanStyle.db"
		conn = create_connection(database)
		with conn:
			#new_base_pose = (mytool.Posture_Basics, mytool.path)
			#base_pose_id = add_new_base_pose(conn, new_base_pose)
			#print(base_pose_id)
			#print("1. Query basic movement by base id:")
			#select_basic_movement_by_base(conn,1)
			
			new_basic_movement = (Id_Posture,mytool.Basic_Motions, mytool.path)
			basic_movement_id = add_new_basic_movement(conn, new_basic_movement)
			print(basic_movement_id)
			
			#print("2. Query all basic movements")
			#select_all_basics(conn)
			#new_base_pose = (mytool.Basic_Motions, mytool.path)

		
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
		#layout.label("Posture Basics")
		#layout.prop(mytool, "Posture_Basics", text="")
		layout.label("Basic Motions")
		layout.prop(mytool, "Basic_Motions", text="")
		layout.label("Path")
		layout.prop(mytool, "path", text="")
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