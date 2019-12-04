# Definition for singly-linked list.
from listnode import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        a = head
        while True:
            if not a or not a.next:
                break
            if a.val == a.next.val:
                a.next = a.next.next
                if not a.next:
                    break
            else:
                a = a.next

        return head


if __name__ == '__main__':
    l = [1, 1, 1]
    x = ListNode.list2Node(l)
    print(Solution().deleteDuplicates(x))
