bl_info = {
	"name": "Add-on Clustering Basic Motions",
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

class ClusterSettings(PropertyGroup):

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

class ClusterMotionOperator(bpy.types.Operator):
	bl_idname = "wm.cluster_motions"
	bl_label = "Clustering Basic Motions"

	List_Bones_UpperBody = ['Chest', 'Chest2', 'Chest3', 'Chest4', 'Neck', 'Head', 'RightCollar', 'RightShoulder', 'RightElbow', 'RightWrist', 'LeftCollar', 'LeftShoulder', 'LeftElbow', 'LeftWrist']
	List_Bones_Lower_Body = ['RightHip', 'RightKnee', 'RightAnkle', 'RightToe', 'LeftHip', 'LeftKnee', 'LeftAnkle', 'LeftToe']

	def execute(self, context):
		scene = context.scene
		clustertool = scene.cluster_tool
		file_path = clustertool.path
	
		return {'FINISHED'}

# ------------------------------------------------------------------------
#    my tool in objectmode
# ------------------------------------------------------------------------

class OBJECT_PT_cluster_panel(Panel):
	bl_idname = "OBJECT_PT_cluster_panel"
	bl_label = "Cluster Basic Motions"
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
		clustertool = scene.cluster_tool
		layout.prop(clustertool, "Basic_Motions", text="")
		layout.prop(clustertool, "path", text="")
		layout.operator("wm.cluster_motions")

# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------

def register():
	bpy.utils.register_module(__name__)
	bpy.types.Scene.cluster_tool = PointerProperty(type=ClusterSettings)

def unregister():
	bpy.utils.unregister_module(__name__)
	del bpy.types.Scene.cluster_tool

if __name__ == "__main__":
	register()