import sqlite3
from sqlite3 import Error
from IPython import embed
import Setting
 
 #query_create_tb_base_pose = CREATE TABLE `base_pose` ('id`	INTEGER,`name`	TEXT NOT NULL,`location`	TEXT NOT NULL,PRIMARY KEY(`id`));
 #query_create_tb_basic_movement = CREATE TABLE `basic_movement` (`id`	INTEGER,`base_id`	INTEGER NOT NULL,`name`	TEXT NOT NULL,`location`	TEXT NOT NULL,PRIMARY KEY(`id`));

 #tu the 1 = ('T_CHAYDAN','Chay Dan','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/TayChayDan.bvh')
 #tu the 2 = ('T_DANGHOA','Dang Hoa','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/TayDangHoa.bvh')
 #tu the 3 = ('T_DANGRUOU','Dang Ruou','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/TayDangRuou.bvh')
 #tu the 4 = ('T_CUOPBONG','Cuop Bong','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/TayCuopBong.bvh')
 #tu the 5 = ('T_TAUNHAC','Tau Nhac','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/TayTauNhac.bvh')
 #tu the 6 = ('C_CHUV','Chan Chu V','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/ChanChuV.bvh')
 #tu the 7 = ('C_CHUCHI','Chan Chu Chi','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/ChanChuChi.bvh')
 #tu the 8 = ('C_QUATRAM','Chan Qua Tram','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/ChanQuaTram.bvh')
 #tu the 9 = ('C_CHUDINH','Chan Chu Dinh','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/ChanChuDinh.bvh')
 #tu the 10 = ('C_DEMGOT','Cha Dem Got','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/ChanDemGot.bvh')
 #tu the 11 = ('C_CHONGQUY','Chan Chong Quy','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/ChanChongChanQuy.bvh')
 #tu the 12 = ('C_QUY','Hai Chan Quy','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/HaiDauGoiCungQuy.bvh')
 #tu the 13 = ('C_COMOTBEN','Chan Co Mot Ben','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/HaiChanCoVeMotBen.bvh')
 #tu the 14 = ('C_DUOITHANG','Chan Duoi Thang','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/DuoiThangHaiChan.bvh')
 #tu the 15 = ('C_BATCHEO','Chan Bat Cheo','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/HaiChanBatCheo.bvh')



def create_connection(db_file):
	""" create a database connection to the SQLite database
		specified by the db_file
	:param db_file: database file
	:return: Connection object or None
	"""
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e) 
	return None
 
 
def select_all_basics(conn, Body):
	"""
	Query all rows in the tasks table
	:param conn: the Connection object
	:return:
	"""
	cur = conn.cursor()
	cur.execute("SELECT * FROM Basic_Motions WHERE Body = ?",(Body,)) 
	rows = cur.fetchall() 
	#for row in rows:
		#print(row)
	return rows

def select_basic_movement_by_base(conn, Name_Motion, Body):
	"""
	Query basic movement by base movement id
	:param conn: the Connection object
	:param Name_Motion:
	:return:
	"""
	cur = conn.cursor()
	cur.execute("SELECT * FROM Basic_Motions WHERE Body = ? AND Name_Motion=?", (Body,Name_Motion,))	
	rows = cur.fetchall()
	return rows

def select_basic_movement_by_name(conn, Name_Motion):
	cur = conn.cursor()
	cur.execute("SELECT * FROM Basic_Motions WHERE Name_Motion = ?",(Name_Motion,))
	rows = cur.fetchall()
	return rows

def select_label_motion_by_base(conn, path_Motion):
	cur = conn.cursor()
	cur.execute("SELECT * FROM Basic_Motions WHERE Path_Motion = ?", (path_Motion,))
	row = cur.fetchall()
	return row

def add_new_base_pose(conn, new_base_pose):
	sql = ''' INSERT INTO Basic_Posture(Id_Posture,Name_Posture,Path_Motion)
			  VALUES(?,?,?) '''
	cur = conn.cursor()
	cur.execute(sql, new_base_pose)
	return cur.lastrowid

def add_new_basic_movement(conn, new_basic_movement):
	sql = ''' INSERT INTO Basic_Motions(Id_Posture, Body, Name_Motion, Path_Motion)
			  VALUES(?,?,?,?) '''
	cur = conn.cursor()
	cur.execute(sql, new_basic_movement)
	return cur.lastrowid
 
