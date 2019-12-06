# Definition for a binary tree node.
class TreeNode(object):
    """定义二叉树"""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def list2Tree(list1):
        """
            列表转成二叉树
        :param list1:
        :return:
        """
        listNode = []
        for l in list1:
            node = TreeNode(l)
            if listNode:
                if not listNode[0].left:
                    listNode[0].left = node
                else:
                    listNode[0].right = node
                    listNode.pop(0)
                listNode.append(node)
            else:
                head = node
                listNode.append(node)
        return head

    @staticmethod
    def __firstRootBianLiTreeNode(head, l):
        if head:
            l.append(head.val)
            TreeNode.__firstRootBianLiTreeNode(head.left, l)
            TreeNode.__firstRootBianLiTreeNode(head.right, l)

    @staticmethod
    def __midRootBianLiTreeNode(head, l):
        pass

    def listAllTreeNode(self, mode=1):
        """先根遍历
            mode 默认1 先根遍历  2中根遍历  3后根遍历
        """
        l = []
        if mode == 1:
            # 先根遍历
            TreeNode.__firstRootBianLiTreeNode(self, l)
        elif mode == 2:
            # 中根遍历
            pass
        elif mode == 3:
            # 后根遍历
            pass
        return l

    def __str__(self):
        return ','.join([str(i) for i in self.listAllTreeNode()])


if __name__ == '__main__':
    treeNode = TreeNode.list2Tree([1, 2, 2, 3, 4, 4, 3])
    lst = treeNode.listAllTreeNode(2)
    print(lst)
