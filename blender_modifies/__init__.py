import bpy,IPython
import math
import pdb
import os.path
from bpy import context
import mathutils
from mathutils import Vector,Quaternion
from math import radians, degrees

def Import_Bvh(file_path):
	try:
		if not os.path.exists(file_path):
			IPython.embed()
			print('File .BVH is not available.')
		bpy.ops.import_anim.bvh(filepath=file_path, axis_forward='Y',axis_up='Z', rotate_mode='NATIVE')
	except:
		print("Couln't open file: {}".format(file_path))

def Export_Bvh(file_path):
	try:
		if os.path.exists(file_path):
			os.remove(file_path)
		scn = bpy.context.scene

		bpy.context.scene.render.fps = 20  # We configure the frame rate		
		bpy.ops.export_anim.bvh(filepath=file_path, global_scale = 1, frame_start= scn.frame_start, frame_end= scn.frame_end, rotate_mode='NATIVE', root_transform_only=True)	
	except:
		print("Couldn't export file")

def Get_Data_Key_Frame():
	sce = bpy.context.scene
	ob = bpy.context.object

	for f in range(sce.frame_start, sce.frame_end+1):
		sce.frame_set(f)
		print("Frame %i" % f)
		for pbone in ob.pose.bones:
			IPython.embed()
			print(pbone.name, pbone.location)

def Rotation_Bone( BoneName, FrameNumber, ValueX, ValueY, ValueZ):
	sce = bpy.context.scene
	ob = bpy.context.object
	
	for f in range(sce.frame_start, sce.frame_end+1):
		sce.frame_set(f)
		if f == FrameNumber:
			keyFrame = context.scene.frame_current
			keyInterp = context.user_preferences.edit.keyframe_new_interpolation_type
			for pbone in ob.pose.bones:
				if pbone.name == BoneName:
					bpy.ops.object.mode_set(mode='POSE')
					pbone.bone.select = True
					IPython.embed()
					pbone.rotation_euler.x = math.radians(ValueX)
					pbone.rotation_euler.y = math.radians(ValueY)
					pbone.rotation_euler.z = math.radians(ValueZ)					
					bpy.context.scene.update()
					#IPython.embed()
					pbone.keyframe_insert(data_path="rotation_euler" ,frame=keyFrame)
					context.user_preferences.edit.keyframe_new_interpolation_type = keyInterp
					bpy.ops.object.mode_set(mode='OBJECT')