# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result = ''
        result = str(self.val)
        while True:
            if not self.next:
                break
            result += result + str(self.next.val)
            self.next = self.next.next
        return result


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head

        pre = dummy_head
        cur = head

        while cur:
            if pre and cur.val == pre.val:
                pre.next = cur.next
                cur.next = None
                cur = pre.next
                continue

            pre = cur
            cur = cur.next
        return dummy_head.next

if __name__ == '__main__':
    solu = Solution()
    # x =[1, 1, 2]
    # l1 = ListNode(1)
    # l2 = ListNode(1)
    # l3 = ListNode(2)
    # l1.next = l2
    # l2.next = l3

    # y = solu.deleteDuplicates(l1)
    # print(y)
    # print(l1)
