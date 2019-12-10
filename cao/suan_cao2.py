from random import randint


class CalCaoJinFen(object):
    """计算类"""

    def __init__(self, source_lsit, result):
        self.source_data = source_lsit
        self.result = result

    def getResult(self):
        len1 = len(self.source_data)

        while 1:
            random_num = randint(0, len1 - 1)
            self.source_data[random_num]



if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    result = 10
