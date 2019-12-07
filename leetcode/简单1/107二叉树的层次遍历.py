# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # 思路，先求第1层，然后根据第1层求出第二层，再根据第2层求出第3层，一直到最后 。
        # 得到结果然后倒序输出即可 。
        # 这就是算法的秒啊，想不出来就头疼，不会，想出来就豁然开朗。
        if not root:
            return root
        result = [[root]]
        while True:
            list1 = result[-1]
            l = []
            for node in list1:
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            if not l:
                break
            result.append(l)
        result1 = []
        for res in result:
            r1 = []
            for re in res:
                r1.append(re.val)
            result1.append(r1)
        result1.reverse()
        return result1
