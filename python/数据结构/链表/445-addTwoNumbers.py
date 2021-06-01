# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
#  
#
# 进阶：
#
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#
#  
#
# 示例：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_l1 = []
        stack_l2 = []
        p1, p2 = l1, l2
        while p1:
            stack_l1.append(p1)
            p1 = p1.next
        while p2:
            stack_l2.append(p2)
            p2 = p2.next
        carry = 0
        head = ListNode()
        p3 = head
        ans = []
        while stack_l1 or stack_l2:
            if stack_l1 and stack_l2:
                tmp1 = stack_l1.pop()
                tmp2 = stack_l2.pop()
                ans.append((tmp1.val + tmp2.val + carry) % 10)
                carry = (tmp1.val + tmp2.val + carry) // 10
            elif not stack_l1:
                tmp2 = stack_l2.pop()
                ans.append((tmp2.val + carry) % 10)
                carry = (tmp2.val + carry) // 10
            else:
                tmp1 = stack_l1.pop()
                ans.append((tmp1.val + carry) % 10)
                carry = (tmp1.val + carry) // 10
        if carry: ans.append(carry)
        while ans:
            tt = ans.pop()
            p3.next = ListNode(tt)
            p3 = p3.next
        return head.next
