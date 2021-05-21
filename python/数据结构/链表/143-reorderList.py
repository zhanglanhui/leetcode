#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
# 通过次数96,583提交次数159,702

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        prev = ListNode(-1, head)
        p = prev
        p1 = p2 = head
        stack = []
        while p2.next:
            p2 = p2.next
            stack.append(p2)
        chang = False
        time = 0
        size = len(stack)
        while time <= size:
            if not chang:
                p.next = p1
                p1 = p1.next
            else:
                p.next = stack.pop()
            chang = ~chang
            p = p.next
            time += 1
        p.next = None
        return prev.next
