# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """合并两个有序链表"""
        if not l1:
            return l2
        if not l2:
            return l1
        result = ListNode(0)
        l3 = result
        while True:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

            if l1 is None:
                l3.next = l2
                break
            elif l2 is None:
                l3.next = l1
                break

        return result.next
