import bpy,IPython
import math
import pdb


def import_bvh(file_path):
	try:		
		bpy.ops.import_anim.bvh(filepath=file_path, axis_forward='Y',axis_up='Z', rotate_mode='NATIVE')
	except:
		print("Couldn't open file: {}".format(file_path))

def export_bvh():
	try:				
		bpy.context.scene.render.fps = 20  # We configure the frame rate		
		bpy.ops.export_anim.bvh(filepath="/home/huan/Documents_Master/InterfaceV2/two_cmu_retargeted/bvh_modified/suyvan_03.bvh",frame_start=1, frame_end=250, rotate_mode='NATIVE', root_transform_only=True)	
	except:
		print("Couldn't export file")

# get keyframes of object list
def get_keyframes(obj_list):
    keyframes = []
    for obj in obj_list:
        anim = obj.animation_data
        if anim is not None and anim.action is not None:
            for fcu in anim.action.fcurves:
                for keyframe in fcu.keyframe_points:
                    x, y = keyframe.co
                    if x not in keyframes:
                        keyframes.append((math.ceil(x)))
    return keyframes

def Key_Frame_Points(): #Gets the key-frame values as an array.
    KEYFRAME_POINTS_ARRAY = []
    # selection = bpy.context.selected_objects
    fcurves = bpy.context.active_object.animation_data.action.fcurves
    for curve in fcurves:
        IPython.embed()
        keyframePoints = curve.keyframe_points
        for keyframe in keyframePoints:
            KEYFRAME_POINTS_ARRAY.append(round(keyframe.co[1],6))
    print(KEYFRAME_POINTS_ARRAY)
    return KEYFRAME_POINTS_ARRAY