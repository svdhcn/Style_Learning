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
				('TuTheNgoi4', "Duoi Thang Hai Chan", ""),
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
				('DuoiHaiChan', "Duoi Thang Hai Chan", ""),
				('NgoiMotBen', "Ngoi Hai Chan Co Ve Mot Ben", ""),
				('HaiChanQuy', "Hai Dau Goi Cung Quy", ""),
				('ChanChongQuy', "Chan Chong Chan Quy", ""),
				('ChanDem', "Chan Dem Got", ""),
				('ChanDinh', "Chan Chu Dinh", ""),
				('ChanTram', "Chan Qua Tram", ""),
				('ChanChi', "Chan Chu Chi", ""),
				('ChanChuV', "Chan Hinh Chu V", ""),
				('Nem', "Nem", ""),
				('XeTo', "Xe To", ""),
				('Ganh', "Ganh", ""),
				('VuotToc', "Vuot Toc", ""),
				('GatLua', "Gat Lua", ""),
				('LanTayAo', "Lan Tay Ao", ""),
				('PhuiTayAo', "Phui Tay Ao", ""),
				('DeTho', "De Tho", ""),
				('CuopBong', "Cuop Bong", ""),
				('XeTo', "Xe To", ""),
				('DayThuyen', "Day Thuyen", ""),
				('RacDau', "Rac Dau", ""),
				('CheoDo', "Cheo Do", ""),
				('RotRuou', "Rot Ruou", ""),
				('SoiBong', "Soi Bong", ""),
				('Vay', "Vay", ""),
				('DangRuou', "Dang Ruou", ""),
				('VunGon', "Vun Gon", ""),
				('DuaThoi', "Dua Thoi", ""),
				('ChongSuon', "Chong Suon", ""),
				('PhayTay', "Phay Tay", ""),
				('DangLenCao', "Dang Len Cao", ""),
				('DungTay', "Dung Tay", ""),
				('Bay', "Bay", ""),
				('DangHoa', "Dang Hoa", ""),
				('BatQuyet', "Bat Quyet", ""),
				('QuaySoi', "Quay Soi", ""),
				('LePhat', "Le Phat", ""),
				('HoaSenNo', "Hoa Sen No", ""),
				('ChayDan', "Chay Dan", "")
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
		bpy.ops.export_anim.bvh(filepath= file_path, global_scale = 1, frame_start= mytool.Start_Frame, frame_end= mytool.End_Frame)
		'''
		database = "/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/dance.db"
		conn = create_connection(database)
		with conn:
			new_base_pose = (mytool.Posture_Basics, mytool.path)
			base_pose_id = add_new_base_pose(conn, new_base_pose)
			print(base_pose_id)
			print("1. Query basic movement by base id:")
			select_basic_movement_by_base(conn,1)
			
			new_basic_movement = (base_pose_id,mytool.Basic_Motions, mytool.path)
			basic_movement_id = add_new_basic_movement(conn, new_basic_movement)
			print(basic_movement_id)
			
			print("2. Query all basic movements")
			select_all_basics(conn)
			new_base_pose = (mytool.Basic_Motions, mytool.path)

		'''
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
		layout.label("Posture Basics")
		layout.prop(mytool, "Posture_Basics", text="")
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