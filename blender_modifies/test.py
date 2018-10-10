import blender_modifies

blender_modifies.Import_Bvh("/home/huan/Documents_Master/InterfaceV2/two_cmu_retargeted/Hand_Modified/Hand_Suyvan_data.bvh")
blender_modifies.Get_Data_Rotation()
blender_modifies.K_means_clustering(5)
#blender_modifies.Edit_Rotation_Bone("RightShoulder", 1, #)

#blender_modifies.Get_Data_Rotation()
#blender_modifies.Rotation_Bone("RightShoulder", 1 , 10, 20, -15)
#blender_modifies.Export_Bvh("/home/huan/Document#