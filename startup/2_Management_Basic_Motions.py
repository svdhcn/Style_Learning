#----------------------------------------------------------
# File layout.py
#----------------------------------------------------------
import bpy
 

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
		subrow.operator("my.button", text="Dang Hoa", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Bay", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Dung Tay", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Dang Len Cao", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Phay Tay", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Chong Suon", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Dua Thoi", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Vun Gon", icon = 'POSE_DATA')
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Dang Ruou", icon = 'POSE_DATA').loc="5 21"
		subrow.operator("my.button", text="Vay", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Soi Bong", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Rot Ruou", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Cheo Do", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Rac Dau", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Day Thuyen", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Xe To", icon = 'POSE_DATA')
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Cuop Bong", icon = 'POSE_DATA').loc="5 21"
		subrow.operator("my.button", text="De Tho", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Phui Tay Ao", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Lan Tay Ao", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Gat Lua", icon = 'POSE_DATA')
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tau Nhac", icon = 'POSE_DATA').loc="5 21"
		subrow.operator("my.button", text="Vuot Toc", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Ganh", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Xe To", icon = 'POSE_DATA')
		subrow.operator("my.button", text="Nem", icon = 'POSE_DATA')

		layout.label("Lower Body", icon = 'OUTLINER_OB_ARMATURE')
		row = layout.row()
		col = row.column()
		subrow = row.column()
		subrow.operator("my.button", text="Chan Hinh Chu V", icon = 'POSE_DATA').loc="5 21"
		subrow.operator("my.button", text="Chan Chong Chan Quy", icon = 'POSE_DATA')
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Chan Chu Chi", icon = 'POSE_DATA').loc="5 21"
		subrow.operator("my.button", text="Hai Dau Goi Cung Quy", icon = 'POSE_DATA')
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Chan Chu Dinh", icon = 'POSE_DATA').loc="5 21"
		subrow.operator("my.button", text="Hai Chan Co Mot Ben", icon = 'POSE_DATA')
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Dem Got", icon = 'POSE_DATA').loc="5 21"
		subrow.operator("my.button", text="Duoi Thang Hai Chan", icon = 'POSE_DATA')
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Tau Nhac", icon = 'POSE_DATA').loc="5 21"
		subrow.operator("my.button", text="Hai Chan Bat Cheo", icon = 'POSE_DATA')

#   Button
class OBJECT_BasicMotion_Button(bpy.types.Operator):
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
def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
	register()