# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    """
     顶 ：求？
     
     max(左节点的最大深度，右节点的最大深度）+ 1
     
     叶子的最大深度   1
    
    """
