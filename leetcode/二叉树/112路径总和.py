# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
            给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
            这条路径上所有节点值相加等于目标和。
            思路：
            1.把所有的路径全部记录，然后去判断有没有这种。
                改进：不查全部，而是只要查到有一条就返回True，找完还是没有就返回False
        :param root:
        :param sum:
        :return:
        """
        if root:
            if not root.left and not root.right:
                return root.val == sum
            elif not root.left:
                return self.hasPathSum(root.right, sum - root.val)
            elif not root.right:
                return self.hasPathSum(root.left, sum - root.val)
            else:
                return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        else:
            return False
