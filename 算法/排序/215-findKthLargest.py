#!/usr/bin/python3
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
        # 第k个最大的元素，即升序排列后，index为len(nums)-k
        k = len(nums) - k
        low = 0
        high = len(nums) - 1
        while low <= high:
            p = self.patition(nums, low, high)
            if k < p:
                high = p - 1
            elif k > p:
                low = p + 1
            else:
                return nums[p]
        return -1

    def patition(self, alist, low, high):
        mid_value = alist[low]
        while low < high:
            while low < high and alist[high] >= mid_value:
                high -= 1
            alist[low] = alist[high]

            while low < high and alist[low] <= mid_value:
                low += 1
            alist[high] = alist[low]
        alist[low] = mid_value
        return low


# 堆排序
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass


print(Solution1().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
