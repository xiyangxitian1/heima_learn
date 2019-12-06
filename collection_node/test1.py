l = [1, 2, 3, 4]


def foo():
    while True:
        for i in l:
            if i == 4:
                break
            print(i)

        print("结束")
        break
    print('foo结束。。。')


if __name__ == '__main__':
    foo()