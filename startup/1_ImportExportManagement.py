#----------------------------------------------------------
# File BvhFileManagement
#----------------------------------------------------------
import bpy

from bpy_extras.io_utils import ImportHelper, ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, IntProperty
from bpy.types import Operator

# Class Creat Basic Motions
class BvhFileManagement(bpy.types.Panel):
	bl_label = "Import Export BVH file"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOL_PROPS"

	@classmethod
	def poll(self,context):
		return context.object is not None
 
	def draw(self, context):
		layout = self.layout		
		# Creat Basic motions
		row = layout.row()
		row.alignment = 'LEFT'
		row.operator("wm.import", text="Import BVH file", icon = 'IMPORT')
		row.operator("wm.export", text="Export BVH file", icon = 'EXPORT')

class ExportBvhData(Operator, ExportHelper):
	bl_idname = "wm.export"
	bl_label = "Export BVH Data"

	filename_ext = ".bvh"

	filter_glob = StringProperty(
			default="*.bvh",
			options={'HIDDEN'},
			maxlen=255,  # Max internal buffer length, longer would be clamped.
			)

	scale = IntProperty(
		name = "Scale",
		description = "Scale",
		default = 1,
		min = 1
		)

	startFrame = IntProperty(
		name = "Start Frame",
		description = "Start Frame",
		default = 0,
		min = 0
		)

	endFrame = IntProperty(
		name = "End Frame",
		description = "End Frame",
		default = 250,
		min = 1
		)

	rotation = EnumProperty(
			name="Rotation",
			description="Choose items",
			items=(('NATIVE', "Euler(Native)", ""),
				   ('XYZ', "Euler(XYZ)", ""),
				   ('XZY', "Euler(XZY)", ""),
				   ('YXZ', "Euler(YXZ)", ""),
				   ('YZX', "Euler(YZX)", ""),
				   ('ZXY', "Euler(ZXY)", ""),
				   ('ZYX', "Euler(ZYX)", "")),
			default='NATIVE',
			)

	translation = BoolProperty(
            name="Root Translation Only",
            description="Root Translation Only",
            default= True,
            )


	def execute(self, context):
		bpy.context.scene.render.fps = 60		
		print ("hello, this is function export")
		return bpy.ops.export_anim.bvh(filepath=self.filepath, global_scale = self.scale, frame_start= self.startFrame, frame_end= self.endFrame, rotate_mode=self.rotation, root_transform_only=self.translation)


class ImportBvhData(Operator, ImportHelper):
	"""This appears in the tooltip of the operator and in the generated docs"""
	bl_idname = "wm.import"  # important since its how bpy.ops.import_test.some_data is constructed
	bl_label = "Import BVH Data"

	# ImportHelper mixin class uses this
	filename_ext = ".bvh"

	filter_glob = StringProperty(
			default="*.bvh",
			options={'HIDDEN'},
			maxlen=255,  # Max internal buffer length, longer would be clamped.
			)

	# List of operator properties, the attributes will be assigned
	# to the class instance from the operator settings before calling.

	forward = EnumProperty(
			name="Forward",
			description="Choose items",
			items=(('X', "X Forward", ""),
				   ('Y', "Y Forward", ""),
				   ('Z', "Z Forward", ""),
				   ('-X', "-X Forward", ""),
				   ('-Y', "-Y Forward", ""),
				   ('-Z', "-Z Forward", "")),
			default='Y',
			)

	up = EnumProperty(
			name="Up",
			description="Choose items",
			items=(('X', "X Up", ""),
				   ('Y', "Y Up", ""),
				   ('Z', "Z Up", ""),
				   ('-X', "-X Up", ""),
				   ('-Y', "-Y Up", ""),
				   ('-Z', "-Z Up", "")),
			default='Z',
			)
	rotation = EnumProperty(
			name="Rotation",
			description="Choose items",
			items=(('Quaternion', "Quaternion", ""),
				   ('NATIVE', "Euler(Native)", ""),
				   ('XYZ', "Euler(XYZ)", ""),
				   ('XZY', "Euler(XZY)", ""),
				   ('YXZ', "Euler(YXZ)", ""),
				   ('YZX', "Euler(YZX)", ""),
				   ('ZXY', "Euler(ZXY)", ""),
				   ('ZYX', "Euler(ZYX)", "")),
			default='NATIVE',
			)

	def execute(self, context):
		bpy.context.scene.render.fps = 60
		return bpy.ops.import_anim.bvh(filepath= self.filepath, axis_forward=self.forward, axis_up=self.up, rotate_mode=self.rotation)

 
#    Registration
def register():
	bpy.utils.register_class(ImportBvhData)
	#bpy.utils.register_class(ExportBvhData)
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.register_class(ImportBvhData)
	#bpy.utils.register_class(ExportBvhData)
	bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
	register()

	# test call
	#bpy.ops.import_test.some_data('INVOKE_DEFAULT')