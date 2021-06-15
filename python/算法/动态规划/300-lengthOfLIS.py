#!/usr/bin/python3
from typing import List
import functools


# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#
#  
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 动态规划
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# 贪心
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tmp = []
        for x in nums:
            if not tmp or x > tmp[-1]:
                tmp.append(x)
            else:
                left, right = 0, len(tmp) - 1
                loc = len(tmp) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if tmp[mid] >= x:
                        loc = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                tmp[loc] = x
                print(tmp)
        return len(tmp)


print(Solution2().lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]))
