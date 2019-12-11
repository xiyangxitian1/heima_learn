import functools


def function_wrapper(wrapped):
    
    @functools.wraps(wrapped)
    def _wrapper(*args, **kwargs):
        print("额外的功能")
        return wrapped(*args, **kwargs)

    return _wrapper()


@function_wrapper
def foo():
    print("foo...")


if __name__ == '__main__':
    foo()
