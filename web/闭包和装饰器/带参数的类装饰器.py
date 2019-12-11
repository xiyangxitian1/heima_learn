class logger(object):
    # def __init__(self, level='INFO'):
    #     self.level = level

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # print("[{level}]: the function {func}() is running...".format(level=self.level, func=func.__name__))
            print(self.args, self.kwargs)
            print('function {}() is running'.format(func.__name__))
            result = func(*args, **kwargs)
            return result

        return wrapper


@logger(level="WARNING")
def say(something):
    print("say {}!".format(something))
    return 1


if __name__ == '__main__':
    a = say("hello")
    print(a)
