#!/usr/bin/python3
from typing import List

# 编写一个程序，找到两个单链表相交的起始节点。
#
# 如下面的两个链表：
#
#
#
# 在节点 c1 开始相交。
#
#  
#
# 示例 1：
#
#
#
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 暴力解法
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        null_node = ListNode(-1)
        while pA:
            pB = headB
            while pB:
                if pA == pB:
                    return pA
                pB = pB.next
            pA = pA.next
        return null_node.next


# hash
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p = headA
        null_node = ListNode(-1)
        sets = set()
        while p:
            sets.add(p)
            p = p.next
        p = headB
        while p:
            if p in sets:
                return p
            p = p.next
        return null_node.next


# 其他解法
class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr1, curr2 = headA, headB
        while curr1 != curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA
        return curr1