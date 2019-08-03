import Gbk2Big5
import file_extension


class Gbk2Big5_txt():
    """
    将txt文件简繁转换
    """
    def __init__(self, path, flag=0):
        self.path = path  # 文件路径
        self.flag = flag  # 0-简转繁， 1-繁转简
        self.file_extension = ".txt"  # 文件拓展名
        self.file_extension_True = file_extension.file_extension(self.path)  # 真实文件拓展名

    def file_open_txt(self):
        f = open(self.path)
        file = f.read()
        f.close()
        return file

    def is_file(self):
        """判断文件是否为txt"""
        if self.file_extension == self.file_extension_True:
            return True
        else:
            return False

    def convert(self):
        if self.is_file():
            file = str(Gbk2Big5.Gbk2Big5(self.file_open_txt()))
            # print(file)
            f = open(self.path, 'w')
            f.write(file)
            f.close()
            # print('简繁转换成功')
        else:
            print('文件类型错误')


if __name__ == '__main__':
    a = Gbk2Big5_txt('./kitdat/brands.txt')
    a.convert()
