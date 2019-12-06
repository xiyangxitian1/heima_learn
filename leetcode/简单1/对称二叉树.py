# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        leftNode, rightNode = root.left, root.right
        # 判断左右两边是否相同即可,不行，不是判断相同，而是判断是不是镜像的，是否对称
        # 左边树的左点的一个节点值与右边树的右边一个节点值相同
        return self.isSymmetricTwoNode(leftNode, rightNode)

    @staticmethod
    def isSymmetricTwoNode(leftNode, rightNode) -> bool:
        # 判断第一个节点是否是与第二个对称的
        if not leftNode and not rightNode:
            return True
        elif not leftNode or not rightNode:
            return False
        elif leftNode.val != rightNode.val:
            return False
        return Solution.isSymmetricTwoNode(leftNode.left, rightNode.right) \
               and Solution.isSymmetricTwoNode(leftNode.right, rightNode.left)


if __name__ == '__main__':
    head = TreeNode(1)
    leftNode = TreeNode(2)
    rightNode = TreeNode(2)
    head.left = leftNode
    head.right = rightNode
    leftNode.left = TreeNode(3)
    leftNode.right = TreeNode(4)
    rightNode.left = TreeNode(4)
    rightNode.right = TreeNode(3)

    oS = Solution()
    y = oS.isSymmetric(head)
    print(y)
