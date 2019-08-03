import Gbk2Big5
import Gbk2Big5_txt
import pypyodbc


class Gbk2Big5_mdb(Gbk2Big5_txt.Gbk2Big5_txt):
    """
    将mdb文件简繁转换
    """

    def __init__(self, path, flag=0):
        super(Gbk2Big5_mdb, self).__init__(path, flag)
        self.file_extension = ".mdb"  # 文件拓展名
        self.password = ""  # 数据库密码
        self.str = 'Driver={Microsoft Access Driver (*.mdb)};PWD' + self.password + ";DBQ=" + self.path
        self.conn = pypyodbc.win_connect_mdb(str)  # 数据库连接
        self.cur = self.conn.cursor()  # 创建游标

    def convert(self):
        if self.is_file():
            pass
            # TODO(hrh): 遍历并转换mdb中的数据
        else:
            print('文件类型错误')


if __name__ == '__main__':
    a = Gbk2Big5_mdb('./kitdat/CabinetDrawer.mdb')
    a.convert()
