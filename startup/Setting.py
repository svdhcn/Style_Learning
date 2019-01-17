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

Dict_Motion = {1: "ChayDan", 2 : "HoaSenNo", 3 : "LePhat", 4 : "QuaySoi", 5 : "BatQuyet", 6 : "DangHoa", 7 : "Bay", 8 : "RungTay", 9 : "DangLenCao", 10 : "PhayTay",
		11 : "ChongSuon", 12 : "DuaThoi", 13 : "VunGon", 14 : "DangRuou", 15 : "Vay", 16 : "SoiBong", 17 : "RotRuou", 18 : "CheoDo", 19 : "RacDau", 20 : "DayThuyen",
		21 : "XeTo3", 22 : "CuopBong", 23 : "DeTho", 24 : "PhuiTayAo", 25 : "LanTayAo", 26 : "GatLua", 27 : "TauNhac", 28 : "VuotToc", 29 : "Ganh", 30 : "XeTo5", 31 : "Nem",
		32 : "ChanChuChiNam", 33 : "ChanChuChiNu", 34 : "ChanChongQuy", 35 : "ChanChuDinh", 36 : "ChanDemGot", 37 : "HaiChanQuy", 38 : "ChanNuLech", 39 : "ChanNamNgang", 40 : "NgoiMotBen", 
		41 : "ChanQuaTram", 42 : "ChanLaoSay", 43 : "ChanBatCheo", 44 : "ChanKhongLuuNam", 45 : "ChanKhongLuuNu", 46 : "ChanXien", 47 : "ChanDuoiThang" }

dictMotion = {"ChayDan" : 1, "HoaSenNo" : 2, "LePhat" : 3, "QuaySoi" : 4, "BatQuyet" : 5, "DangHoa" : 6, "Bay" : 7, "RungTay" : 8, "DangLenCao" : 9, "PhayTay" : 10,
			 "ChongSuon" : 11, "DuaThoi" : 12, "VunGon" : 13, "DangRuou" : 14, "Vay" : 15, "SoiBong" :16, "RotRuou" : 17, "CheoDo" : 18, "RacDau" : 19, "DayThuyen" : 20,
			 "XeTo3" : 21, "CuopBong" :22, "DeTho" : 23, "PhuiTayAo" : 24, "LanTayAo" : 25, "GatLua" : 26, "TauNhac" : 27, "VuotToc" : 28, "Ganh" : 29, "XeTo5" : 30, "Nem" : 31,
			 "ChanChuChiNam" : 32, "ChanChuChiNu" : 33, "ChanChongQuy" : 34, "ChanChuDinh" : 35, "ChanDemGot" : 36, "HaiChanQuy" : 37, "ChanNuLech" : 38, "ChanNamNgang" : 39, "NgoiMotBen" : 40,
			 "ChanQuaTram" : 41, "ChanLaoSay" : 42, "ChanBatCheo" : 43, "ChanKhongLuuNam" : 44, "ChanKhongLuuNu" : 45, "ChanXien" : 46, "ChanDuoiThang" : 47}

List_Motion_Upper = ["ChayDan", "HoaSenNo", "LePhat", "QuaySoi", "BatQuyet","DangHoa", "Bay", "RungTay", "DangLenCao", "PhayTay", "ChongSuon", "DuaThoi", "VunGon",
					"DangRuou", "Vay", "SoiBong", "RotRuou", "CheoDo", "RacDau", "DayThuyen", "XeTo3", "CuopBong", "DeTho", "PhuiTayAo", "LanTayAo", "GatLua",
					"VuotToc", "Ganh", "XeTo5", "Nem"]
List_Motion_Lower = ["ChanChuChiNam", "ChanChuChiNu", "ChanChongQuy", "ChanChuDinh", "ChanDemGot", "HaiChanQuy", "ChanNuLech", "ChanNamNgang", "NgoiMotBen", 
					"ChanQuaTram", "ChanLaoSay", "ChanBatCheo", "ChanKhongLuuNam", "ChanKhongLuuNu", "ChanXien", "ChanDuoiThang"]

List_Bone_Upper_Body = ['Hips','Chest', 'Chest2', 'Chest3', 'Chest4', 'Neck', 'Head', 'RightCollar', 'RightShoulder', 'RightElbow', 'RightWrist', 'LeftCollar', 'LeftShoulder', 'LeftElbow', 'LeftWrist']
List_Bone_Lower_Body = ['Hips','RightHip', 'RightKnee', 'RightAnkle', 'RightToe', 'LeftHip', 'LeftKnee', 'LeftAnkle', 'LeftToe']

listBones = ['Hips','Chest', 'Chest2', 'Chest3', 'Chest4', 'Neck', 'Head',
			'RightCollar', 'RightShoulder', 'RightElbow', 'RightWrist', 'LeftCollar', 'LeftShoulder', 'LeftElbow', 'LeftWrist',
			'RightHip', 'RightKnee', 'RightAnkle', 'RightToe', 'LeftHip', 'LeftKnee', 'LeftAnkle', 'LeftToe']

Divide_Body = {'Upper' : 0, 'Lower' : 1}