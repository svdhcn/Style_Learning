import IPython
import math
from os import listdir
from os.path import isfile, join
import glob, os
import numpy as np
import pandas as pd

List_Bones_UpperBody = ['Hips','Chest', 'Chest2', 'Chest3', 'Chest4', 'Neck', 'Head', 'RightCollar', 'RightShoulder', 'RightElbow', 'RightWrist', 'LeftCollar', 'LeftShoulder', 'LeftElbow', 'LeftWrist', 'RightHip', 'RightKnee', 'RightAnkle', 'RightToe', 'LeftHip', 'LeftKnee', 'LeftAnkle', 'LeftToe']
		

def get_text_files_data():
	os.getcwd()
	os.chdir('..')
	path = os.getcwd() +'/Clusterring'
	text_data = []
	os.chdir(path)
	for file in glob.glob("*.txt"):
		text_data.append(path + '/'+ file)
	return text_data

def write_data_to_dataFrame():
	List_Bones = ['Hips','Chest', 'Chest2', 'Chest3', 'Chest4', 'Neck', 'Head',
				'RightCollar', 'RightShoulder', 'RightElbow', 'RightWrist', 'LeftCollar', 'LeftShoulder', 'LeftElbow', 'LeftWrist',
				'RightHip', 'RightKnee', 'RightAnkle', 'RightToe', 'LeftHip', 'LeftKnee', 'LeftAnkle', 'LeftToe']
	
	Bones_Body = np.array(List_Bones)
	DataMotion = pd.DataFrame(columns= Bones_Body)
	fname = ''
	textData = get_text_files_data()
	for data in textData:
		fname = data.split('\\')[-1:][-1]
		f = open(data, 'r' )
		for i in range(0,50):
			s = f.readline()
			IPython.embed()
	return {'FINISHED'}

d = write_data_to_dataFrame()