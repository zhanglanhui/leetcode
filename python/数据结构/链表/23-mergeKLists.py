#!/usr/bin/python3
from typing import List
import functools


# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#  
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwoList(l1: ListNode, l2: ListNode):
            p1, p2 = l1, l2
            head = ListNode(0)
            p3 = head
            while p1 or p2:
                if not p1 or (p2 and p2.val < p1.val):
                    p3.next = p2
                    p2 = p2.next
                else:
                    p3.next = p1
                    p1 = p1.next
                p3=p3.next
            return head.next

        headdd = ListNode(0)
        size = len(lists)
        if size == 0: return headdd.next
        if size <= 1: return lists[0]
        sss = size
        tmp22 = lists
        while sss > 1:
            tmp = []
            for i in range(0, sss, 2):
                if i + 1 >= sss:
                    tmp.append(tmp22[i])
                    continue
                tmp.append(mergeTwoList(tmp22[i], tmp22[i + 1]))
            tmp22 = tmp
            sss = len(tmp22)
        return tmp22[0]
