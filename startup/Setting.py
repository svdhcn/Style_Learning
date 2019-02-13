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

Dict_Motion = {1: "ChayDan", 2 : "HoaSenNo", 3 : "LePhat", 4 : "QuaySoi", 5 : "DangHoa", 6 : "Bay", 7 : "RungTay", 8 : "DangLenCao", 9 : "PhayTay",
		10 : "ChongSuon", 11 : "DuaThoi", 12 : "VunGon", 13 : "DangRuou", 14 : "Vay", 15 : "SoiBong", 16 : "RotRuou", 17 : "CheoDo", 18 : "RacDau", 19 : "DayThuyen",
		20 : "XeTo3", 21 : "CuopBong", 22 : "DeTho", 23 : "PhuiTayAo", 24 : "LanTayAo", 25 : "GatLua", 26 : "TauNhac", 27 : "VuotToc", 28 : "Ganh", 29 : "XeTo5", 30 : "Nem",
		31 : "ChanChuChiNam", 32 : "ChanChuChiNu", 33 : "ChanChongQuy", 34 : "ChanChuDinh", 35 : "ChanDemGot", 36 : "HaiChanQuy", 37 : "ChanNuLech", 38 : "ChanNamNgang", 39 : "NgoiMotBen", 
		40 : "ChanQuaTram", 41 : "ChanLaoSay", 42 : "ChanBatCheo", 43 : "ChanKhongLuuNam", 44 : "ChanKhongLuuNu", 45 : "ChanXien", 46 : "ChanDuoiThang" }

dictMotion = {"ChayDan" : 1, "HoaSenNo" : 2, "LePhat" : 3, "QuaySoi" : 4, "DangHoa" : 5, "Bay" : 6, "RungTay" : 7, "DangLenCao" : 8, "PhayTay" : 9,
			 "ChongSuon" : 10, "DuaThoi" : 11, "VunGon" : 12, "DangRuou" : 13, "Vay" : 14, "SoiBong" :15, "RotRuou" : 16, "CheoDo" : 17, "RacDau" : 18, "DayThuyen" : 19,
			 "XeTo3" : 20, "CuopBong" :21, "DeTho" : 22, "PhuiTayAo" : 23, "LanTayAo" : 24, "GatLua" : 25, "TauNhac" : 26, "VuotToc" : 27, "Ganh" : 28, "XeTo5" : 29, "Nem" : 30,
			 "ChanChuChiNam" : 31, "ChanChuChiNu" : 32, "ChanChongQuy" : 33, "ChanChuDinh" : 34, "ChanDemGot" : 35, "HaiChanQuy" : 36, "ChanNuLech" : 37, "ChanNamNgang" : 38, "NgoiMotBen" : 39,
			 "ChanQuaTram" : 40, "ChanLaoSay" : 41, "ChanBatCheo" : 42, "ChanKhongLuuNam" : 43, "ChanKhongLuuNu" : 44, "ChanXien" : 45, "ChanDuoiThang" : 46}

List_Motion_Upper = ["ChayDan", "HoaSenNo", "LePhat", "QuaySoi","DangHoa", "Bay", "RungTay", "DangLenCao", "PhayTay", "ChongSuon", "DuaThoi", "VunGon",
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

Motion_Upper = {"ChayDan" : 1, "HoaSenNo" : 2, "LePhat" : 3, "QuaySoi" : 4, "DangHoa" : 5, "Bay" : 6, "RungTay" : 7, "DangLenCao" : 8, "PhayTay" : 9,
			 	"ChongSuon" : 10, "DuaThoi" : 11, "VunGon" : 12, "DangRuou" : 13, "Vay" : 14, "SoiBong" :15, "RotRuou" : 16, "CheoDo" : 17, "RacDau" : 18, "DayThuyen" : 19,
			 	"XeTo3" : 20, "CuopBong" :21, "DeTho" : 22, "PhuiTayAo" : 23, "LanTayAo" : 24, "GatLua" : 25, "TauNhac" : 26, "VuotToc" : 27, "Ganh" : 28, "XeTo5" : 29, "Nem" : 30,}