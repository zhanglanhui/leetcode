#!/usr/bin/python3
import random
from typing import List
import functools


# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 快排
class Solution1:
    def findKthLargest(self, nums, k) -> int:
        def partition(nums, low, high):
            if low >= high: return
            tmp = random.randint(low, high)
            nums[tmp], nums[high] = nums[high], nums[tmp]
            i = low
            for j in range(low, high):
                if nums[j] > nums[high]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        def quick_sort(nums, low, high):
            if low >= high: return
            pivot = partition(nums, low, high)
            if pivot == k - 1: return
            quick_sort(nums, pivot + 1, high)
            quick_sort(nums, low, pivot - 1)
            # return nums[k - 1]

        quick_sort(nums, 0, len(nums) - 1)
        return nums[k - 1]


#### 堆排序，重要
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def max_heapify(heap, root, heap_len):
            p = root
            while p * 2 + 1 < heap_len:
                l, r = p * 2 + 1, p * 2 + 2
                _next = l if heap_len <= r or heap[r] < heap[l] else r
                if heap[p] < heap[_next]:
                    heap[p], heap[_next] = heap[_next], heap[p]
                    p = _next
                else:
                    break

        def heapSort(nums: List[int]):
            for i in range(len(nums) - 1, -1, -1):
                max_heapify(nums, i, len(nums))
            for i in range(len(nums) - 1, len(nums) - 1 - k, -1):
                nums[i], nums[0] = nums[0], nums[i]
                max_heapify(nums, 0, i)

        heapSort(nums)
        return nums[len(nums) - k]


print(Solution2().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 3))


# 快排
class Solution3:
    def findKthLargest(self, nums, k) -> int:
        def random_partition(nums, lo, hi):
            pivot = random.randint(lo, hi)
            nums[hi], nums[pivot] = nums[pivot], nums[hi]
            i = lo
            for j in range(lo, hi):
                if nums[j] > nums[hi]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[hi], nums[i] = nums[i], nums[hi]
            return i

        def quick_sort(nums, left, right):
            if left >= right: return
            pivot = random_partition(nums, left, right)
            if pivot == k - 1: return
            quick_sort(nums, left, pivot - 1)
            quick_sort(nums, pivot + 1, right)
            return

        if not nums: return 0
        quick_sort(nums, 0, len(nums) - 1)
        return nums[k - 1]


print(Solution3().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 3))


class Solution4:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def max_heapify(heap, root, heap_len):
            p = root
            while p * 2 + 1 < heap_len:
                l, r = p * 2 + 1, p * 2 + 2
                _next = l if heap_len <= r or heap[r] < heap[l] else r
                if heap[p] < heap[_next]:
                    heap[p], heap[_next] = heap[_next], heap[p]
                    p = _next
                else:
                    break

        def heapSort(nums: List[int]):
            for i in range(len(nums) - 1, -1, -1):
                max_heapify(nums, i, len(nums))
            for i in range(len(nums) - 1, len(nums) - k, -1):
                nums[i], nums[0] = nums[0], nums[i]
                max_heapify(nums, 0, i)

        heapSort(nums)
        return nums[0]


print(Solution4().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 3))
