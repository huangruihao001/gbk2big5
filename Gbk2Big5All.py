import Gbk2Big5_txt
import Gbk2Big5_ini
import Gbk2Big5_dat
import Gbk2Big5_mdb
import Gbk2Big5_filename
import Gbk2Big5_folder
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

    elif file_extension.file_extension(path) == '.mdb':
        a = Gbk2Big5_mdb.Gbk2Big5_mdb(path)
        a.convert()

    else:
        return False
    return True

def Gbk2Big5All_filename(path):
    try:
        a = Gbk2Big5_filename.Gbk2Big5_filename(path)
        a.convert()
    except:
        return False
    else:
        return True

def Gbk2Big5All_folder(path):
    try:
        a = Gbk2Big5_folder.Gbk2Big5_folder(path)
        a.convert()
    except:
        return False
    else:
        return True