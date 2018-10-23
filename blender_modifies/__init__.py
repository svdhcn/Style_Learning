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
		bpy.ops.export_anim.bvh(filepath=file_path, global_scale = 1, frame_start= 1, frame_end= 6180, rotate_mode='NATIVE', root_transform_only=True)
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
	frame_end = 6180
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

def kmeans_clustering_preview(K):
	data = pca_rotation(2)
	#Display_Data_Rotation(data)
	repeat = 1
	for i in range(repeat):
		centroids,_ = kmeans(data, K)
		idx,_ = vq(data,centroids)
		plt.scatter(data[:, 0], data[:, 1], c=idx, s=50, cmap='viridis');
		plt.plot(centroids[:,0],centroids[:,1],'sm',markersize=8)
		plt.show()

def kmeans_clustering():
	K = 30
	data = Get_Data_Rotation()
	repeat = 30
	mindiff = 0
	Centroids
	# begin repeat n times with k means
	for i in range(repeat):
		centroids,diff = kmeans(data, K)
		if mindiff > diff:
			mindiff = diff
			Centroids = centroids
			print (mindiff)
	#  end repeat
	labels,_ = vq(data,Centroids)
	data = [[]]
	for label in labels:
		data.append(centroids[label])
	data.remove([])
	return data

	#anch = [[]]
	#for i in range(0, len(data)):
	#	if i%20 == 0:
	#		anch.append[data[i]]
	#bspline
	#IPython.embed()
	#print("centroids:", centroids)
	#plt.scatter(data[:, 0], data[:, 1], c=idx, s=50, cmap='viridis');
	#plt.plot(centroids[:,0],centroids[:,1],'sm',markersize=8)
	#plt.show()
	
def Edit_data():
	data = kmeans_clustering()
	data = np.array(data)
	frame_start = 1
	frame_end = 6180
	sce = bpy.context.scene
	ob = bpy.context.object
	for f in range(frame_start, frame_end):
		sce.frame_set(f)
		keyFrame = context.scene.frame_current
		keyInterp = context.user_preferences.edit.keyframe_new_interpolation_type
		for pbone in ob.pose.bones:
			lastMode = pbone.rotation_mode
			pbone.rotation_mode = "XYZ"
			bpy.ops.object.mode_set(mode='POSE')
			pbone.bone.select = True
			if pbone.name == "RightElbow":					
				pbone.rotation_euler.x = data[f - 1][0]
				pbone.rotation_euler.y = data[f - 1][1]
				pbone.rotation_euler.z = data[f - 1][2]	
			elif pbone.name == "RightWrist":
				pbone.rotation_euler.x = data[f - 1][3]
				pbone.rotation_euler.y = data[f - 1][4]
				pbone.rotation_euler.z = data[f - 1][5]	
			bpy.context.scene.update()
			pbone.keyframe_insert(data_path="rotation_euler" ,frame=keyFrame)
			context.user_preferences.edit.keyframe_new_interpolation_type = keyInterp
			bpy.ops.object.mode_set(mode='OBJECT')
			pbone.rotation_mode = lastMode
	print("Edit done")

def pca_rotation(pca_components):
	data = Get_Data_Rotation()
	(U, s, Va) = pca(data, pca_components, True)
	print("U", U.shape, "s", s.shape, "Va", Va.shape)
	err = diffsnorm(data, U, s, Va)
	print('facebook pca time: error: %E' % (err))
	return np.dot(U,np.diag(s))

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