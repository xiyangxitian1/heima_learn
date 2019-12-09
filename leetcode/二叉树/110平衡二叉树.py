# 比较每个两个子节点的高度，看是否相差不大于1即可
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        # 遍历所有节点，全部都做判断
        l = []
        Solution.getAllNode(root, l)
        for l1 in l:
            lefMaxDepth = self.maxDepth(l1.left)
            rightMaxDepth = self.maxDepth(l1.right)
            if abs(lefMaxDepth - rightMaxDepth) > 1:
                return False
        return True

    @staticmethod
    def getAllNode(root: TreeNode, l):
        if root:
            l.append(root)
        if root.left:
            Solution.getAllNode(root.left, l)
        if root.right:
            Solution.getAllNode(root.right, l)
