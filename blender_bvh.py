import bpy

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
    return vector / np.linalg.norm(vector)

def angle_between_vector(v1, v2, n):
    # v1_u = unit_vector(v1)
    # v2_u = unit_vector(v2)
    # print "v1: ", v1, " | v1_u: ", v1_u
    # print "v2: ", v2, " | v2_u: ", v2_u
    # # return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    # return (np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))/np.pi)*180
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
    
    
if __name__ == '__main__':

    
    # Begin
    ListJoints, idLimb, idCoupling = read_config('E:/hmi/thay long/InterfaceV2/Config')
    print(idLimb)
    print(idCoupling)

    file_path = 'E:/hmi/thay long/InterfaceV2/two_cmu_retargeted/No-001.bvh'
    bpy.ops.import_anim.bvh(filepath=file_path,
                    axis_forward='-Z', axis_up='Y', filter_glob="*.bvh",
                    target='ARMATURE', global_scale=1.0, frame_start=1,
                    use_fps_scale=False, update_scene_fps=False,
                    update_scene_duration=False, use_cyclic=False,
                    rotate_mode='NATIVE')
    #bpy.context.scene.render.fps = 72
    bpy.context.scene.objects.active = ob
    bpy.ops.object.mode_set(mode='POSE')
    sce = bpy.context.scene
    footRight = bpy.data.objects["Armature"].data.bones["ikHeelRight"]
    #animations = list(bpy.data.actions)
    
    for f in range(sce.frame_start, sce.frame_end+1):
        footRight.select = True
        footRight.head +=Vector((1,1,0))
        footRight.tail +=Vector((1,1,0))
            
    # We export the file with the appropriate settings
    #bpy.ops.export_anim.bvh(
        # filepath=file_path + '_exported.bvh',
        # check_existing=True, filter_glob="*.bvh",
        # global_scale=1.0, frame_start=1, frame_end=1515,
        # rotate_mode='XYZ', root_transform_only=True)