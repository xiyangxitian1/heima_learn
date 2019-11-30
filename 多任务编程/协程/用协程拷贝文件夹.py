"""拷贝文件夹（采用多任务的方式）"""
import os
import time_util
import multiprocessing
import threading
import gevent
from gevent import monkey

# 如 E:/io  拷贝到F:/io1

monkey.patch_all()


@time_util.get_time
def copyDir(path, destPath):
    '''拷贝文件夹'''
    if not os.path.exists(path):
        print('文件夹不存在')
        return
    if not os.path.exists(destPath):
        os.makedirs(destPath)
    # 拷贝
    copyAllFiles(path, destPath)


def copyAllFiles(path1, path2, isDir=False):
    g1 = None
    g2 = None
    g3 = None
    if isDir or os.path.isdir(path1):
        dirs = os.listdir(path1)
        for dir in dirs:
            path11 = os.path.join(path1, dir)
            path22 = os.path.join(path2, dir)
            if not os.path.exists(path22) and os.path.isdir(path11):
                os.makedirs(path22)
                if not g2:
                    g2 = gevent.spawn(copyAllFiles, path11, path22, True)
                # copyAllFiles(path11, path22, True)  # 加上是否是目录判断  提高效率
                g2.join()
                continue
            if not g3:
                g3 = gevent.spawn(copyAllFiles, path11, path22)
            g3.join()
            # copyAllFiles(path11, path22)
    else:
        # copyFileToFile(path1, path2)
        # 每次都启用一个进程去copy文件
        # multiprocessing.Process(target=copyFileToFile, args=(path1, path2)).start()
        # 每次都启用一个线程去copy文件
        # threading.Thread(target=copyFileToFile, args=(path1, path2)).start()
        # 用协程的方式去copy文件

        if not g1:
            g1 = gevent.spawn(copyFileToFile, path1, path2)
        g1.join()


def copyFileToFile(file1, file2):
    with open(file1, 'rb') as f1:
        with open(file2, 'wb') as f2:
            f2.write(f1.read())


if __name__ == '__main__':
    # copyDir(r'E:\io', r'F:\io1')
    # copyDir(r'F:\heima\33期就业班', r'F:\heima1')  # 程序执行共用时：57.18418884277344
    # 程序执行时间是很长的，所以采取多任务的方式来提高程序的速度
    # copyDir(r'F:\heima\33期就业班', r'F:\heima2') # 程序执行共用时：9.067957639694214   现在用时少了很多，这是用的多进程的方式
    # copyDir(r'F:\heima\33期就业班', r'F:\heima5')  # 程序执行共用时：1.2547411918640137   现在用时少了更多，这是用的多线程的方式
    # copyDir(r'F:\heima\33期就业班', r'F:\heima6')  # 程序执行共用时：39.45530891418457   用协程的方式实现  应该是有问题，操作了相同的函数了
    copyDir(r'F:\heima\33期就业班', r'F:\heima7')  # 程序执行共用时：39.45530891418457   用协程的方式实现
