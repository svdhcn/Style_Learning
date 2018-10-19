import re
import numpy as np
import sys
import scipy
import IPython
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from scipy.interpolate import BSpline

def read_data_rotation():
    ROTATION_KEY_DATA = []
    f = open("/home/huan/Documents_Master/Style_Learning/DataRotation.txt", "r")
    reader = csv.reader(f, delimiter=",")
    for line in reader:
        loc_ = Point(float(line[0]), float(line[1]))  #tuples for location
        geo_locs.append(loc_)
    ROTATION_KEY_DATA = np.array(ROTATION_KEY_DATA)
    return ROTATION_KEY_DATA

def kmeans_clustering(X, clusters):
    kmeans = KMeans(n_clusters=clusters, random_state=0).fit(X)
    print('Centers found by scikit-learn:')
    print(kmeans.cluster_centers_)
    pred_label = kmeans.predict(X)
    print(pred_label)    