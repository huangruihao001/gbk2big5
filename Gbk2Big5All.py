import Gbk2Big5_txt
import file_extension


def Gbk2Big5All(path):
    if file_extension.file_extension(path) == '.txt':
        a = Gbk2Big5_txt.Gbk2Big5_txt(path)
        a.convert()
    else:
        return False
    return True