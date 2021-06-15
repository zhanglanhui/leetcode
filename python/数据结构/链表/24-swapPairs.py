# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 示例 2：
#
# 输入：head = []
# 输出：[]
# 示例 3：
#
# 输入：head = [1]
# 输出：[1]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        tt = self.swapPairs(head.next.next)
        tmp = head.next
        head.next = tt
        tmp.next = head
        return tmp


class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        prev1 = prev = ListNode(0, head)
        p = head
        while p and p.next:
            prev1.next = p.next
            tmp = p.next.next
            p.next.next = p
            p.next = tmp
            prev1 = p
            p = tmp
        return prev.next
