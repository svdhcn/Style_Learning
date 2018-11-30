#----------------------------------------------------------
# File layout.py
#----------------------------------------------------------
import bpy
 

#   Layout panel
class LayoutPanel(bpy.types.Panel):
	bl_label = "Style Learning Management"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOL_PROPS"
 
	def draw(self, context):
		layout = self.layout
		
		# Creat Basic motions
		layout.label("Creat Basic motions")
		row = layout.row()
		row.alignment = 'LEFT'
		row.operator("my.button", text="Import BVH file", icon = 'IMPORT').number=1
		row.operator("my.button", text="Export BVH file", icon = 'EXPORT').number=2

		# Read Basic motions
		layout.label("Read Basic motions")

		layout.label("Upper Body", icon = 'OUTLINER_OB_ARMATURE')
		row = layout.row()
		col = row.column()
		subrow = row.column()
		subrow.operator("my.button", text="Chay Dan", icon = 'POSE_DATA').number = 3
		subrow.operator("my.button", text="Hoa Sen No", icon = 'POSE_DATA').number = 4
		subrow.operator("my.button", text="Le Phat", icon = 'POSE_DATA').number = 5
		subrow.operator("my.button", text="Quay Soi", icon = 'POSE_DATA').number = 6
		subrow.operator("my.button", text="Bat Quyet", icon = 'POSE_DATA').number = 7
		subrow = row.column(align=True)
		subrow.operator("my.button", text="Dang Hoa", icon = 'POSE_DATA').loc="5 21"
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

		layout.label("Update Basic motions")
		row = layout.row()
		box = row.box()
		box.operator("my.button", text="11", emboss=False).loc="4 11"
		box.operator("my.button", text="12", emboss=False).loc="4 12"
		col = row.column()
		subrow = col.row()
		subrow.operator("my.button", text="13").loc="4 13"
		subrow.operator("my.button", text="14").loc="4 14"
		subrow = col.row(align=True)
		subrow.operator("my.button", text="15").loc="4 15"
		subrow.operator("my.button", text="16").loc="4 16"
		box = row.box()
		box.operator("my.button", text="17").number=17
		box.separator()
		box.operator("my.button", text="18")
		box.operator("my.button", text="19")
 
		layout.label("Delete Basic motions")
		row = layout.row()
		row.alignment = 'LEFT'
		row.operator("my.button", text="Delete Basic Motions")

#   Button
class OBJECT_OT_Button(bpy.types.Operator):
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
bpy.utils.register_module(__name__)