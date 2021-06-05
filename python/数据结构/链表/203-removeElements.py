# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-linked-list-elements
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        ttt = self.removeElements(head.next, val)
        head.next = ttt
        return ttt if head.val == val else head
