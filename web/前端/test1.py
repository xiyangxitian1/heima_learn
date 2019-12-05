import dis

a = 1
b = '1'


def test1():
    if a > 2 and a < 10 and a < 30:
        pass


def test2():
    if a > 2:
        pass


if __name__ == '__main__':
    dis.dis(test1)
    print('#' * 100)
    dis.dis(test2)
