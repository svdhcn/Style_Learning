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
# lib use to pca
from fbpca import pca
from fbpca import diffsnorm
# lib use to Gaussian Process model for regression
import GPy
from scipy.interpolate import BSpline

from os import listdir
from os.path import isfile, join

from bvh import Bvh
 # lib use to HMM
import imp
from hmmlearn import hmm


data_rotation_body = []
data_rotation_foots = []
data_location_hips = []
basic_motion = []
frame_start = 1
frame_end = 1
List_Bones_UpperBody = ['Chest', 'Chest2', 'Chest3', 'Chest4', 'Neck', 'Head', 'RightCollar', 'RightShoulder', 'RightElbow', 'RightWrist', 'LeftCollar', 'LeftShoulder', 'LeftElbow', 'LeftWrist']
List_Bones_LowerBody = ['RightHip', 'RightKnee', 'RightAnkle', 'RightToe', 'LeftHip', 'LeftKnee', 'LeftAnkle', 'LeftToe']

""""""""""""""""""""""""""""" Machine Learning """""""""""""""""""""""""""""""""""""""

def Kmeans_Clustering_Preview(K):
	data = Pca_Rotation(2)

	plt.plot(data[:,0], data[:,1], 'b^', markersize = 4, alpha = .8)
	plt.axis('equal')
	plt.plot()
	plt.show()

	repeat = 10
	mindiff = 0.0
	labels = []
	Centroids = []
	# begin repeat n times with k means
	for i in range(repeat):
		centroids,diff = kmeans(data, K)
		if i == 0:
			mindiff = diff
			Centroids = centroids
			print (mindiff)
			labels,_ = vq(data,Centroids)
		else:
			if mindiff > diff:
				mindiff = diff
				Centroids = centroids
				print ("mindiff ",mindiff)
				print("New centroids", Centroids)				
				labels,_ = vq(data,Centroids)
	#  end repeat
	print("Centroids", Centroids)
	plt.scatter(data[:, 0], data[:, 1], c=labels, s=50, cmap='viridis');
	plt.plot(Centroids[:,0],Centroids[:,1],'sm',markersize=8)
	plt.show()

def Kmeans_Clustering(K, body, listPathMotions, pathCluster):
	# Read all File motions in data base, 
	# Get all data Rotation in .bvh file	
	for pathMotion in listPathMotions:
		bpy.ops.import_anim.bvh(filepath= pathMotion, axis_forward="Y", axis_up="Z", rotate_mode="NATIVE")
		with open(pathMotion) as f:
			global frame_end			
			mocap = Bvh(f.read())
			frame_end = mocap.nframes
		if body == "Upper":
			data = Get_Data_Rotation_UpperBody()
		elif body == "Lower":
			data = Get_Data_Rotation_LowerBody()
		bpy.ops.object.mode_set(mode='OBJECT')
		bpy.ops.object.delete(use_global=False)
	repeat = 5
	mindiff = 0.0
	labels = []
	Centroids = []
	# begin repeat n times with k means
	for i in range(repeat):
		centroids,diff = kmeans(data, K)
		if i == 0:
			mindiff = diff
			Centroids = centroids
			labels,_ = vq(data,Centroids)
		elif mindiff > diff:
			mindiff = diff
			Centroids = centroids
			labels,_ = vq(data,Centroids)
	#  end repeat
	# Export cluster in .txt file
	file = open(pathCluster, "w+")
	file.write(str(Centroids))
	file.close()
	
	'''
	data = [[]]
	for label in labels:
		data.append(Centroids[label])
	data.remove([])
	data = np.array(data)	
	#smoothData = Bspline_Rotation_Data(labels, data)	
	return data
	'''

def Pca_Rotation(pca_components):
	# This function to loss dimention data

	data = Get_Data_Rotation()
	(U, s, Va) = pca(data, pca_components, True)
	print("U", U.shape, "s", s.shape, "Va", Va.shape)
	err = diffsnorm(data, U, s, Va)
	print('facebook pca time: error: %E' % (err))
	return np.dot(U,np.diag(s))

""""""""""""""""""""""""""""" Execute Data """""""""""""""""""""""""""""
# This function to get all data rotation of bones

def Get_Data_Rotation_UpperBody():	
	sce = bpy.context.scene
	ob = bpy.context.object
	ROTATION_KEY_DATA = []
	for f in range(frame_start, frame_end):
		sce.frame_set(f)
		rotation_bone = []
		for pbone in ob.pose.bones:
			if pbone.name in List_Bones_UpperBody:
				rotation_bone.extend([pbone.rotation_euler.x, pbone.rotation_euler.y ,pbone.rotation_euler.z])								
		ROTATION_KEY_DATA.append(rotation_bone)
	ROTATION_KEY_DATA = np.array(ROTATION_KEY_DATA)
	return ROTATION_KEY_DATA

def Get_Data_Rotation_LowerBody():	
	sce = bpy.context.scene
	ob = bpy.context.object
	ROTATION_KEY_DATA = []
	for f in range(frame_start, frame_end):
		sce.frame_set(f)
		rotation_bone = []
		for pbone in ob.pose.bones:
			if pbone.name in List_Bones_LowerBody:
				rotation_bone.extend([pbone.rotation_euler.x, pbone.rotation_euler.y ,pbone.rotation_euler.z])								
		ROTATION_KEY_DATA.append(rotation_bone)
	ROTATION_KEY_DATA = np.array(ROTATION_KEY_DATA)
	return ROTATION_KEY_DATA

def Get_data_rotation_Body():
	global data_rotation_body
	data_rotation_body = Get_Data_Rotation()

