# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/odd-even-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        odd_p = head
        even_p = kkk = head.next
        while even_p and even_p.next:
            odd_p.next = even_p.next
            odd_p = odd_p.next
            even_p.next = odd_p.next
            even_p = even_p.next
        odd_p.next = kkk
        return head
