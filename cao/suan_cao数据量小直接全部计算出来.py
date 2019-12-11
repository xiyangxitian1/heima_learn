from random import randint
import copy
import threading


class CalCaoJinFen(object):
    """计算类"""

    def __init__(self, source_lsit, result):
        # 把这个一层的列表source_lsit再包装两层
        self.source_data = [[source_lsit]]
        self.result = result
        self.__getFirstResult()  # 第一次进行处理
        self.__getNResult()  # 进行完全的处理，得到最终结果在self.source_data中
        # 把字符a全部去掉
        self.__remove_a_from_data()
        # 转换成两层列表
        self.__convert2list()

    def calculate_result(self):
        """计算结果"""
        for i in self.source_data:
            if sum(i) == self.result:
                print(i)

    @staticmethod
    def findAindex(list1):
        """获取a在列表中最后的位置 ,没有则返回None"""
        for i in range(len(list1) - 1, -1, -1):
            if 'a' == list1[i]:
                return i
        return None

    def __getNResult(self):
        """得到最终结果"""
        # 上一次得到的结果
        while self.source_data[-1][0].count('a') < len(self.source_data[-1][0]) - 1:
            len1 = len(self.source_data[-1][0])
            source_list = []
            source_list1 = []
            source_list.append(source_list1)
            i = self.source_data[-1]
            for j in i:  # j仍然是个列表
                index_a = CalCaoJinFen.findAindex(j)  # 字符a在列表j中的最后位置
                if index_a == len1 - 1:  # 如果字符a在列表中的最后了，就不需要再计算在内了
                    continue
                for k in range(index_a + 1, len1):
                    j_copy = copy.copy(j)
                    j_copy[k] = 'a'  # 把字符a的下一个数字设置为a  算是去掉
                    source_list1.append(j_copy)
            self.source_data += source_list

    def __getFirstResult(self):
        # 去掉一个
        source_list = []
        source_list1 = []
        source_list.append(source_list1)
        i = self.source_data[0][0]
        len1 = len(i)
        for j in range(len1):
            # i_i = i.copy()  # 复制一个i 这种方式太慢  还没有切片快，
            i_i = copy.copy(i)
            i_i[j] = 'a'  # 用个a来表示这个位置已经被去掉了
            source_list1.append(i_i)
        self.source_data += source_list
        # print(self.source_data)

    def __remove_a_from_data(self):
        for i in self.source_data:
            for j in i:
                while j.count('a') > 0:
                    j.remove('a')

    def __convert2list(self):
        """转成两层的列表，而不是用3层了"""
        source_list = []
        for i in self.source_data:
            for j in i:
                source_list.append(j)
        self.source_data = source_list


if __name__ == '__main__':
    list1 = [
        -11048.44,
        3.25,
        18.19,
        74.57,
        82.77,
        118.09,
        304.05,
        623.05,
        641.14,
        716.39,
        761.93,
        930.23,
        1154.23,
        1216.83,
        1419.63,
        1876.93,
        2514.38,
        2581.96,
        3000,
        3151.25,
        5824.94,
        6452.4,
        8825.27,
        10553.48,
        10557.93,
        11524.95,
        13983.14,
        17203.12,
        20652.37,
        23711.04,
        48582.71,
        55850.48,
        55920.31,
        62647.44,
        65431.46,
        72519.35,
    ]
    result = 285718.69
    if len(list1) > 12:
        print("数据量太大，此方法不适合!（此方法适合计算数据量不超过12个的情况）")
    else:
        cao = CalCaoJinFen(list1, result)
        cao.calculate_result()
