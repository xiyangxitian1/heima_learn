import threading, time, os


def sing():
    for i in range(5):
        print('sing...%d' % i)
        time.sleep(0.5)


def dance():
    for i in range(5):
        print('dance...%d' % i)
        time.sleep(0.5)


def eat():
    for i in range(5):
        print('吃饭...%d' % i)
        time.sleep(0.5)


def learn():
    for i in range(5):
        print('学习...%d' % i)
        time.sleep(0.5)


if __name__ == '__main__':
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t3 = threading.Thread(target=eat)
    t4 = threading.Thread(target=learn)
    t1.start()
    # t1.join()  # 阻塞 等待t1执行完成
    t2.start()
    t3.start()
    t4.start()
