import blender_modifies

blender_modifies.Import_Bvh("/home/huan/Documents_Master/InterfaceV2/two_cmu_retargeted/Hand_Modified/Hand_Suyvan_data.bvh")
#blender_modifies.Get_Data_Rotation()
#blender_modifies.pca_rotation(3)
blender_modifies.Edit_data()
blender_modifies.Export_Bvh("/home/huan/Documents_Master/InterfaceV2/two_cmu_retargeted/Hand_Modified/Hand_Suyvan_Export.bvh")