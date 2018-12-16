import sqlite3
from sqlite3 import Error
 
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
 
 
def select_all_basics(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM base_pose")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_basic_movement_by_base(conn, base_id):
    """
    Query basic movement by base movement id
    :param conn: the Connection object
    :param base_id:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM basic_movement WHERE base_id=?", (base_id,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

def add_new_base_pose(conn, new_base_pose):
    sql = ''' INSERT INTO Basic_Posture(Id_Posture,Name_Posture,path)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, new_base_pose)
    return cur.lastrowid

def add_new_basic_movement(conn, new_basic_movement):
    sql = ''' INSERT INTO basic_movement(base_id, name, path)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, new_basic_movement)
    return cur.lastrowid
 
 
def main():
    database = "/home/huan/Documents_Master/Style_Learning/HumanStyle.db"

    #/home/Documents_Master/Style_Learning/Data_Motions/Posture/TayChayDan.bvh
    # create a database connection
    conn = create_connection(database)
    with conn:
        new_basic_posture = ('C_BATCHEO','Chan Bat Cheo','/home/huan/Documents_Master/Style_Learning/Data_Motions/Posture/HaiChanBatCheo.bvh')
        basic_posture_id = add_new_base_pose(conn, new_basic_posture)
        print(basic_posture_id)
        #print("1. Query basic movement by base id:")
        #select_basic_movement_by_base(conn,1)

        #new_basic_movement = (base_pose_id,'Dang Hoa','/home/name/location/danghoa.bvh')
        #basic_movement_id = add_new_basic_movement(conn, new_basic_movement)
 
        #print("2. Query all basic movements")
        #select_all_basics(conn)

 
 
if __name__ == '__main__':
    main()