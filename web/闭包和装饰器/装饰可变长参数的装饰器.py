import functools


def func_out(fn):
    def func_inner(*args, **kwargs):
        print("额外的功能……")
        r = fn(*args, **kwargs)
        return r

    return func_inner


@func_out
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
    result1 = functools.reduce(lambda x, y: x + y, args)
    result2 = functools.reduce(lambda x, y: x + y, kwargs.values())
    return result1 + result2


r = foo(1, 2, 3, c=4)
print(r)
