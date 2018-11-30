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

def Test_HMM():
	startprob = np.array([0.6, 0.3, 0.1, 0.0])
	# The transition matrix, note that there are no transitions possible
	# between component 1 and 3
	transmat = np.array([[0.7, 0.2, 0.0, 0.1],
	                     [0.3, 0.5, 0.2, 0.0],
	                     [0.0, 0.3, 0.5, 0.2],
	                     [0.2, 0.0, 0.2, 0.6]])
	# The means of each component
	means = np.array([[0.0,  0.0],
	                  [0.0, 11.0],
	                  [9.0, 10.0],
	                  [11.0, -1.0]])
	# The covariance of each component
	covars = .5 * np.tile(np.identity(2), (4, 1, 1))

	# Build an HMM instance and set parameters
	model = hmm.GaussianHMM(n_components=4, covariance_type="full")

	# Instead of fitting it from the data, we directly set the estimated
	# parameters, the means and covariance of the components
	model.startprob_ = startprob
	model.transmat_ = transmat
	model.means_ = means
	model.covars_ = covars

	# Generate samples
	X, Z = model.sample(500)

	# Plot the sampled data
	plt.plot(X[:, 0], X[:, 1], ".-", label="observations", ms=6,
	         mfc="orange", alpha=0.7)

	# Indicate the component numbers
	for i, m in enumerate(means):
	    plt.text(m[0], m[1], 'Component %i' % (i + 1),
	             size=17, horizontalalignment='center',
	             bbox=dict(alpha=.7, facecolor='w'))
	plt.legend(loc='best')
	plt.show()

data_rotation_body = []
data_rotation_foots = []
data_location_hips = []
basic_motion = []
frame_start = 1
frame_end = 1
List_Bones_Body = ['Hips', 'Chest', 'Chest2', 'Chest3', 'Chest4', 'Neck', 'Head', 'RightCollar', 'RightShoulder', 'RightElbow', 'RightWrist', 'LeftCollar', 'LeftShoulder', 'LeftElbow', 'LeftWrist']
List_Bones_Foots = ['Hips', 'RightHip', 'RightKnee', 'RightAnkle', 'RightToe', 'LeftHip', 'LeftKnee', 'LeftAnkle', 'LeftToe']
""""""""""""""""""""""""""""" Import and Export BVH file """""""""""""""""""""""""""""

def Import_Bvh(file_path):
	try:
		if not os.path.exists(file_path):
			print('File .BVH is not available.')
		bpy.ops.import_anim.bvh(filepath=file_path, axis_forward='Y',axis_up='Z', rotate_mode='NATIVE')
		with open(file_path) as f:
			global frame_end			
			mocap = Bvh(f.read())
			frame_end = mocap.nframes
		print("Importing is successful !!!")
	except:
		print("Couln't open file: {}".format(file_path))

def Export_Bvh(file_path):
	try:
		if os.path.exists(file_path):
			os.remove(file_path)		
		bpy.context.scene.render.fps = 60  # We configure the frame rate		
		bpy.ops.export_anim.bvh(filepath=file_path, global_scale = 1, frame_start= frame_start, frame_end= frame_end, rotate_mode='NATIVE', root_transform_only=True)
		print("Exporting is successful !!!")
	except:
		print("Couldn't export file")

def Delete_Bvh():
	bpy.ops.object.mode_set(mode='OBJECT')
	bpy.ops.object.delete(use_global=False)
	print ("Delete done")

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

def Kmeans_Clustering():
	K = 100
	data = Get_Data_Rotation()
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
	data = [[]]
	for label in labels:
		data.append(Centroids[label])
	data.remove([])
	data = np.array(data)	
	#smoothData = Bspline_Rotation_Data(labels, data)	
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

def Bspline_Rotation_Data(labels, data):
	#This funtion do smooth rotation data
	print("Start Bspline")
	knots_array = [[]]
	z = []
	k = 2
	for i in range(0, int(len(labels)/20)):
		z.append(i*20)
		knots_array.append(data[labels[i*20]])
	knots_array.remove([])
	knots_array = np.array(knots_array)
	#print ("knots_array: ", knots_array)
	x1 = knots_array[:, 0]
	x2 = knots_array[:, 1]
	x3 = knots_array[:, 2]
	x4 = knots_array[:, 3]
	x5 = knots_array[:, 4]
	x6 = knots_array[:, 5]
	x7 = knots_array[:, 6]
	x8 = knots_array[:, 7]
	x9 = knots_array[:, 8]

	spl_1 = BSpline(z, x1, k)
	spl_2 = BSpline(z, x2, k)
	spl_3 = BSpline(z, x3, k)
	spl_4 = BSpline(z, x4, k)
	spl_5 = BSpline(z, x5, k)
	spl_6 = BSpline(z, x6, k)
	spl_7 = BSpline(z, x7, k)
	spl_8 = BSpline(z, x8, k)
	spl_9 = BSpline(z, x9, k)
	smooth_data = []
	#spl_1_data = []
	#spl_1_ind = []
	for i in range(0, len(data)):
		#spl_1_data.append([spl_1(i)])
		#spl_1_ind.append(i)
		smooth_data.append([spl_1(i), spl_2(i), spl_3(i), spl_4(i), spl_5(i), spl_6(i), spl_7(i), spl_8(i), spl_9(i)])
	smooth_data = np.array(smooth_data)
	
	#fig, ax = plt.subplots()
	#ax.plot(spl_1_ind, spl_1_data, 'b-', lw=4, alpha=0.7, label='BSpline')
	#ax.grid(True)
	#ax.legend(loc='best')
	#plt.show()
	print('Smooth Done !!!')
	return smooth_data

