# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        prev = ListNode(0)
        prev.next = head
        p1, p2 = prev, prev
        n = k
        while n > 0:
            p2 = p2.next
            n -= 1
        while p2:
            p2 = p2.next
            p1 = p1.next
        return p1
