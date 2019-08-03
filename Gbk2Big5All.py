import Gbk2Big5_txt
import Gbk2Big5_ini
import Gbk2Big5_dat
import file_extension


def Gbk2Big5All(path):
    if file_extension.file_extension(path) == '.txt':
        a = Gbk2Big5_txt.Gbk2Big5_txt(path)
        a.convert()

    elif file_extension.file_extension(path) == '.ini':
        a = Gbk2Big5_ini.Gbk2Big5_ini(path)
        a.convert()

    elif file_extension.file_extension(path) == '.dat':
        a = Gbk2Big5_dat.Gbk2Big5_dat(path)
        a.convert()

    else:
        return False
    return True