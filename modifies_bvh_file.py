import bpy,IPython

def hello():
	print("Hello blender")

def import_bvh_file():
	bpy.ops.object.transform_apply(rotation=True)
	bpy.ops.import_anim.bvh(filepath="/home/huan/Documents_Master/InterfaceV2/two_cmu_retargeted/Suyvan_test.bvh")
