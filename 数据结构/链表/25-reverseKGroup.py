#!/usr/bin/python3
from typing import List
import functools


# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 进阶：
#
# 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverse(head: ListNode, tail: ListNode) -> [ListNode, ListNode]:
        prev = tail.next
        curr = head
        while prev != tail:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        hair = ListNode(0)
        hair.next = head
        prev = hair
        head1 = head
        while head1:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head1, tail = Solution.reverse(head1, tail)
            # 把子链表重新接回原链表
            prev.next = head1
            tail.next = nex
            prev = tail
            head1 = tail.next
        return hair.next
