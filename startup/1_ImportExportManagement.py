#----------------------------------------------------------
# File layout.py
#----------------------------------------------------------
import bpy
 
# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
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
		row.operator("my.button", text="Import BVH file", icon = 'IMPORT')
		#row.operator("my.button", text="Export BVH file", icon = 'EXPORT').number=2


class ImportSomeData(Operator, ImportHelper):
	"""This appears in the tooltip of the operator and in the generated docs"""
	bl_idname = "my.button"  # important since its how bpy.ops.import_test.some_data is constructed
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

	Forward = EnumProperty(
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

	Up = EnumProperty(
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
	Rotation = EnumProperty(
			name="Rotation",
			description="Choose between two items",
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
		print ("The local file path is:", self.filepath)
		print("Forward", self.Forward)
		print("Up", self.Up)
		print("Rotation", self.Rotation)
		return bpy.ops.import_anim.bvh(filepath= self.filepath, axis_forward=self.Forward, axis_up=self.Up, rotate_mode=self.Rotation)
		#return read_some_data(context, self.filepath, self.use_setting)

 #    Registration
#bpy.utils.register_module(__name__)
 
#    Registration
def register():
	bpy.utils.register_class(ImportSomeData)
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.register_class(ImportSomeData)
	bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
	register()

	# test call
	bpy.ops.import_test.some_data('INVOKE_DEFAULT')