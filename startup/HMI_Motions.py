import bpy, IPython
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
#import GPy
from scipy.interpolate import BSpline

from os import listdir
from os.path import isfile, join

from bvh import Bvh
 # lib use to HMM
import imp

import Setting
from SQL_Motions import *

frame_start = 1
frame_end = 1

""""""""""""""""""""""""""""" Machine Learning """""""""""""""""""""""""""""""""""""""
def Export_Bvh(file_path):
	try:
		if os.path.exists(file_path):
			os.remove(file_path)		
		bpy.context.scene.render.fps = 60  # We configure the frame rate		
		bpy.ops.export_anim.bvh(filepath=file_path, global_scale = 1, frame_start= frame_start, frame_end= frame_end, rotate_mode='NATIVE', root_transform_only=True)
		print("Exporting is successful !!!")
	except:
		print("Couldn't export file")

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

def Kmeans_Clustering(K, divideMotion, listPathMotions):
	# Read all File motions in data base, 
	# Get all data Rotation in .bvh file
	rotationData = []
	np.random.seed(0) # To make sure that the random seeds of K-Means algorithm are consistent	
	for pathMotion in listPathMotions:
		# Read all data rotation of motion from bvh file
		rotationData = Get_Data_Rotation_BVH_File(pathMotion, divideMotion)
		#bpy.ops.object.mode_set(mode='OBJECT')
		#bpy.ops.object.delete(use_global=False)

		# Start Clustering
		repeat = 5
		mindiff = 0.0
		labels = []
		Centroids = []	
		# begin repeat n times with k means
		for i in range(repeat):
			centroids,diff = kmeans(rotationData, K)
			if i == 0:
				mindiff = diff
				Centroids = centroids
				labels,_ = vq(rotationData,Centroids)
			elif mindiff > diff:
				mindiff = diff
				Centroids = centroids
				labels,_ = vq(rotationData,Centroids)
		#End repeat/end Cluster
		'''
		data = [[]]
		for label in labels:
			data.append(Centroids[label])
		data.remove([])
		data = np.array(data)
		'''
		######### Write data to database #############
		labelMotion = ''
		database = Setting.path_database
		conn = create_connection(database)
		with conn:
			list_label_movement = select_label_motion_by_base(conn, pathMotion)

		for i in range(0, len(list_label_movement)):
			labelMotion = list_label_movement[i][3]
		for dataMotion in Centroids:
			database = Setting.path_database
			conn = create_connection(database)
			with conn:			
				newDataSqllite = (Setting.dictMotion[labelMotion],dataMotion[0],dataMotion[1],dataMotion[2],dataMotion[3],dataMotion[4],dataMotion[5],dataMotion[6],dataMotion[7],dataMotion[8],
								dataMotion[9],dataMotion[10],dataMotion[11],dataMotion[12],dataMotion[13],dataMotion[14],dataMotion[15],dataMotion[16],dataMotion[17],
								dataMotion[18],dataMotion[19],dataMotion[20],dataMotion[21],dataMotion[22],dataMotion[23],dataMotion[24],dataMotion[25],dataMotion[26],
								dataMotion[27],dataMotion[28],dataMotion[29],dataMotion[30],dataMotion[31],dataMotion[32],dataMotion[33],dataMotion[34],dataMotion[35],
								dataMotion[36],dataMotion[37],dataMotion[38],dataMotion[39],dataMotion[40],dataMotion[41],dataMotion[42],dataMotion[43],dataMotion[44])
				databasic_id = add_new_data_upper_motion(conn, newDataSqllite)
				#print(databasic_id)

	'''
	# Export cluster in .txt file
	file = open(pathCluster, "w+")
	#file.write("Data clustering of Motion." + '\n')
	#file.write("The number of cluster is :" + str(K) + '\n')	

	for centroid in Centroids:
		for element in centroid:
			file.write(str(element) + ' ')
		file.write('\n')
	file.close()
	#smoothData = Bspline_Rotation_Data(labels, data)	
	#Export_Bvh(pathCluster)
	'''
	return {'FINISHED'}

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

