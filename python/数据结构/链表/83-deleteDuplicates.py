# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
#
# 返回同样按升序排列的结果链表。
#
#  
#
# 示例 1：
#
#
# 输入：head = [1,1,2]
# 输出：[1,2]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sets = set()
        prev = p = ListNode(-1, head)
        last = None
        while prev.next:
            prev = prev.next
            ttt = prev.val
            if ttt not in sets:
                sets.add(prev.val)
                if last:
                    last.next = prev
                last = prev
        if last: last.next = None
        return p.next
