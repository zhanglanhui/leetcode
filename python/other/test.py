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
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        cur = prev = ListNode(0)
        p = head
        change = False
        time = 0
        while time <= len(stack):
            if change:
                cur.next = stack.pop()
            else:
                cur.next = p
                p = p.next
            change = ~change
            cur = cur.next
            time += 1
        cur.next = None
        return prev.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = prev = ListNode(-1000, head)
        while cur.next:
            tmp = cur.next
            if tmp.val != cur.val:
                cur = cur.next
            else:
                cur.next = tmp.next
        return prev.next


from random import randint


def heapSort(nums: List[int]) -> List[int]:
    # build_heap
    for i in range(len(nums) - 1, -1, -1):
        max_heapify(nums, i, len(nums))
    # sort_heap
    for i in range(len(nums) - 1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        max_heapify(nums, 0, i)
    return nums


def max_heapify(heap, root, heap_len):
    p = root
    while p * 2 + 1 < heap_len:
        l, r = p * 2 + 1, p * 2 + 2
        if heap_len <= r or heap[r] < heap[l]:
            _next = l
        else:
            _next = r
        if heap[p] < heap[_next]:
            heap[p], heap[_next] = heap[_next], heap[p]
            p = _next
        else:
            break


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isNumeralOrChar(s):
            if 0 <= ord(s) - ord("0") <= 9 or 0 <= ord(s) - ord("a") <= 25 or 0 <= ord(s) - ord("A") <= 25:
                return True
            return False

        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            while p1 < p2 and not isNumeralOrChar(s[p1]):
                p1 += 1
            while p1 < p2 and not isNumeralOrChar(s[p2]):
                p2 -= 1
            if s[p1] == s[p2] or \
                    ord(s[p1].lower()) - ord("a") == ord(s[p2].lower()) - ord("a"):
                p1 += 1
                p2 -= 1
            else:
                return False
        return True


print(Solution().isPalindrome("0P"))
