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

from HMI_Motions import Kmeans_Clustering
import Setting
import IPython
# ------------------------------------------------------------------------
#    store properties in the active scene
# ------------------------------------------------------------------------

class ClusterSettings(PropertyGroup):

	NumberOfCluster = IntProperty(
		name = "Number Of Clusters",
		description="A integer property",
		default = 100,
		min = 0
		)

	Divide_Motions = EnumProperty(
		name="Divide Motions:",
		description="Data motion attribute.",
		items=[ ('Upper', "Upper Motion", ""),
				('Lower', "Lower Motion", "")]
		)

# ------------------------------------------------------------------------
#    operators
# ------------------------------------------------------------------------

class ClusterMotionOperator(bpy.types.Operator):
	bl_idname = "wm.cluster_motions"
	bl_label = "Clustering Basic Motions"	

	def execute(self, context):
		scene = context.scene
		clustertool = scene.cluster_tool
		pathMotions = []

		database = Setting.path_database
		conn = create_connection(database)
		with conn:
			list_basic_movement = select_all_basics(conn, Setting.Divide_Body[clustertool.Divide_Motions])
					
		for i in range(0, len(list_basic_movement)):
			pathMotions.append(list_basic_movement[i][4])

		Divide_Motion = Setting.Divide_Body[clustertool.Divide_Motions]
		#IPython.embed()
				
		Kmeans_Clustering(clustertool.NumberOfCluster, Divide_Motion, pathMotions)
	
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
		layout.prop(clustertool, "Divide_Motions", text="")
		layout.prop(clustertool, "NumberOfCluster")
		#layout.prop(clustertool, "path", text="")
		layout.operator("wm.cluster_motions")
		#row = layout.row()
		#row.operator("wm.upper_motions")
		#row.operator("wm.lower_motions")

# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------

def register():
	bpy.utils.register_class(OBJECT_PT_cluster_panel)
	bpy.utils.register_module(__name__)
	bpy.types.Scene.cluster_tool = PointerProperty(type=ClusterSettings)

def unregister():
	bpy.utils.unregister_class(OBJECT_PT_cluster_panel)
	bpy.utils.unregister_module(__name__)
	del bpy.types.Scene.cluster_tool

if __name__ == "__main__":
	register()