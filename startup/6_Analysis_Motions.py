bl_info = {
	"name": "Add-on Analysis Motions",
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
#from SQL_Motions import add_new_base_pose, add_new_basic_movement, create_connection, select_basic_movement_by_base, select_all_basics
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

class AnalysisSettings(PropertyGroup):

	path = StringProperty(
        name="Path",
        description="Path to Directory",
        default="/home/",
        maxlen=1024,
        subtype='FILE_PATH')

# ------------------------------------------------------------------------
#    operators
# ------------------------------------------------------------------------

class AnalysisMotionOperator(bpy.types.Operator):
	bl_idname = "wm.analysis_motions"
	bl_label = "Analysis Motions"

	List_Bones_UpperBody = ['Chest', 'Chest2', 'Chest3', 'Chest4', 'Neck', 'Head', 'RightCollar', 'RightShoulder', 'RightElbow', 'RightWrist', 'LeftCollar', 'LeftShoulder', 'LeftElbow', 'LeftWrist']
	List_Bones_Lower_Body = ['RightHip', 'RightKnee', 'RightAnkle', 'RightToe', 'LeftHip', 'LeftKnee', 'LeftAnkle', 'LeftToe']

	def execute(self, context):
		print ("This is the function to analysis motions.")	
		return {'FINISHED'}
	
# ------------------------------------------------------------------------
#    my tool in objectmode
# ------------------------------------------------------------------------

class OBJECT_PT_Analysis_panel(Panel):
	bl_idname = "OBJECT_PT_analysis_panel"
	bl_label = "Analysis Motion"
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
		analysistool = scene.analysis_tool
		layout.label("Motion need to Analysis")
		layout.prop(analysistool, "path", text="")
		layout.operator("wm.analysis_motions")

# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------

def register():
	bpy.utils.register_class(OBJECT_PT_Analysis_panel)
	bpy.utils.register_module(__name__)
	bpy.types.Scene.analysis_tool = PointerProperty(type=AnalysisSettings)

def unregister():
	bpy.utils.unregister_class(OBJECT_PT_Analysis_panel)
	bpy.utils.unregister_module(__name__)
	del bpy.types.Scene.analysis_tool

if __name__ == "__main__":
	register()