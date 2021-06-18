#!/usr/bin/python3
from typing import List
import functools
from utils import *


# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 进阶：
# 你可以在 O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
#  
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def sortList(self, head: ListNode) -> ListNode:
        def nodeLength(head: ListNode):
            h, l = head, 0
            while h:
                h = h.next
                l += 1
            return l

        def nodeNext(head: ListNode, l):
            h = head
            while l > 0:
                h = h.next
                l -= 1
            return h

        def merge(h1: ListNode, h2: ListNode):
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, h1, h2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            if temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head
        length = nodeLength(head)
        subLength = 1
        while subLength < length:
            prv = head
            cur = nodeNext(head, subLength)
            merge(prv, cur)
            subLength <<= 1


print(Solution1().sortList())


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(hair: ListNode, mid: ListNode):
            dummy_node = p = ListNode(0)
            p1, p2 = hair, mid
            while p1 or p2:
                if p1 or (p2 and p2.val < p1.val):
                    p.next = p2
                    p2 = p2.next
                else:
                    p.next = p1
                    p1 = p1.next
                p = p.next
            return dummy_node.next

        def merge_sort(hair, tail):
            if not hair or hair == tail: return hair
            if hair.next == tail:
                hair.next = None
                return hair
            # 找到mid
            slow, fast = hair, hair
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            print(slow, fast)
            return merge(merge_sort(hair, slow), merge_sort(slow, tail))

        return merge_sort(head, None)
