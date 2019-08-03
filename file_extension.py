import os.path


def file_extension(path):
    """获取文件后缀名"""
    return os.path.splitext(path)[1]


if __name__ == '__main__':
    print(file_extension('./kitdat/SysInnerSetting.txt'))