def Get_Data_Rotation_BVH_File(pathMotion, divideMotion):
	ROTATION_KEY_DATA = []
	dataRotationMoverment = []
	bpy.ops.object.mode_set(mode='OBJECT')
	bpy.ops.object.delete(use_global=False)
	bpy.ops.import_anim.bvh(filepath= pathMotion, axis_forward="Y", axis_up="Z", rotate_mode="NATIVE")
	with open(pathMotion) as f:
		global frame_end
		mocap = Bvh(f.read())
		frame_end = mocap.nframes
		sce = bpy.context.scene
		ob = bpy.context.object
		if divideMotion == 0:
			for f in range(frame_start, frame_end):
				sce.frame_set(f)
				rotation_bone = []
				for pbone in ob.pose.bones:
					if pbone.name in Setting.List_Bone_Upper_Body:
						rotation_bone.extend([pbone.rotation_euler.x, pbone.rotation_euler.y ,pbone.rotation_euler.z])								
				ROTATION_KEY_DATA.append(rotation_bone)
		elif divideMotion == 1:
			for f in range(frame_start, frame_end):
				sce.frame_set(f)
				rotation_bone = []
				for pbone in ob.pose.bones:
					if pbone.name in Setting.List_Bone_Lower_Body:
						rotation_bone.extend([pbone.rotation_euler.x, pbone.rotation_euler.y ,pbone.rotation_euler.z])								
				ROTATION_KEY_DATA.append(rotation_bone)
		else:
			print("Wrong data divideMotion.")

		dataRotationMoverment = np.asarray(ROTATION_KEY_DATA)
	return dataRotationMoverment

def EditMoverment(pathBasicMotion, body, pathMotionEdit, startFrame, endFrame):
	dataRotationMoverment = Get_Data_Rotation_BVH_File(pathBasicMotion, body)
	bpy.ops.object.mode_set(mode='OBJECT')
	bpy.ops.object.delete(use_global=False)
	bpy.ops.import_anim.bvh(filepath= pathMotionEdit, axis_forward="Y", axis_up="Z", rotate_mode="NATIVE")
	IPython.embed()
	if body == 0:
		EditUpperRotation(dataRotationMoverment, startFrame, endFrame)
	elif body == 1:
		EditLowerRotation(dataRotationMoverment, startFrame, endFrame)
	else:
		Print("Wrong data of Body Motion.")
	return {"FINISHED"}

def EditLowerRotation(dataRotationMoverment, startFrame, endFrame):
	# This funtion to change rotation Foots data of bone
	#data = Kmeans_Clustering()	
	print('Shape data rotation foots is:', dataRotationMoverment.shape)
	sce = bpy.context.scene
	ob = bpy.context.object	
	bpy.ops.object.mode_set(mode='POSE')
	#frame_end_change = dataRotationMoverment.shape[0]
	for f in range(startFrame, endFrame):
		frameSet = f - 1
		sce.frame_set(f)
		keyFrame = context.scene.frame_current
		keyInterp = context.user_preferences.edit.keyframe_new_interpolation_type
		context.user_preferences.edit.keyframe_new_interpolation_type = "BEZIER"
		for pbone in ob.pose.bones:
			lastMode = pbone.rotation_mode
			pbone.rotation_mode = "XYZ"
			pbone.bone.select = True
			if pbone.name not in Setting.List_Bone_Lower_Body:
				continue
			if pbone.name == 'Hips':
				continue		
			if pbone.name == "RightHip":
				pbone.rotation_euler = dataRotationMoverment[frameSet][3:6]
			elif pbone.name == "RightKnee":
				pbone.rotation_euler = dataRotationMoverment[frameSet][6:9]
			elif pbone.name == "RightAnkle":
				pbone.rotation_euler = dataRotationMoverment[frameSet][9:12]
			elif pbone.name == "RightToe":
				pbone.rotation_euler = dataRotationMoverment[frameSet][12:15]
			elif pbone.name == "LeftHip":
				pbone.rotation_euler = dataRotationMoverment[frameSet][15:18]
			elif pbone.name == "LeftKnee":
				pbone.rotation_euler = dataRotationMoverment[frameSet][18:21]
			elif pbone.name == "LeftAnkle":
				pbone.rotation_euler = dataRotationMoverment[frameSet][21:24]
			elif pbone.name == "LeftToe":
				pbone.rotation_euler = dataRotationMoverment[frameSet][24:27]
			bpy.context.scene.update()
			pbone.keyframe_insert(data_path="rotation_euler" ,frame=keyFrame)
			pbone.rotation_mode = lastMode
			context.user_preferences.edit.keyframe_new_interpolation_type = keyInterp
			#IPython.embed()
	bpy.ops.object.mode_set(mode='OBJECT')
	print("Edit lower rotation done")	