def Get_data_rotation_Foots():
	global data_rotation_foots
	data_rotation_foots = Get_Data_Rotation()

def Get_Basic_Motion():
	global basic_motion
	basic_motion = Kmeans_Clustering()

def Edit_Data_Rotation_Foots():
	# This funtion to change rotation Foots data of bone
	#data = Kmeans_Clustering()	
	print('Shape data rotation foots is:', data_rotation_foots.shape)
	sce = bpy.context.scene
	ob = bpy.context.object	
	bpy.ops.object.mode_set(mode='POSE')
	frame_end_change = data_rotation_foots.shape[0]
	for f in range(frame_start, frame_end_change):
		frameSet = f - 1
		sce.frame_set(f)
		keyFrame = context.scene.frame_current
		keyInterp = context.user_preferences.edit.keyframe_new_interpolation_type
		context.user_preferences.edit.keyframe_new_interpolation_type = "BEZIER"
		for pbone in ob.pose.bones:
			lastMode = pbone.rotation_mode
			pbone.rotation_mode = "XYZ"
			pbone.bone.select = True
			if pbone.name not in List_Bones_Foots:
				continue
			if pbone.name == 'Hips':
				continue		
			if pbone.name == "RightHip":
				pbone.rotation_euler = data_rotation_foots[frameSet][3:6]
			elif pbone.name == "RightKnee":
				pbone.rotation_euler = data_rotation_foots[frameSet][6:9]
			elif pbone.name == "RightAnkle":
				pbone.rotation_euler = data_rotation_foots[frameSet][9:12]
			elif pbone.name == "RightToe":
				pbone.rotation_euler = data_rotation_foots[frameSet][12:15]
			elif pbone.name == "LeftHip":
				pbone.rotation_euler = data_rotation_foots[frameSet][15:18]
			elif pbone.name == "LeftKnee":
				pbone.rotation_euler = data_rotation_foots[frameSet][18:21]
			elif pbone.name == "LeftAnkle":
				pbone.rotation_euler = data_rotation_foots[frameSet][21:24]
			elif pbone.name == "LeftToe":
				pbone.rotation_euler = data_rotation_foots[frameSet][24:27]
			bpy.context.scene.update()
			pbone.keyframe_insert(data_path="rotation_euler" ,frame=keyFrame)
			pbone.rotation_mode = lastMode
			context.user_preferences.edit.keyframe_new_interpolation_type = keyInterp
			#IPython.embed()
	bpy.ops.object.mode_set(mode='OBJECT')
	print("Edit rotation done")	

def Edit_Data_Rotation_Body():
	# This funtion to change rotation data of bone
	print('Shape data rotation foots is:', data_rotation_body.shape)
	sce = bpy.context.scene
	ob = bpy.context.object	
	bpy.ops.object.mode_set(mode='POSE')
	frame_end_change = data_rotation_body.shape[0]
	for f in range(frame_start, frame_end_change):
		frameSet = f - 1
		sce.frame_set(f)
		sce.frame_set(frameSet)
		keyFrame = context.scene.frame_current
		keyInterp = context.user_preferences.edit.keyframe_new_interpolation_type
		context.user_preferences.edit.keyframe_new_interpolation_type = "BEZIER"
		for pbone in ob.pose.bones:
			lastMode = pbone.rotation_mode
			pbone.rotation_mode = "XYZ"
			pbone.bone.select = True
			if pbone.name not in List_Bones_Body:
				continue
			if pbone.name == 'Hips':
				continue
			elif pbone.name == 'Chest':
				pbone.rotation_euler = data_rotation_body[frameSet][3: 6]
			elif pbone.name == 'Chest2':
				pbone.rotation_euler = data_rotation_body[frameSet][6: 9]
			elif pbone.name =='Chest3':
				pbone.rotation_euler = data_rotation_body[frameSet][9: 12]
			elif pbone.name == 'Chest4':
				pbone.rotation_euler = data_rotation_body[frameSet][12: 15]
			elif pbone.name == 'Neck':
				pbone.rotation_euler = data_rotation_body[frameSet][15: 18]
			elif pbone.name == 'Head':
				pbone.rotation_euler = data_rotation_body[frameSet][18: 21]
			elif pbone.name == 'RightCollar':
				pbone.rotation_euler = data_rotation_body[frameSet][21: 24]
			elif pbone.name == 'RightShoulder':
				pbone.rotation_euler = data_rotation_body[frameSet][24: 27]
			elif pbone.name == 'RightElbow':
				pbone.rotation_euler = data_rotation_body[frameSet][27: 30]
			elif pbone.name == 'RightWrist':
				pbone.rotation_euler = data_rotation_body[frameSet][30: 33]
			elif pbone.name == 'LeftCollar':
				pbone.rotation_euler = data_rotation_body[frameSet][33: 36]
			elif pbone.name == 'LeftShoulder':
				pbone.rotation_euler = data_rotation_body[frameSet][36: 39]
			elif pbone.name == 'LeftElbow':
				pbone.rotation_euler = data_rotation_body[frameSet][39: 42]
			elif pbone.name == 'LeftWrist':
				pbone.rotation_euler = data_rotation_body[frameSet][42: 45]
			bpy.context.scene.update()
			pbone.keyframe_insert(data_path="rotation_euler" ,frame=keyFrame)
			pbone.rotation_mode = lastMode
			context.user_preferences.edit.keyframe_new_interpolation_type = keyInterp
		
	bpy.ops.object.mode_set(mode='OBJECT')
	print("Edit rotation done")
