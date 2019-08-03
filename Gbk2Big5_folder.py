import os
import Gbk2Big5_txt
import Gbk2Big5

class Gbk2Big5_folder(Gbk2Big5_txt.Gbk2Big5_txt):
    """将ini文件简繁转换"""
    def __init__(self, path, flag=0):
        super(Gbk2Big5_folder, self).__init__(path, flag)

    def convert(self):
        dbtype_list = self.dbtype_list()
        for i in dbtype_list:
            old_path = self.path + "/" + str(i)
            new_path = self.path + "/" + str(Gbk2Big5.Gbk2Big5(i))
            print(new_path)
            try:
                os.rename(old_path, new_path)
            except Exception as e:
                print(e)
                print('rename dir fail\r\n')

    def dbtype_list(self):
        dbtype_list = []
        for root, dirs, files in os.walk(self.path):
            # print(root)  # 当前目录路径
            # print(dirs)  # 当前路径下所有子目录
            # print(files)  # 当前路径下所有非目录子文件
            dbtype_list.extend(dirs)
            dbtype_list.extend(files)
            break
        return dbtype_list


if __name__ == '__main__':
    a = Gbk2Big5_folder('./kitdat/新建文件夹')
    print(a.dbtype_list())
    a.convert()