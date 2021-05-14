#!/usr/bin/python3
from typing import List
import functools


# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 递归
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead


# 迭代
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        return prev


print(Solution1().reverseList([1, 2, 3, 4, 5]))
