"""多线程删除文件夹"""
import os
import time_util


@time_util.get_time
def delDir(path):
    if not os.path.exists(path):
        print('文件夹不存在')
        return

    if os.path.isfile(path):
        os.remove(path)
    else:
        if not os.listdir(path):
            os.removedirs(path)
        else:
            dirs = os.listdir(path)
            for d in dirs:
                path1 = os.path.join(path, d)
                delDir(path1)
            else:
                os.removedirs(path)


if __name__ == '__main__':
    delDir(r'F:\test')
