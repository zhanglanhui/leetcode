# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        prev11 = ListNode(-1, head)
        p2 = p1 = head
        for _ in range(left - 1):
            prev11 = prev11.next
            p1 = p1.next
        for _ in range(right - 1):
            p2 = p2.next
        prev11.next = p2
        prev1 = prev = p2.next
        curr = p1
        while curr != prev1:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        return head if left>1 else prev11.next
