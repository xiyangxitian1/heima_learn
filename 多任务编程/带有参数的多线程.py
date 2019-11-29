import threading
import time


def foo(*args, **kwargs):
    if 'count' in kwargs.keys():
        for _ in range(kwargs['count']):
            print('foo_kwargs...')
    elif args:
        for _ in range(args[0]):
            print('foo_args...')


if __name__ == '__main__':
    t = threading.Thread(target=foo, args=(3,), kwargs={'count1': 5})
    t.start()