def add_new_data_upper_motion(conn, new_data):
	sql = '''INSERT INTO Data_Uppper_Motion(LabelMotion, HipsX, HipsY, HipsZ, ChestX, ChestY, ChestZ, Chest2X, Chest2Y, Chest2Z, Chest3X, Chest3Y, Chest3Z, Chest4X, Chest4Y, Chest4Z, 
						NeckX, NeckY, NeckZ, HeadX, HeadY, HeadZ, RightCollarX, RightCollarY, RightCollarZ, RightShoulderX, RightShoulderY, RightShoulderZ, RightElbowX, RightElbowY, RightElbowZ, RightWristX, RightWristY, RightWristZ,
						LeftCollarX, LeftCollarY, LeftCollarZ, LeftShoulderX, LeftShoulderY, LeftShoulderZ, LeftElbowX, LeftElbowY, LeftElbowZ, LeftWristX, LeftWristY, LeftWristZ)
			  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
	cur = conn.cursor()
	cur.execute(sql, new_data)
	return cur.lastrowid

def main():
	return {'FINISHED'}
	'''
	database = Setting.path_database
	#database = "/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/HumanStyle.db"
	#/home/Documents_Master/Style_Learning/Data_Motions/Posture/TayChayDan.bvh
	# create a database connection
	conn = create_connection(database)
	with conn:
		#new_basic_posture = ('C_BATCHEO','Chan Bat Cheo','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/HaiChanBatCheo.bvh')
		#basic_posture_id = add_new_base_pose(conn, new_basic_posture)
		#print(basic_posture_id)
		#print("1. Query basic movement by base id:")
		#select_basic_movement_by_base(conn,1)

		#new_basic_movement = (base_pose_id,'Dang Hoa','/home/name/location/danghoa.bvh')
		#basic_movement_id = add_new_basic_movement(conn, new_basic_movement)

		dataMotion = [0.006464495224380781, 0.09777148045373685, -0.118865928189321, 0.006464495224380781, 0.09777148045373685, -0.118865928189321, 0.005376123835572578, 0.0422590867136464, -0.052936247578172974,
					0.005376123399897056, 0.04225909382556424, -0.052936250287475006, 0.004240568326856715, 0.03166945910815037, -0.039717420088973915,
					0.3291529832464276, -0.19359606549595343, -0.0026189844453862556, -0.030174195851114662, -0.3544828783382069, 0.05897416513074528,
					-0.12667650164979877, 0.20063630739847818, -0.06114501009384791, -0.6526311003800594, 1.0185997594486584, 0.09863963223677163, 
					0.35361515030716406, -0.4547048518151948, 0.9637008544170496, 1.158036596847303, -0.6713826999519811, 0.7192759604165049, 
					-0.1540648318601377, -0.07880401916124603, -0.1043957124153773, -0.948996061628515, -0.7602381615927725, 0.5999973326018362, 
					0.15445910507079327, -0.2614415432467605, -0.40621712081360095, 1.0351235035694006, 0.826783400593382, -0.6419498613386443]
		#dataMotion = [0.006465, 0.097772, -0.118866, 0.006465, 0.097772, -0.118866, 0.005376, 0.042260, -0.052937, 0.005376, 0.042259, -0.052936, 0.004241, 0.031669, -0.039717, 0.329153, -0.193596, -0.002619, -0.030174, -0.354483, 0.058974, -0.126677, 0.200636, -0.061145, -0.652631, 1.018599, 0.098639, 0.353615, -0.454705, 0.963701, 1.158037, -0.671382, 0.719275, -0.154065, -0.078804, -0.104396, -0.948996, -0.760238, 0.599997, 0.154459, -0.261441, -0.4062175, 1.035123, 0.826783, -0.641949]
		Label = [1]

		newDataSqllite = (1,dataMotion[0],dataMotion[1],dataMotion[2],dataMotion[3],dataMotion[4],dataMotion[5],dataMotion[6],dataMotion[7],dataMotion[8],
						dataMotion[9],dataMotion[10],dataMotion[11],dataMotion[12],dataMotion[13],dataMotion[14],dataMotion[15],dataMotion[16],dataMotion[17],
						dataMotion[18],dataMotion[19],dataMotion[20],dataMotion[21],dataMotion[22],dataMotion[23],dataMotion[24],dataMotion[25],dataMotion[26],
						dataMotion[27],dataMotion[28],dataMotion[29],dataMotion[30],dataMotion[31],dataMotion[32],dataMotion[33],dataMotion[34],dataMotion[35],
						dataMotion[36],dataMotion[37],dataMotion[38],dataMotion[39],dataMotion[40],dataMotion[41],dataMotion[42],dataMotion[43],dataMotion[44])
		print('new data', newDataSqllite)
		databasic_id = add_new_data_upper_motion(conn, newDataSqllite)
		print("Done")
		#select_all_basics(conn) 
	'''

if __name__ == '__main__':
	main()