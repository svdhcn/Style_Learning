import bpy,IPython
import math
import pdb
import os.path
import mathutils
from mathutils import Vector,Quaternion
from math import radians, degrees
import numpy as np
context = bpy.context
from scipy.cluster.vq import vq, kmeans, whiten
import matplotlib.pyplot as plt
from scipy import linalg as la
from fbpca import pca
from fbpca import diffsnorm

def Import_Bvh(file_path):
	try:
		if not os.path.exists(file_path):
			print('File .BVH is not available.')
		bpy.ops.import_anim.bvh(filepath=file_path, axis_forward='Y',axis_up='Z', rotate_mode='NATIVE')
		print("Importing is successful !!!")
	except:
		print("Couln't open file: {}".format(file_path))

def Export_Bvh(file_path):
	try:
		if os.path.exists(file_path):
			os.remove(file_path)		
		bpy.context.scene.render.fps = 20  # We configure the frame rate		
		bpy.ops.export_anim.bvh(filepath=file_path, global_scale = 1, frame_start= 1, frame_end= 50, rotate_mode='NATIVE', root_transform_only=True)
		print("Exporting is successful !!!")
	except:
		print("Couldn't export file")

def Get_Data_Key_Frame():
	sce = bpy.context.scene
	ob = bpy.context.object
	for f in range(sce.frame_start, sce.frame_end + 1):
		sce.frame_set(f)
		print("Frame %i" % f)
		for pbone in ob.pose.bones:
			print(pbone.name, pbone.location)

def Get_Data_Rotation():
	sce = bpy.context.scene
	frame_start = 1
	frame_end = 6181
	ob = bpy.context.object
	ROTATION_KEY_DATA = []
	for f in range(frame_start, frame_end):
		sce.frame_set(f)
		rotation_bone = []
		for pbone in ob.pose.bones:
			if pbone.name != "RightShoulder":
				rotation_bone.extend([pbone.rotation_euler.x, pbone.rotation_euler.y ,pbone.rotation_euler.z])				
		ROTATION_KEY_DATA.append(rotation_bone)
	ROTATION_KEY_DATA = np.array(ROTATION_KEY_DATA)
	return ROTATION_KEY_DATA

def kmeans_clustering(K):
	data = pca_rotation(3)
	centroids,_ = kmeans(data, K)
	idx,_ = vq(data,centroids)
	plt.plot(data[idx==0,0],data[idx==0,1],'ob',
	 data[idx==1,0],data[idx==1,1],'or',
	 data[idx==2,0],data[idx==2,1],'og') # third cluster points
	plt.plot(centroids[:,0],centroids[:,1],'sm',markersize=8)
	plt.show()

def pca_rotation(pca_components):
	data = Get_Data_Rotation()
	Display_Data_Rotation(data)
	repeat = 20
	for i in range(repeat):
		(U, s, Va) = pca(data, pca_components, True)
	err = diffsnorm(data, U, s, Va)
	print('facebook pca time: error: %E' % (err))
	IPython.embed()
	return U

def Display_Data_Rotation (X):
    plt.plot(X[:,0], X[:,1], 'b^', markersize = 4, alpha = .8)
    plt.axis('equal')
    plt.plot()
    plt.show()
def Edit_Rotation_Bone( BoneName, FrameNumber, ValueX, ValueY, ValueZ, bdegrees =True):
	sce = bpy.context.scene
	ob = bpy.context.object

	for f in range(sce.frame_start, sce.frame_end+1):
		sce.frame_set(f)
		if f == FrameNumber:
			keyFrame = context.scene.frame_current
			keyInterp = context.user_preferences.edit.keyframe_new_interpolation_type
			for pbone in ob.pose.bones:
				if pbone.name == BoneName:					
					lastMode = pbone.rotation_mode
					pbone.rotation_mode = "XYZ"
					bpy.ops.object.mode_set(mode='POSE')
					pbone.bone.select = True			
					if bdegrees ==True:
						pbone.rotation_euler.x = math.radians(ValueX)
						pbone.rotation_euler.y = math.radians(ValueY)
						pbone.rotation_euler.z = math.radians(ValueZ)
					else:
						pbone.rotation_euler.x = ValueX
						pbone.rotation_euler.y = ValueY
						pbone.rotation_euler.z = ValueZ							
					bpy.context.scene.update()
					pbone.keyframe_insert(data_path="rotation_euler" ,frame=keyFrame)
					context.user_preferences.edit.keyframe_new_interpolation_type = keyInterp
					bpy.ops.object.mode_set(mode='OBJECT')
					pbone.rotation_mode = lastMode