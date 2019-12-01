import time


def get_time(fn):
    def wrapper(*args, **kwargs):
        begin = time.time()
        fn(*args, **kwargs)
        print('执行共用时{}ms'.format(time.time() - begin))

    return wrapper
