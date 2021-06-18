#!/usr/bin/python3
from typing import List
import functools


# 峰值元素是指其值大于左右相邻值的元素。
#
# 给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞ 。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3,1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-peak-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums: return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid + 1] >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left


print(Solution().findPeakElement([1,2,3,1]))
