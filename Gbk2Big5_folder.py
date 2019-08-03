import Gbk2Big5


class Gbk2Big5_folder():
    """
    将文件夹简繁转换
    """
    def __init__(self, path, flag=0):
        self.path = path
        self.flag = flag

    def file_open_txt(self):
        f = open(self.path)
        file = f.read()
        f.close()
        return file

    def file_write_txt(self):
        file = str(Gbk2Big5.Gbk2Big5(self.file_open_txt()))
        print(file)
        f = open(self.path, 'w')
        f.write(file)
        f.close()


if __name__ == '__main__':
    a = Gbk2Big5_folder('./kitdat/SysInnerSetting.txt')
    a.file_write_txt()