def Bspline_Location_Data(data):
	# This funtion do smooth lotation data 

	data = np.array(data)
	knots_array = [[]]
	z = []
	k = 2
	for i in range(0, int(len(data)/30)):
		z.append(i*30)
		knots_array.append(data[i*30])
	knots_array.remove([])
	knots_array = np.array(knots_array)
	print ("knots_array: ", knots_array)
	x1 = knots_array[:, 0]
	x2 = knots_array[:, 1]
	x3 = knots_array[:, 2]
	x4 = knots_array[:, 3]
	x5 = knots_array[:, 4]
	x6 = knots_array[:, 5]
	spl_1 = BSpline(z, x1, k)
	spl_2 = BSpline(z, x2, k)
	spl_3 = BSpline(z, x3, k)
	spl_4 = BSpline(z, x4, k)
	spl_5 = BSpline(z, x5, k)
	spl_6 = BSpline(z, x6, k)

	_Smooth_data = []
	for i in range(0, len(data)):
		_Smooth_data.append([spl_1(i), spl_2(i), spl_3(i), spl_4(i), spl_5(i), spl_6(i)])
	_Smooth_data = np.array(_Smooth_data)
	print("Smooth data done")
	return _Smooth_data	
	""" this is plot data after smoothly
	spl_1_ind = []
	spl_1_ind.append(i)
	fig, ax = plt.subplots()
	ax.plot(spl_1_ind, spl_1_data, 'b-', lw=4, alpha=0.7, label='BSpline')
	ax.grid(True)
	ax.legend(loc='best')
	plt.show()
	"""
def Pca_Rotation(pca_components):
	# This function to loss dimention data

	data = Get_Data_Rotation()
	(U, s, Va) = pca(data, pca_components, True)
	print("U", U.shape, "s", s.shape, "Va", Va.shape)
	err = diffsnorm(data, U, s, Va)
	print('facebook pca time: error: %E' % (err))
	return np.dot(U,np.diag(s))

""""""""""""""""""""""""""""" Execute Data """""""""""""""""""""""""""""

def Get_Data_Rotation():
	# This function to get all data rotation of bones

	sce = bpy.context.scene
	ob = bpy.context.object
	ROTATION_KEY_DATA = []
	for f in range(frame_start, frame_end):
		sce.frame_set(f)
		rotation_bone = []
		for pbone in ob.pose.bones:
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

def Get_Data_Hip_Location():
	#This function to get all data lotation of bones
	
	sce = bpy.context.scene
	ob = bpy.context.object
	LOCATION_KEY_DATA = []
	for f in range(frame_start, frame_end):
		sce.frame_set(f)
		location_bone = []
		for pbone in ob.pose.bones:
			if pbone.name == "Hips":
				location_bone.extend(pbone.head)			
		LOCATION_KEY_DATA.append(location_bone)
	LOCATION_KEY_DATA = np.array(LOCATION_KEY_DATA)
	return LOCATION_KEY_DATA

def Get_data_lotation_Hips():
	global data_location_hips
	data_location_hips = Get_Data_Hip_Location()

def Edit_Data_Hips_Lotation():
	# This funtion to change lotation data of bone
	print('Shape data lotation Hips is:', data_location_hips.shape)
	sce = bpy.context.scene
	ob = bpy.context.object
	keyInterp = context.user_preferences.edit.keyframe_new_interpolation_type
	context.user_preferences.edit.keyframe_new_interpolation_type = "BEZIER"
	bpy.ops.object.mode_set(mode='EDIT')
	for f in range(frame_start, frame_end):
		sce.frame_set(f)
		keyFrame = context.scene.frame_current		
		for pbone in ob.pose.bones:			
			if pbone.name == "Hips":
				bone = ob.data.edit_bones[pbone.name]
				bone.head.x = data_location_hips[f - 1][0]
				bone.head.y = data_location_hips[f - 1][1]
				bone.head.z = data_location_hips[f - 1][2]				
			bpy.context.scene.update()
			pbone.keyframe_insert(data_path="rotation_euler" ,frame=keyFrame)
			context.user_preferences.edit.keyframe_new_interpolation_type = keyInterp
	bpy.ops.object.mode_set(mode='OBJECT')
	print("Edit location done")

def Edit_Rotation_Bone( BoneName, FrameNumber, ValueX, ValueY, ValueZ, bdegrees =True):
	sce = bpy.context.scene
	ob = bpy.context.object

	for f in range(sce.frame_start, sce.frame_end + 1):
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
