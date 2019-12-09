# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """这个是要遍历根到叶子节点的所有的路径了，然后判断是不是等于sum，返回所有的结果"""
        if not root:
            return None
        # 递归返回一个列表，每个列表中是好多的列表，是每个子节点到叶子节点的路径。
        return self.getResult(root, sum)

    def getResult(self, root, sum1):
        path = self.getAllPath(root)
        result = []
        for i in path:
            if sum1 == sum(i):
                result.append(i)
        return result

    def getAllPath(self, node) -> List[List[int]]:
        """
            得到根节点到所有叶子节点的路径
        :param root:
        :return:
        """
        if not node.left and not node.right:
            return [[node.val]]
        else:
            val = node.val
            if node.left and node.right:
                return [[node.val] + j for j in
                        [i for i in self.getAllPath(node.left)] + [i for i in self.getAllPath(node.right)]]
            if node.right:
                return [[node.val] + j for j in [i for i in self.getAllPath(node.right)]]
            if node.left:
                return [[node.val] + j for j in [i for i in self.getAllPath(node.left)]]
