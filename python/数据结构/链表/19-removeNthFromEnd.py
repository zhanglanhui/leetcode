#!/usr/bin/python3
from typing import List
import functools
from collections import defaultdict

# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
# 进阶：你能尝试使用一趟扫描实现吗？
#
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 示例 2：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = p2 = head
        t = 0
        ttt = ListNode(-1)
        while p2 and t < n:
            p2 = p2.next
            t += 1
        while p2 and p2.next:
            p2 = p2.next
            p1 = p1.next
        if not p2:
            return head.next
        if p1.next:
            p1.next = p1.next.next
        else:
            return ttt.next
        return head
