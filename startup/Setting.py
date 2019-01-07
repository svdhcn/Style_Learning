bl_info = {
	"name": "Setting file",
	"description": "",
	"author": "Huan Vu Huu",
	"version": (0, 0, 1),
	"blender": (2, 79, 0),
	"location": "3D View > Tools",
	"warning": "", # used for warning icon and text in addons panel
	"wiki_url": "",
	"tracker_url": "",
	"category": "Development"
}

path_database = "/home/huanvh/Documents/Style_Learning/HumanStyle.db"

dictMotion = {"ChayDan" : 1, "HoaSenNo" : 2, "LePhat" : 3, "QuaySoi" : 4, "BatQuyet" : 5, "DangHoa" : 6, "Bay" : 7, "RungTay" : 8, "DangLenCao" : 9, "PhayTay" : 10,
			 "ChongSuon" : 11, "DuaThoi" : 12, "VunGon" : 13, "DangRuou" : 14, "Vay" : 15, "SoiBong" :16, "RotRuou" : 17, "CheoDo" : 18, "RacDau" : 19, "DayThuyen" : 20,
			 "XeTo3" : 21, "CuopBong" :22, "DeTho" : 23, "PhuiTayAo" : 24, "LanTayAo" : 25, "GatLua" : 26, "TauNhac" : 27, "VuotToc" : 28, "Ganh" : 29, "XeTo5" : 30, "Nem" : 31,
			 "ChanChuV" : 32, "ChanChongQuy" : 33, "ChanChi" : 34, "HaiChanQuy" : 35, "ChanDinh" : 36, "NgoiMotBen" : 37, "ChanDem" : 38, "DuoiHaiChan" : 39, "ChanTram" : 40, "ChanBatCheo" : 41}

List_Motion_Upper = ["ChayDan", "HoaSenNo", "LePhat", "QuaySoi", "BatQuyet","DangHoa", "Bay", "RungTay", "DangLenCao", "PhayTay", "ChongSuon", "DuaThoi", "VunGon",
					"DangRuou", "Vay", "SoiBong", "RotRuou", "CheoDo", "RacDau", "DayThuyen", "XeTo3", "CuopBong", "DeTho", "PhuiTayAo", "LanTayAo", "GatLua",
					"VuotToc", "Ganh", "XeTo5", "Nem"]
List_Motion_Lower = ["ChanChuV", "ChanChi", "ChanTram ", "ChanDinh", "ChanDem", "ChanChongQuy", "HaiChanQuy", "NgoiMotBen", "DuoiHaiChan", "ChanBatCheo"]

List_Bone_UpperBody = ['Chest', 'Chest2', 'Chest3', 'Chest4', 'Neck', 'Head', 'RightCollar', 'RightShoulder', 'RightElbow', 'RightWrist', 'LeftCollar', 'LeftShoulder', 'LeftElbow', 'LeftWrist']
List_Bone_Lower_Body = ['RightHip', 'RightKnee', 'RightAnkle', 'RightToe', 'LeftHip', 'LeftKnee', 'LeftAnkle', 'LeftToe']

listBones = ['Hips','Chest', 'Chest2', 'Chest3', 'Chest4', 'Neck', 'Head',
			'RightCollar', 'RightShoulder', 'RightElbow', 'RightWrist', 'LeftCollar', 'LeftShoulder', 'LeftElbow', 'LeftWrist',
			'RightHip', 'RightKnee', 'RightAnkle', 'RightToe', 'LeftHip', 'LeftKnee', 'LeftAnkle', 'LeftToe']

Divide_Body = {'Upper' : 0, 'Lower' : 1}