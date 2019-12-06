# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 思路，遍历节点 先根遍历，如果遍历路径到都是向右，就退出。

        head = root
        maxDep = 0
        return maxDep