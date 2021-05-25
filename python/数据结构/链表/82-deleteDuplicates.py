# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
#
# 返回同样按升序排列的结果链表。
#
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = ListNode(-101, head)
        p2 = p = node
        prev_val = -101
        stack = []
        while p:
            p_tmp = p
            if prev_val != p.val:
                if stack:
                    p2.next = stack.pop()
                    p2 = p2.next
                stack.append(p)
                p = p.next
            else:
                stack = []
                p = p.next
            prev_val = p_tmp.val
        if stack:
            p2.next = stack.pop()
            p2 = p2.next
        p2.next=None
        return node.next
