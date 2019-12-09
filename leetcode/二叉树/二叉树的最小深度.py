class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        return 0 if not root else min(self.minDepth(root.left), self.minDepth(root.right)) + 1
