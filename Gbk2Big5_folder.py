import os
import Gbk2Big5_txt
import Gbk2Big5

class Gbk2Big5_folder(Gbk2Big5_txt.Gbk2Big5_txt):
    """将ini文件简繁转换"""
    def __init__(self, path, flag=0):
        super(Gbk2Big5_folder, self).__init__(path, flag)

    def convert(self):
        new_path = str(Gbk2Big5.Gbk2Big5(str(self.path)))
        print(new_path)
        try:
            os.rename(self.path, new_path)
        except Exception as e:
            print(e)
            print('rename dir fail\r\n')


if __name__ == '__main__':
    a = Gbk2Big5_folder('./kitdat/龙')
    a.convert()