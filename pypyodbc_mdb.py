#导入模块
import pypyodbc
import Gbk2Big5

#定义conn
def mdb_conn(db_name, password = ""):
    """
    功能：创建数据库连接
    :param db_name: 数据库名称
    :param db_name: 数据库密码，默认为空
    :return: 返回数据库连接
    """
    str = 'Driver={Microsoft Access Driver (*.mdb)};PWD' + password + ";DBQ=" + db_name
    conn = pypyodbc.win_connect_mdb(str)

    return conn

#增加记录
def mdb_add(conn, cur, sql):
    """
    功能：向数据库插入数据
    :param conn: 数据库连接
    :param cur: 游标
    :param sql: sql语句
    :return: sql语句是否执行成功
    """
    try:
        cur.execute(sql)
        conn.commit()
        return True
    except:
        return False

#删除记录
def mdb_del(conn, cur, sql):
    """
    功能：向数据库删除数据
    :param conn: 数据库连接
    :param cur: 游标
    :param sql: sql语句
    :return: sql语句是否执行成功
    """
    try:
        cur.execute(sql)
        conn.commit()
        return True
    except:
        return False

#修改记录
def mdb_modi(conn, cur, sql):
    """
    功能：向数据库修改数据
    :param conn: 数据库连接
    :param cur: 游标
    :param sql: sql语句
    :return: sql语句是否执行成功
    """
    try:
        cur.execute(sql)
        conn.commit()
        return True
    except:
        return False

#查询记录
def mdb_sel(cur, sql):
    """
    功能：向数据库查询数据
    :param cur: 游标
    :param sql: sql语句
    :return: 查询结果集
    """
    try:
        cur.execute(sql)
        return cur.fetchall()
    except:
        return []

#获取表名列表
def mdb_table_list(cur):
    table_list = []  # 获取数据库所有表名
    for table_info in cur.tables(tableType='TABLE'):
        table_list.append(table_info[2])
    # print(table_list)
    return table_list

def mdb_modi_mu(cur, tablename):
    #批量简转繁
    sql = "SELECT * FROM " + tablename + " "
    sel_data = mdb_sel(cur, sql)
    # print(sel_data)

    for i in sel_data:
        # print(i)
        # print(i[0])
        head = ""  # sql语句中对应的列信息
        for a in i.cursor_description:
            # print(a[0])
            if len(head) != 0:
                head = head + " , "
            head = head + str(a[0])  # sql语句中对应的列信息
        line_list = []
        for j in i:
            line_list.append(str(Gbk2Big5.Gbk2Big5(str(j))))
        sql_str = "" # 简转繁后的字符串
        for k in line_list:
            if len(sql_str) != 0:
                sql_str = sql_str + ", "
            str_k = str(k)
            if str_k == 'None':
                str_k = "''"
            # else:
            #     str_k = "'" + str_k + "'"

            sql_str = sql_str + str_k

        #删
        sql = "Delete FROM " + tablename + " where ID = " + str(i[0])
        if mdb_del(conn, cur, sql):
           print("删除成功！")
        else:
           print("删除失败！")

        #增
        sql = "Insert Into " + tablename + " (" + head + ") Values " + " (" + str(sql_str) + ")"
        # print(sql)
        if mdb_add(conn, cur, sql):
           print("插入成功！")
        else:
           print("插入失败！")

if __name__ == '__main__':
    pathfile = './kitdat/CabinetDrawer.mdb'
    tablename = 'Drawer'
    conn = mdb_conn(pathfile)  # 创建数据库连接
    cur = conn.cursor() # 创建游标

    # #增
    # sql = "Insert Into " + tablename + " (id , drawerGroup) Values ('6799', '31')"
    # if mdb_add(conn, cur, sql):
    #    print("插入成功！")
    # else:
    #    print("插入失败！")

    # #删
    # sql = "Delete FROM " + tablename + " where DrawerGroup = '33'"
    # if mdb_del(conn, cur, sql):
    #    print("删除成功！")
    # else:
    #    print("删除失败！")

    # #改
    # sql = "Update " + tablename + " Set DrawerGroup = '哈哈' where ID = 4182"
    # if mdb_modi(conn, cur, sql):
    #    print("修改成功！")
    # else:
    #    print("修改失败！")

    #查
    # sql = "SELECT * FROM " + tablename + " where id = 4181 or id = 4182"
    # sel_data = mdb_sel(cur, sql)
    # print(sel_data)


    # # 获取表名列表
    # table_list = mdb_table_list(cur)
    # print(table_list)

    mdb_modi_mu(cur, tablename)




    cur.close()    #关闭游标
    conn.close()   #关闭数据库连接