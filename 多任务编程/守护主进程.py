import multiprocessing
import time


def task():
    for i in range(5):
        print('task..%d' % i)
        time.sleep(1)
        # exit()


if __name__ == '__main__':
    p = multiprocessing.Process(target=task)
    # 推荐使用守护主线程这种方法
    p.daemon = True
    p.start()
    time.sleep(2)
    print('over')
    # p.terminate()
    exit()
