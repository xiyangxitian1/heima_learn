class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def append(self, val) -> None:
        """在链表的最后增加链表"""
        a = self
        while True:
            if a.next is None:
                a.next = ListNode(val)
                break
            a = a.next

    def insertAfter(self, val) -> None:
        """在下一个位置插入数据"""
        a = self
        if a.next is None:
            a.next = ListNode(val)
        else:
            node = ListNode(val)
            node.next = a.next
            a.next = node

    def insertBefore(self, val):
        """在前一个位置插入数据"""
        a = self
        node = ListNode(val)
        node.next = a
        return node

    def insertIndex(self, index, val):
        """
            在指定位置插入
            如果index小于等于1就是第1个位置插入
            如果index大于等于链表长度就在末尾插入
        """
        node = ListNode(val)
        if index == 0:
            node.next = self
            return node
        a = self
        i = 0
        while True:
            if i >= index or a.next is None:
                a.insertAfter(val)
                return self
            a = a.next
            i += 1

    def remove(self, val: object):
        """这是一个删除的方法，只删除第一个匹配的值,返回删除的一结果"""
        if self.val == val:
            return self.next
        a = self
        while True:
            if a.next is None:
                break
            if a.next.val == val:
                a.next = a.next.next
                break
            a = a.next
        return self

    def removeIndex(self, index):
        """删除指定位置的链表元素"""
        if index == 0:
            return self.remove(self.val)
        a = self
        i = 1
        while True:
            if a.next is None:
                return self
            if i >= index:
                a.next = a.next.next
                return self
            i += 1
            a = a.next

    def removeBefore(self):
        """
            删除前面的一个元素
            这个搞笑，做不到
        """
        pass

    def removeAfter(self):
        """
            删除后面的一个元素
        """
        if self.next is None:
            return self
        self.next = self.next.next
        return self
        # 下面这个太投巧了，但是效率可能不高
        # 写方法时还是尽量不要调用现成的方法，除非效率很高
        # return self.removeIndex(1)

    def replace(self, oldVal, newVal, is_all=False):
        """
            修改元素的值，把oldVal修改成newVal
            如果all是True，就全部修改，如果是False，就修改匹配的第一个元素
        :param is_all:
        :param oldVal:
        :param newVal:
        :return:
        """
        a = self
        while True:
            if a.val == oldVal:
                a.val = newVal
                if not is_all:
                    break
            if a.next is None:
                break
            a = a.next
        return self

    def replaceAll(self, oldVal, newVal):
        """
            修改元素的值，把oldVal修改成newVal
            如果all是True，就全部修改，如果是False，就修改匹配的第一个元素
        :param oldVal:
        :param newVal:
        :return:
        """
        a = self
        while True:
            if a.val == oldVal:
                a.val = newVal
            if a.next is None:
                break
            a = a.next
        return self

    def update(self, index=0, val=0):
        """
        修改指定位置的元素的值
        :param index:
        :param val:
        :return:
        """
        a = self
        i = 0
        while True:
            if i >= index:
                a.val = val
                break
            if a.next is None:
                break
            i += 1
            a = a.next
        return self

    def toList(self):
        result = list()
        while True:
            result.append(self.val)
            if self.next is None:
                break
            self = self.next
        return result

    @staticmethod
    def list2Node(lst: list):
        """
            把列表转成链表
        :param lst:
        :return:
        """
        if lst is None or len(lst) == 0:
            return None
        result = ListNode(0)
        head = result
        for l in lst:
            node = ListNode(l)
            head.next = node
            head = head.next
        return result.next

    def getValByIndex(self, index: int):
        """
            查找指定位置的元素的值,如果没有返回None
        :param index:
        :return:
        """
        if index < 0:
            return None
        i = 0
        while True:
            if i >= index:
                return self.val
            if self.next is None:
                return None
            i += 1
            self = self.next

    def getIndexByVal(self, val):
        """
            根据值查找元素在的位置（链表的第一个值是val的元素）,如果没有返回None
        :param val:
        :return:
        """
        i = 0
        while True:
            if self.val == val:
                break
            if self.next is None:
                return None
            i += 1
            self = self.next
        return i

    def getNodeByIndex(self, index):
        """
            返回指定位置的元素
        :param index:
        :return:
        """
        i = 0
        while True:
            if i == index:
                return self
            if self.next is None:
                return None
            i += 1
            self = self.next

    def __str__(self):
        """打印链表"""
        a = self
        result = []
        while True:
            if a is None:
                break
            result.append(a.val)
            a = a.next
        return ''.join(str(i) for i in result)


# if __name__ == '__main__':
#     l = [1, 2, 3, 4, 5]
#     n = ListNode.list2Node(l)
#     print(n)
# n.printNode()
# l1 = n.toList()
# print(l1)
# n.printNode()
#
# v = n.getValByIndex(2)
# print(v)
# n.printNode()
