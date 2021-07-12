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


class Solution2:
    def reorderList(self, head: ListNode) -> None:
        def get_half_list(h):
            if not h or not h.next: return h
            prev = ListNode(0, h)
            p, p1, p2 = prev, h, h
            while p2:
                p = p.next
                p1 = p1.next
                p2 = p2.next
                if p2:
                    p2 = p2.next
            return p, p1

        def reverse(curr):
            prev = None
            while curr:
                _next = curr.next
                curr.next = prev
                prev = curr
                curr = _next
            return prev

        def merge(h1, h2):
            p1, p2 = h1, h2
            prev1 = prev = ListNode(0)
            flag = True
            while p1 or p2:
                if flag:
                    prev.next = p1
                    p1 = p1.next
                else:
                    prev.next = p2
                    p2 = p2.next
                flag = not flag
                prev = prev.next
            prev.next = None
            return prev1.next

        mid1, mid2 = get_half_list(head)
        mid1.next = None
        mid2 = reverse(mid2)
        head = merge(head, mid2)


class Solution3:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next: return
        stack = []
        p = head
        while p:
            stack.append(p.val)
            p = p.next
        prev = pp = ListNode(0)
        exchange = True
        tmp = len(stack)
        time = 0
        while time <= tmp:
            if exchange:
                pp.next = head
                head = head.next
            else:
                pp.next = ListNode(stack.pop(), None)
            pp = pp.next
            exchange = not exchange
            time += 1
        pp.next = None
        return prev.next
