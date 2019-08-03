import os.path


def file_extension(path):
    """获取文件后缀名"""
    return os.path.splitext(path)[1]

def file_name(path):
    """获取文件名"""
    (filepath, tempfilename) = os.path.split(path)
    return tempfilename

def file_path(path):
    """获取文件路径"""
    (filepath, tempfilename) = os.path.split(path)
    return filepath



if __name__ == '__main__':
    print(file_extension('./kitdat/SysInnerSetting.txt'))
    print(file_name('./kitdat/SysInnerSetting.txt'))
    print(file_path('./kitdat/SysInnerSetting.txt'))
