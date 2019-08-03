import Gbk2Big5_txt


class Gbk2Big5_html(Gbk2Big5_txt.Gbk2Big5_txt):
    """将dat文件简繁转换"""
    def __init__(self, path, flag=0):
        super(Gbk2Big5_html, self).__init__(path, flag)
        self.file_extension = ".html"  # 文件拓展名



if __name__ == '__main__':
    a = Gbk2Big5_html('./kitdat/brands.html')
    a.convert()
