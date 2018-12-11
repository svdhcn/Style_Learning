#----------------------------------------------------------
# File layout.py
# Rotation data is stored in a text file
# Every changes to the bvh file has to update on the corresponding text file
#----------------------------------------------------------
import bpy
from SQL_Motions import select_basic_movement_by_base
 

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
		subrow.operator("my.button", text="Chay Dan", icon = 'POSE_DATA').number = 1
		subrow.operator("my.button", text="Hoa Sen No", icon = 'POSE_DATA').number = 2
		subrow.operator("my.button", text="Le Phat", icon = 'POSE_DATA').number = 3
		subrow.operator("my.button", text="Quay Soi", icon = 'POSE_DATA').number = 4
		subrow.operator("my.button", text="Bat Quyet", icon = 'POSE_DATA').number = 5
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Dang Hoa", icon = 'POSE_DATA').number = 6
		subrow.operator("my.button", text="Bay", icon = 'POSE_DATA').number = 7
		subrow.operator("my.button", text="Dung Tay", icon = 'POSE_DATA').number = 8
		subrow.operator("my.button", text="Dang Len Cao", icon = 'POSE_DATA').number = 9
		subrow.operator("my.button", text="Phay Tay", icon = 'POSE_DATA').number = 10
		subrow.operator("my.button", text="Chong Suon", icon = 'POSE_DATA').number = 11
		subrow.operator("my.button", text="Dua Thoi", icon = 'POSE_DATA').number = 12
		subrow.operator("my.button", text="Vun Gon", icon = 'POSE_DATA').number = 13
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Dang Ruou", icon = 'POSE_DATA').number = 14
		subrow.operator("my.button", text="Vay", icon = 'POSE_DATA').number = 15
		subrow.operator("my.button", text="Soi Bong", icon = 'POSE_DATA').number = 16
		subrow.operator("my.button", text="Rot Ruou", icon = 'POSE_DATA').number = 17
		subrow.operator("my.button", text="Cheo Do", icon = 'POSE_DATA').number = 18
		subrow.operator("my.button", text="Rac Dau", icon = 'POSE_DATA').number = 19
		subrow.operator("my.button", text="Day Thuyen", icon = 'POSE_DATA').number = 20
		subrow.operator("my.button", text="Xe To", icon = 'POSE_DATA').number = 21
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Cuop Bong", icon = 'POSE_DATA').number = 22
		subrow.operator("my.button", text="De Tho", icon = 'POSE_DATA').number = 23
		subrow.operator("my.button", text="Phui Tay Ao", icon = 'POSE_DATA').number = 24
		subrow.operator("my.button", text="Lan Tay Ao", icon = 'POSE_DATA').number = 25
		subrow.operator("my.button", text="Gat Lua", icon = 'POSE_DATA').number = 26
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tau Nhac", icon = 'POSE_DATA').number = 27
		subrow.operator("my.button", text="Vuot Toc", icon = 'POSE_DATA').number = 28
		subrow.operator("my.button", text="Ganh", icon = 'POSE_DATA').number = 29
		subrow.operator("my.button", text="Xe To", icon = 'POSE_DATA').number = 30
		subrow.operator("my.button", text="Nem", icon = 'POSE_DATA').number = 31

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
		subrow.operator("my.button", text="Dem Got", icon = 'POSE_DATA').number = 38
		subrow.operator("my.button", text="Duoi Thang Hai Chan", icon = 'POSE_DATA').number = 39
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tau Nhac", icon = 'POSE_DATA').number = 40
		subrow.operator("my.button", text="Hai Chan Bat Cheo", icon = 'POSE_DATA').number = 41

#   Button
class OBJECT_BasicMotion_Button(bpy.types.Operator):
	bl_idname = "my.button"
	bl_label = "Button"
	number = bpy.props.IntProperty()
	row = bpy.props.IntProperty()
	loc = bpy.props.StringProperty()

	def execute(self, context):
		if self.number == 1:
			print ("Chay Dan")
		elif self.number == 2:
			print ("Hoa sen no")
		elif self.number == 3:
			print ("Le Phat")
		else:
			print ("Huan")
		
		return{'FINISHED'}
 
#    Registration
def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
	register()