import Gbk2Big5_txt
import file_extension


class Gbk2Big5_ini(Gbk2Big5_txt.Gbk2Big5_txt):
    """将ini文件简繁转换"""
    def __init__(self, path, flag=0):
        super(Gbk2Big5_ini, self).__init__(path, flag)
        self.file_extension = ".ini"  # 文件拓展名



if __name__ == '__main__':
    a = Gbk2Big5_ini('./kitdat/brands.ini')
    a.convert()
