import multiprocessing

import time


def foo():
    for i in range(10):
        print(multiprocessing.current_process().name, i)
        time.sleep(1)


if __name__ == '__main__':
    p = multiprocessing.Process(target=foo, name='守护进程')
    p.daemon = True
    p.start()
    p1 = multiprocessing.Process(target=foo)
    # p.daemon = True
    p1.start()

    time.sleep(5)
    print('主进程结束')
    exit()
    print('主进程结束233333333333333')
    # 进程1执行了5次   进程2执行了10次
