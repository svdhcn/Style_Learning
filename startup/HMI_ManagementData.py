import IPython
import math
from os import listdir
from os.path import isfile, join
import glob, os
import numpy as np
import pandas as pd	
import Setting

'''
def get_text_files_data():
	os.getcwd()
	os.chdir('..')
	path = os.getcwd() +'/Clusterring'
	text_data = []
	os.chdir(path)
	for file in glob.glob("*.txt"):
		text_data.append(path + '/'+ file)
	return text_data

def update_data_to_dataFrame():
	List_Bones = Setting.listBones
	
	Bones_Body = np.array(List_Bones)	
	fname = ''
	textData = get_text_files_data()
	df = pd.DataFrame(columns= List_Bones)
	for data in textData:
		fname = data.split('\\')[-1:][-1]
		filename_w_ext = os.path.basename(fname)
		filename, file_extension = os.path.splitext(filename_w_ext)
	return {'FINISHED'}

d = update_data_to_dataFrame()
'''