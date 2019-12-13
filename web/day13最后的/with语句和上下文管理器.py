# with 语句需要和上下文管理器配合使用
#     1.with开始时，上文函数__enter__会被自动调用
#     2.with结束时，下文函数__exit__会被自动调用
import os
class Open(object):

    def __init__(self, filename, filemode):
        print("init...")
        self.__filename = filename
        self.__filemode = filemode

    def __enter__(self):
        print("enter...")
        self.__file = open(self.__filename, self.__filemode)
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit..")
        self.__file.close()

    def __del__(self):
        print("del...")

    def say_hello(self):
        print("hello^")


if __name__ == '__main__':
    # f1 = Open('1.txt', 'w')
    # with f1 as f:
    #     f.write('abc')

    # with Open("1.txt", 'r') as f:
    #     data = f.read()
    #     print(f)
    # print(data)
    if os.path.exists("b.jpg"):
        os.remove("b.jpg")
    f1 = Open("a.jpg", 'rb')
    all_data = ""
    with f1 as f:
        while 1:
            data = f.read(1024)
            print(len(data))
            if data:
                # all_data += data
                with Open("b.jpg", 'ab') as f2:
                    f2.write(data)
                continue
            break

    print(all_data)
    f1.say_hello()
