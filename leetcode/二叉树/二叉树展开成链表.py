# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        def helper(root):
            t1 = root.left
            t2 = root.right
            root.left = None
            # 如果为叶节点，则直接返回此节点*
            if t1 is None and t2 is None:
                return root
            # 如果有一个子节点为None,则根节点的右节点变为非空的节点，并返回此非空节点链表化后的尾节点
            if t1 is None or t2 is None:
                root.right = t2 if t1 is None else t1
                return helper(root.right)
            # 如果两个子节点都不为空
            # 将根节点与左节点连起来
            root.right = t1
            # 对左节点链表化后，返回其尾节点
            t1_tail = helper(t1)
            # 将刚才的尾节点与右节点连接
            t1_tail.right = t2
            # 对右节点进行链表化
            t2_tail = helper(t2)
            # 返回链表化的尾节点
            return t2_tail

        helper(root)
        return root
