# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printListNode(head: ListNode):
    while True:
        if head.next:
            print(head.val)
            head = head.next
        else:
            print(head.val)
            break


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        result = ListNode(0)
        r = result
        while True:
            if not head.next:
                result.next = head
                break
            if head.val != head.next.val:
                result.next = head
                result = result.next
            head = head.next

        return r.next


if __name__ == '__main__':
    solu = Solution()
    head = ListNode(1)
    head1 = ListNode(1)
    head2 = ListNode(2)
    head.next = head1
    head.next.next = head2

    # print(head)
    y = solu.deleteDuplicates(head)
    printListNode(y)
