#!/usr/bin/python3
from typing import List
import functools


# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。
#
#
#
# 示例1:
#
# 输入: nums = [-2 ,1 ,-3 ,4 ,-1 ,2 ,1 ,-5 ,4]
# 输出: 6
# 解释: 连续子数组 [4 ,-1 ,2 ,1] 的和最大，为 6。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("inf")
        last = 0
        for i, x in enumerate(nums):
            last = max(last + nums[i], nums[i])
            ans = max(ans, last)
        return ans


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
