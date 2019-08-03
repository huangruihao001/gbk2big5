import Gbk2Big5
import file_extension


class Gbk2Big5_txt():
    """
    将txt文件简繁转换
    """
    def __init__(self, path, flag=0):
        self.path = path
        self.flag = flag

    def file_open_txt(self):
        f = open(self.path)
        file = f.read()
        f.close()
        return file

    def convert(self):
        if file_extension.file_extension(self.path) == '.txt':
            file = str(Gbk2Big5.Gbk2Big5(self.file_open_txt()))
            # print(file)
            f = open(self.path, 'w')
            f.write(file)
            f.close()
            print('简繁转换成功')
        else:
            print('文件类型错误')


if __name__ == '__main__':
    a = Gbk2Big5_txt('./kitdat/SysInnerSetting.txt')
    a.convert()
