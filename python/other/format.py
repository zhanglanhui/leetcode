# name="111"
# print("hi there %s" % name )
# !/usr/bin/python3
from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        if not l1 or not l2:
            head.next = l1 if not l2 else l2
            return head.next
        p1, p2 = l1, l2
        p3 = head
        while p1 or p2:
            if not p1 or (p2 and p1.val > p2.val):
                p3.next = p2
                p2 = p2.next
            else:
                p3.next = p1
                p1 = p1.next
            p3 = p3.next
        return head.next


print(Solution().lengthOfLongestSubstring("tmmzuxt"))

# name = (1, 2, 3)
# print("hi there %s" % (name,))
# print("hi there {}".format(name))
