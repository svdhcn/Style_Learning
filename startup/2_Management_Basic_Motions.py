bl_info = {
	"name": "Add-on Management Basic Motions",
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


#----------------------------------------------------------
# File layout.py
# Rotation data is stored in a text file
# Every changes to the bvh file has to update on the corresponding text file
#----------------------------------------------------------
import bpy
from SQL_Motions import create_connection, select_basic_movement_by_base
 

#   Layout panel
class BasicMotionsManagement(bpy.types.Panel):
	bl_label = "Basic Motions Management"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOL_PROPS"
 
	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		# Read Basic motions

		layout.label("Upper Body", icon = 'OUTLINER_OB_ARMATURE')
		row = layout.row()
		col = row.column()
		subrow = row.column()
		subrow.operator("my.button", text="Tay Chay Dan", icon = 'POSE_DATA').number = 1
		subrow.operator("my.button", text="Tay Hoa Sen No", icon = 'POSE_DATA').number = 2
		subrow.operator("my.button", text="Tay Le Phat", icon = 'POSE_DATA').number = 3
		subrow.operator("my.button", text="Tay Quay Soi", icon = 'POSE_DATA').number = 4
		subrow.operator("my.button", text="Tay Bat Quyet", icon = 'POSE_DATA').number = 5
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tay Dang Hoa", icon = 'POSE_DATA').number = 6
		subrow.operator("my.button", text="Bay", icon = 'POSE_DATA').number = 7
		subrow.operator("my.button", text="Rung Tay", icon = 'POSE_DATA').number = 8
		subrow.operator("my.button", text="Tay Dang Len Cao", icon = 'POSE_DATA').number = 9
		subrow.operator("my.button", text="Phay Tay", icon = 'POSE_DATA').number = 10
		subrow.operator("my.button", text="Tay Chong Suon", icon = 'POSE_DATA').number = 11
		subrow.operator("my.button", text="Tay Dua Thoi", icon = 'POSE_DATA').number = 12
		subrow.operator("my.button", text="Tay Vun Gon", icon = 'POSE_DATA').number = 13
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tay Dang Ruou", icon = 'POSE_DATA').number = 14
		subrow.operator("my.button", text="Vay Tay", icon = 'POSE_DATA').number = 15
		subrow.operator("my.button", text="Soi Bong", icon = 'POSE_DATA').number = 16
		subrow.operator("my.button", text="Tay Rot Ruou", icon = 'POSE_DATA').number = 17
		subrow.operator("my.button", text="Tay Cheo Do", icon = 'POSE_DATA').number = 18
		subrow.operator("my.button", text="Tay Rac Dau", icon = 'POSE_DATA').number = 19
		subrow.operator("my.button", text="Tay Day Thuyen", icon = 'POSE_DATA').number = 20
		subrow.operator("my.button", text="Xe To The 3", icon = 'POSE_DATA').number = 21
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tay Cuop Bong", icon = 'POSE_DATA').number = 22
		subrow.operator("my.button", text="Tay De Tho", icon = 'POSE_DATA').number = 23
		subrow.operator("my.button", text="Phui Tay Ao", icon = 'POSE_DATA').number = 24
		subrow.operator("my.button", text="Lan Tay Ao", icon = 'POSE_DATA').number = 25
		subrow.operator("my.button", text="Tay Gat Lua", icon = 'POSE_DATA').number = 26
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tau Nhac", icon = 'POSE_DATA').number = 27
		subrow.operator("my.button", text="Tay Vuot Toc", icon = 'POSE_DATA').number = 28
		subrow.operator("my.button", text="Tay Ganh", icon = 'POSE_DATA').number = 29
		subrow.operator("my.button", text="Xe To The 5", icon = 'POSE_DATA').number = 30
		subrow.operator("my.button", text="Tay Nem", icon = 'POSE_DATA').number = 31

		layout.label("Lower Body", icon = 'OUTLINER_OB_ARMATURE')
		row = layout.row()
		col = row.column()
		subrow = row.column()
		subrow.operator("my.button", text="Chan Hinh Chu V", icon = 'POSE_DATA').number = 32
		subrow.operator("my.button", text="Chan Chong Chan Quy", icon = 'POSE_DATA').number = 33
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Chan Chu Chi", icon = 'POSE_DATA').number = 34
		subrow.operator("my.button", text="Hai Dau Goi Cung Quy", icon = 'POSE_DATA').number = 35
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Chan Chu Dinh", icon = 'POSE_DATA').number = 36
		subrow.operator("my.button", text="Hai Chan Co Mot Ben", icon = 'POSE_DATA').number = 37
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Chan Dem Got", icon = 'POSE_DATA').number = 38
		subrow.operator("my.button", text="Hai Chan Duoi Thang", icon = 'POSE_DATA').number = 39
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Chan Qua Tram", icon = 'POSE_DATA').number = 40
		subrow.operator("my.button", text="Hai Chan Bat Cheo", icon = 'POSE_DATA').number = 41

def UpdatedFunction(self, context):
	print("In update func....")
	return

#   Button
class OBJECT_BasicMotion_Button(bpy.types.Operator):
	bl_idname = "my.button"
	bl_label = "Management Basic Motions"
	number = bpy.props.IntProperty()
	row = bpy.props.IntProperty()
	loc = bpy.props.StringProperty()

	checkbox = bpy.props.BoolProperty(name = "Bool Property", default = 0, update = UpdatedFunction)

	def execute(self, context):
		print ("Management Basics")
		return{'FINISHED'}

	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	
	def draw(self, context):
		#pathMotion = []
		Dict_Motion = {1: "ChayDan", 2 : "HoaSenNo", 3 : "LePhat", 4 : "QuaySoi", 5 : "BatQuyet", 6 : "DangHoa", 7 : "Bay", 8 : "RungTay", 9 : "DangLenCao", 10 : "PhayTay",
		11 : "ChongSuon", 12 : "DuaThoi", 13 : "VunGon", 14 : "DangRuou", 15 : "Vay", 16 : "SoiBong", 17 : "RotRuou", 18 : "CheoDo", 19 : "RacDau", 20 : "DayThuyen",
		21 : "XeTo3", 22 : "CuopBong", 23 : "DeTho", 24 : "PhuiTayAo", 25 : "LanTayAo", 26 : "GatLua", 27 : "TauNhac", 28 : "VuotToc", 29 : "Ganh", 30 : "XeTo5", 31 : "Nem",
		32 : "ChanChuV", 33 : "ChanChongQuy", 34 : "ChanChi", 35 : "HaiChanQuy", 36 : "ChanDinh", 37 : "NgoiMotBen", 38 : "ChanDem", 39 : "DuoiHaiChan", 40 : "ChanTram", 41: "ChanBatCheo"}

		Basic_Motion = Dict_Motion[self.number]

		database = "/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/HumanStyle.db"
		conn = create_connection(database)
		with conn:
			select_basic_movement_by_base(conn, Basic_Motion)

		pathMotion = ["/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/Data_Motions/Posture/ChanChongChanQuy.bvh", "/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/Data_Motions/Posture/HuanVH.bvh"]
		print (pathMotion)
		row = self.layout
		for motion in pathMotion:
			row.prop(self, "checkbox", text = motion)
 
#    Registration
def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
	register()