import time


def get_time(fn):
    """计算程序执行时间的装饰器"""

    def inner(*args, **kwargs):
        begin = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print('程序执行共用时：{}'.format(end - begin))
        return result

    return inner
