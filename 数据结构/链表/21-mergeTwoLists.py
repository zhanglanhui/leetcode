#!/usr/bin/python3
from typing import List
import functools


# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
#  
#
# 示例 1：
#
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 递归
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1


# 直接法
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_node = ListNode(-1)
        tmp = pre_node
        while l1 and l2:
            if l1.val > l2.val:
                tmp.next, l2 = l2, l2.next
            else:
                tmp.next, l1 = l1, l1.next
            tmp = tmp.next
        tmp.next = l2 if not l1 else l1
        return pre_node.next

# print(Solution1().mergeTwoLists())
