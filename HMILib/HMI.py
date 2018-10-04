import re
import numpy as np
import sys

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from scipy.interpolate import BSpline
from plot_figure import PlotFigure

def read_config(filename):
    f = open(filename, "r")
    X, Y, Z = 10, 8, 2;
    ListJoints = [[[] for y in range(Y)] for z in range(Z)]
    idLimb = 0
    idCoupling = 0
    typeJoint = 0
    for line in f:
        if "LIMBS" in line:
            typeJoint = 0
            continue
        elif "COUPLINGS" in line:
            typeJoint = 1
            continue
        else:
            itemsmatch = line.strip().split(' ')
            if typeJoint==0:
                ListJoints[typeJoint][idLimb] = itemsmatch
                idLimb+=1
            else:
                ListJoints[typeJoint][idCoupling] = itemsmatch
                idCoupling+=1
    return (ListJoints, idLimb, idCoupling)

def unit_vector(vector):
	## Normalize @vector
    return vector / np.linalg.norm(vector)

def angle_between_vector(v1, v2, n):
	## Calculate angle between 2 vectors.
	## @v1: first vector
	## @v2: second vector
	## @n: 
    x1 = v1[0]
    y1 = v1[1]
    z1 = v1[2]

    x2 = v2[0]
    y2 = v2[1]
    z2 = v2[2]

    xn = n[0]
    yn = n[1]
    zn = n[2]

    dot = x1*x2 + y1*y2 + z1*z2
    det = x1*y2*zn + x2*yn*z1 + xn*y1*z2 - z1*y2*xn - z2*yn*x1 - zn*y1*x2
    angle = (np.arctan2(det, dot)/np.pi)*180
    if angle < 0:
    	angle = 360 + angle
    return angle

def isRotationMatrix(R):
	## Checks if a matrix is a valid rotation matrix.
	## @R: matrix
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype = R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6

def rotationMatrixToEulerAngles(R):
    ## Calculates rotation matrix to euler angles
    ## The result is the same as MATLAB except the order
    ## of the euler angles ( x and z are swapped ).
    assert(isRotationMatrix(R))
     
    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
     
    singular = sy < 1e-6
 
    if  not singular :
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])
    else :
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0
 
    return np.array([x, y, z])

def Polar_To_Descartes(RootX, RootY, RootZ, Length, AlphaZ, AlphaXY):
    AlphaXY = (AlphaXY/180)*np.pi
    AlphaZ = (AlphaZ/180)*np.pi
    z = Length * np.cos(AlphaZ) + RootZ
    lenxy = Length * np.sin(AlphaZ)
    x = lenxy * np.cos(AlphaXY) + RootX
    y = lenxy * np.sin(AlphaXY) + RootY
    return (x, y, z)

def Descartes_To_Polar(X, Y, Z):
    AlphaZ = angle_between_vector([0, 0, 1], [X, Y, Z], [-Y, X, 0])
    AlphaXY = angle_between_vector([X, Y, 0], [1, 0, 0], [0, 0, 1])
    x = np.array([AlphaXY, AlphaZ])
    return x

def angle_of_vectors(listvector):
    s = len(listvector)
    vector_angle = []
    rootangle = Descartes_To_Polar(listvector[0][0], listvector[0][1], listvector[0][2])
    for i in range (1, s):
        tempangle = Descartes_To_Polar(listvector[i][0], listvector[i][1], listvector[i][2])
        angle = tempangle - rootangle
        rootangle = tempangle
        vector_angle.append(angle[0])
        vector_angle.append(angle[1])
    return vector_angle

def points_to_vectors(listpoint, global_positions, nframe):
    s = len(listpoint)
    listvector = []
    for i in range(0, s-1):
        listvector.append(global_positions[nframe][listpoint[i+1]] - global_positions[nframe][listpoint[i]])
    return listvector

def preview_motion(anglearr, lengtharr=[]):
    joint_position = [[0, 0, 0]]
    AlpXY = 270
    AlpZ = 90
    length_egde = 1
    if len(anglearr)/2 == len(lengtharr)-1:
        length_egde = lengtharr[0]
        joint_position.append([0, length_egde, 0])
        for i in range (0, len(anglearr)/2):
            length_egde = lengtharr[1+i]
            AlpZ = AlpZ + anglearr[2*i]
            AlpXY = AlpXY + anglearr[2*i + 1]
            x, y, z = Polar_To_Descartes(joint_position[1+i][0], joint_position[1+i][1], joint_position[1+i][2], length_egde, AlpZ, AlpXY)
            joint_position.append([x, y, z])
    else:
        joint_position.append([0, length_egde, 0])
        for i in range (0, len(anglearr)/2):
            # print "Vector ", i, ": AlpXY = ", AlpXY, " | AlpZ = ", AlpZ, " | anglearr = ",  anglearr[2*i], " | ",  anglearr[2*i + 1]
            AlpXY = AlpXY + anglearr[2*i + 0]
            AlpZ = AlpZ + anglearr[2*i + 1]
            x, y, z = Polar_To_Descartes(joint_position[1+i][0], joint_position[1+i][1], joint_position[1+i][2], length_egde, AlpZ, AlpXY)
            # print "x, y, z = ", x, ", ", y, ", ", z
            joint_position.append([x, y, z])
    return joint_position

def plot_preview(data, index_plt):
	te =[]
	Pos = np.array(preview_motion(data, te))

	# print ("Pos: ", Pos)

	fig1 = plt.figure(index_plt)
	ax = Axes3D(fig1, rect=[0, 0, .95, 1], elev=48, azim=134)
	ax.plot(Pos[:, 0], Pos[:, 1], Pos[:, 2])

	# Make legend, set axes limits and labels
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	tittle = 'Centroid ' + str(index_plt)
	ax.set_title(tittle)
	ax.dist = 12
