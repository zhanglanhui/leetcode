#!/usr/bin/python3
from typing import List
import functools


# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
#
#  
#
# 示例 1：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def merge_sort(self, nums, l, mid, h):
        i, j = l, mid + 1
        tmp = []
        while i <= mid or j <= h:
            if j > h or (i <= mid and nums[i] <= nums[j]):
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        nums[l:h + 1] = tmp

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if 0 == n:
            return
        nums1[m:m + n] = nums2
        self.merge_sort(nums1, 0, m - 1, m + n - 1)
        return


gg = [1, 2, 3, 0, 0, 0]
print(Solution().merge(gg, 3, [2, 5, 6], 3))
print(gg)
