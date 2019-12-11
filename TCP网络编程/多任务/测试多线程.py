import threading
import time


def f1(list1):
    count = 0
    while True:
        if count > 10:
            break
        # print(threading.current_thread().name, num)
        time.sleep(0.2)
        list1.append(count)
        count += 1
    print(threading.current_thread().name, list1)


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    t1 = threading.Thread(target=f1, args=(list1,), name="线程A")
    t1.start()
    t1.join()
    t2 = threading.Thread(target=f1, args=(list1,), name="线程B")
    t2.start()
    t2.join()
    print(list1)
    # 线程会竞争资源，对全局变量有影响
