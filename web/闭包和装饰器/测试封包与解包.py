# 封包与解包

def foo(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)
    foo2(*args, **kwargs)


def foo2(*args, **kwargs):
    print("foo2", args)
    print("foor2", kwargs)


if __name__ == '__main__':
    # foo(1, 2, c=3)  #  封包成了   (1,2)  {'c':3}
    # foo((1, 2), {'c': 3})  # 封包成了 (1,2,{'c':3}),{}     这样写会把参数都当成是args的参数  所以要用声明参数=才可以
    # a = {'c': 3}
    # foo2(a)
    # foo(1, 2, c=3)
    # a = (1, 2)
    # foo(*a, **b)  # 在函数的参数里才会进行封包与解包
    # b = {'c': 3}
    foo(1, 2, b=3)  # b=3 也是只能在参数里使用，会自动的封包成{'b':3}  1,2 会自动的封包成(1,2)
    #  然后再解包成 1,2  b=3  传参给foo2  foo2又有*  又会进行封包