def EditUpperRotation(dataRotationMoverment, startFrame, endFrame):
	# This funtion to change rotation data of bone
	print('Shape data rotation foots is:', dataRotationMoverment.shape)

	sce = bpy.context.scene
	ob = bpy.context.object	
	bpy.ops.object.mode_set(mode='POSE')
	frame_end_change = dataRotationMoverment.shape[0]
	for f in range(startFrame, endFrame):
		frameSet = f
		sce.frame_set(f)
		sce.frame_set(frameSet)
		keyFrame = context.scene.frame_current
		keyInterp = context.user_preferences.edit.keyframe_new_interpolation_type
		context.user_preferences.edit.keyframe_new_interpolation_type = "BEZIER"
		for pbone in ob.pose.bones:
			lastMode = pbone.rotation_mode
			pbone.rotation_mode = "XYZ"
			pbone.bone.select = True
			if pbone.name not in Setting.List_Bone_Upper_Body:
				continue
			if pbone.name == 'Hips':
				continue
			elif pbone.name == 'Chest':
				pbone.rotation_euler = dataRotationMoverment[frameSet][3: 6]
			elif pbone.name == 'Chest2':
				pbone.rotation_euler = dataRotationMoverment[frameSet][6: 9]
			elif pbone.name =='Chest3':
				pbone.rotation_euler = dataRotationMoverment[frameSet][9: 12]
			elif pbone.name == 'Chest4':
				pbone.rotation_euler = dataRotationMoverment[frameSet][12: 15]
			elif pbone.name == 'Neck':
				pbone.rotation_euler = dataRotationMoverment[frameSet][15: 18]
			elif pbone.name == 'Head':
				pbone.rotation_euler = dataRotationMoverment[frameSet][18: 21]
			elif pbone.name == 'RightCollar':
				pbone.rotation_euler = dataRotationMoverment[frameSet][21: 24]
			elif pbone.name == 'RightShoulder':
				pbone.rotation_euler = dataRotationMoverment[frameSet][24: 27]
			elif pbone.name == 'RightElbow':
				pbone.rotation_euler = dataRotationMoverment[frameSet][27: 30]
			elif pbone.name == 'RightWrist':
				pbone.rotation_euler = dataRotationMoverment[frameSet][30: 33]
			elif pbone.name == 'LeftCollar':
				pbone.rotation_euler = dataRotationMoverment[frameSet][33: 36]
			elif pbone.name == 'LeftShoulder':
				pbone.rotation_euler = dataRotationMoverment[frameSet][36: 39]
			elif pbone.name == 'LeftElbow':
				pbone.rotation_euler = dataRotationMoverment[frameSet][39: 42]
			elif pbone.name == 'LeftWrist':
				pbone.rotation_euler = dataRotationMoverment[frameSet][42: 45]
			bpy.context.scene.update()
			pbone.keyframe_insert(data_path="rotation_euler" ,frame=keyFrame)
			pbone.rotation_mode = lastMode
			context.user_preferences.edit.keyframe_new_interpolation_type = keyInterp
		
	bpy.ops.object.mode_set(mode='OBJECT')
	print("Edit upper rotation done")
