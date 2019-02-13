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
import Setting
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
		#subrow.operator("my.button", text="Tay Bat Quyet", icon = 'POSE_DATA').number = 5
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tay Dang Hoa", icon = 'POSE_DATA').number = 5
		subrow.operator("my.button", text="Bay", icon = 'POSE_DATA').number = 6
		subrow.operator("my.button", text="Rung Tay", icon = 'POSE_DATA').number = 7
		subrow.operator("my.button", text="Tay Dang Len Cao", icon = 'POSE_DATA').number = 8
		subrow.operator("my.button", text="Phay Tay", icon = 'POSE_DATA').number = 9
		subrow.operator("my.button", text="Tay Chong Suon", icon = 'POSE_DATA').number = 10
		subrow.operator("my.button", text="Tay Dua Thoi", icon = 'POSE_DATA').number = 11
		subrow.operator("my.button", text="Tay Vun Gon", icon = 'POSE_DATA').number = 12
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tay Dang Ruou", icon = 'POSE_DATA').number = 13
		subrow.operator("my.button", text="Vay Tay", icon = 'POSE_DATA').number = 14
		subrow.operator("my.button", text="Soi Bong", icon = 'POSE_DATA').number = 15
		subrow.operator("my.button", text="Tay Rot Ruou", icon = 'POSE_DATA').number = 16
		subrow.operator("my.button", text="Tay Cheo Do", icon = 'POSE_DATA').number = 17
		subrow.operator("my.button", text="Tay Rac Dau", icon = 'POSE_DATA').number = 18
		subrow.operator("my.button", text="Tay Day Thuyen", icon = 'POSE_DATA').number = 19
		subrow.operator("my.button", text="Xe To The 3", icon = 'POSE_DATA').number = 20
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tay Cuop Bong", icon = 'POSE_DATA').number = 21
		subrow.operator("my.button", text="Tay De Tho", icon = 'POSE_DATA').number = 22
		subrow.operator("my.button", text="Phui Tay Ao", icon = 'POSE_DATA').number = 23
		subrow.operator("my.button", text="Lan Tay Ao", icon = 'POSE_DATA').number = 24
		subrow.operator("my.button", text="Tay Gat Lua", icon = 'POSE_DATA').number = 25
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tau Nhac", icon = 'POSE_DATA').number = 26
		subrow.operator("my.button", text="Tay Vuot Toc", icon = 'POSE_DATA').number = 27
		subrow.operator("my.button", text="Tay Ganh", icon = 'POSE_DATA').number = 28
		subrow.operator("my.button", text="Xe To The 5", icon = 'POSE_DATA').number = 29
		subrow.operator("my.button", text="Tay Nem", icon = 'POSE_DATA').number = 30

		layout.label("Lower Body", icon = 'OUTLINER_OB_ARMATURE')
		row = layout.row()
		col = row.column()
		subrow = row.column()
		subrow.operator("my.button", text="Chan Chu Chi (Nam)", icon = 'POSE_DATA').number = 31
		subrow.operator("my.button", text="Chan Chu Chi (Nu)", icon = 'POSE_DATA').number = 32
		subrow.operator("my.button", text="Chan Chong Chan Quy", icon = 'POSE_DATA').number = 33
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Chan Chu Dinh", icon = 'POSE_DATA').number = 34
		subrow.operator("my.button", text="Chan Dem Got", icon = 'POSE_DATA').number = 35
		subrow.operator("my.button", text="Hai Dau Goi Cung Quy", icon = 'POSE_DATA').number = 36
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Chan Nu Lech", icon = 'POSE_DATA').number = 37
		subrow.operator("my.button", text="Chan Nam Ngang", icon = 'POSE_DATA').number = 38
		subrow.operator("my.button", text="Hai Chan Ngoi Mot Ben", icon = 'POSE_DATA').number = 39
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Chan Qua Tram", icon = 'POSE_DATA').number = 40
		subrow.operator("my.button", text="Chan Lao Say", icon = 'POSE_DATA').number = 41
		subrow.operator("my.button", text="Chan Bat Cheo", icon = 'POSE_DATA').number = 42
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Chan Khong Luu (Nam)", icon = 'POSE_DATA').number = 43
		subrow.operator("my.button", text="Chan Khong Luu (Nu)", icon = 'POSE_DATA').number = 44
		subrow.operator("my.button", text="Chan Chu V - Xien", icon = 'POSE_DATA').number = 45

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
		bpy.ops.object.mode_set(mode='OBJECT')
		bpy.ops.object.delete(use_global=False)
		for pathmotion in self.pathMotion:
			bpy.ops.import_anim.bvh(filepath= pathmotion, axis_forward="Y", axis_up="Z", rotate_mode="NATIVE")
	
		return{'FINISHED'}

	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	
	def draw(self, context):
		self.pathMotion = []

		Basic_Motion = Setting.Dict_Motion[self.number]
		
		database = Setting.path_database

		conn = create_connection(database)
		with conn:
			Body = 0
			if Basic_Motion in Setting.List_Motion_Upper:
				Body = 0
			elif Basic_Motion in Setting.List_Motion_Lower:
				Body = 1
			list_basic_movement = select_basic_movement_by_base(conn, Basic_Motion, Body)

		for i in range(0, len(list_basic_movement)):
			self.pathMotion.append(list_basic_movement[i][4])

		#pathMotion = ["/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/Data_Motions/Posture/ChanChongChanQuy.bvh", "/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/Data_Motions/Posture/HuanVH.bvh"]
		print (self.pathMotion)
		row = self.layout
		for motion in self.pathMotion:
			row.prop(self, "checkbox", text = motion)
 
#    Registration
def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
	register()