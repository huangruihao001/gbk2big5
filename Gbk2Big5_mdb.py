import Gbk2Big5_txt
import win32com_mdb


class Gbk2Big5_mdb(Gbk2Big5_txt.Gbk2Big5_txt):
    """
    将mdb文件简繁转换
    """

    def __init__(self, path, flag=0):
        super(Gbk2Big5_mdb, self).__init__(path, flag)
        self.file_extension = ".mdb"  # 文件拓展名


    def convert(self):
        if self.is_file():
            win32com_mdb.convert_mdb_all(self.path)
        else:
            print('文件类型错误')


if __name__ == '__main__':
    a = Gbk2Big5_mdb('./kitdat/CabinetDrawer.mdb')
    a.convert()
