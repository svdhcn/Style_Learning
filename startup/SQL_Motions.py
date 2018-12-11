import sqlite3
from sqlite3 import Error
 
 #query_create_tb_base_pose = CREATE TABLE `base_pose` ('id`	INTEGER,`name`	TEXT NOT NULL,`location`	TEXT NOT NULL,PRIMARY KEY(`id`));
 #query_create_tb_basic_movement = CREATE TABLE `basic_movement` (`id`	INTEGER,`base_id`	INTEGER NOT NULL,`name`	TEXT NOT NULL,`location`	TEXT NOT NULL,PRIMARY KEY(`id`));

 #tu the 1 = ('Chan hinh chu V ', '/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/TuThe/Chan/ChanChuV.bvh')
 #tu the 2 = ('Chu chi','/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/TuThe/Chan/ChanNuLechNamNgang.bvh')
 #tu the 3 = ('Qua tram','/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/TuThe/Chan/ChanQuaTramLaoSay.bvh')
 #tu the 4 = ('Chu Dinh','/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/TuThe/Chan/ChanChuDinh.bvh')
 #tu the 5 = ('Dem got','/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/TuThe/Chan/ChanQuayKhongLuuNamNu.bvh')
 #tu the 6 = ('Dang hoa','')
 #tu the 7 = ('Dang hoa','')
 #tu the 8 = ('Dang hoa','')
 #tu the 9 = ('Dang hoa','')
 #tu the 10 = ('Dang hoa','')
 #tu the 11 = ('Dang hoa','')



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
    sql = ''' INSERT INTO base_pose(name,path)
              VALUES(?,?) '''
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
    database = "/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/dance.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        new_base_pose = ('Dem got','/home/khmt/Documents/KHMT_MOTIONS/Style_Learning/TuThe/Chan/ChanQuayKhongLuuNamNu.bvh')
        base_pose_id = add_new_base_pose(conn, new_base_pose)
        print(base_pose_id)
        print("1. Query basic movement by base id:")
        select_basic_movement_by_base(conn,1)

        new_basic_movement = (base_pose_id,'Dang Hoa','/home/name/location/danghoa.bvh')
        #basic_movement_id = add_new_basic_movement(conn, new_basic_movement)
 
        print("2. Query all basic movements")
        select_all_basics(conn)

 
 
if __name__ == '__main__':
    main()