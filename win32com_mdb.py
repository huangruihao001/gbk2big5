import win32com.client
import pypyodbc
import Gbk2Big5


# 对指定表名进行简繁转换
def convert_mdb(path, tablename):
    # 建立数据库连接
    conn = win32com.client.Dispatch(r"ADODB.Connection")
    DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = ' + path
    conn.Open(DSN)

    # 打开一个记录集
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs_name = tablename
    rs.Open('[' + rs_name + ']', conn, 1, 3)


    # 查：遍历记录
    rs.MoveFirst()  #光标移到首条记录
    count = 0
    while True:
        if rs.EOF:
            break
        else:
            for i in range(rs.Fields.Count):
                #字段名：字段内容
                # print(rs.Fields[i].Name, "：", rs.Fields[i].Value)
                a = rs.Fields[i].Value
                if isinstance (a,str):
                    jt_str = str(rs.Fields[i].Name) + " = '" + str(rs.Fields[i].Value) + "'"
                    ft_str = str(rs.Fields[i].Name) + " = '" + str(Gbk2Big5.Gbk2Big5(rs.Fields[i].Value)) + "'"
                    sql = "Update " + rs_name + " Set " + ft_str +" where " + jt_str
                    conn.Execute(sql)
            count += 1
        rs.MoveNext()


    conn.Close()

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

#获取表名列表
def mdb_table_list(path):

    pathfile = path
    conn = mdb_conn(pathfile)  # 创建数据库连接
    cur = conn.cursor() # 创建游标



    table_list = []  # 获取数据库所有表名
    for table_info in cur.tables(tableType='TABLE'):
        table_list.append(table_info[2])
    cur.close()    #关闭游标
    conn.close()   #关闭数据库连接
    # print(table_list)
    return table_list

# 对所有表名进行简繁转换
def convert_mdb_all(path):
    table_list = mdb_table_list(path)
    for tablename in table_list:
        convert_mdb(path, tablename)

if __name__ == '__main__':
    # convert_mdb("./kitdat/CabinetDrawer.mdb", "DrawerPriceClass1")
    # mdb_table_list("./kitdat/CabinetDrawer.mdb")
    convert_mdb_all("./kitdat/CabinetDrawer.mdb")



