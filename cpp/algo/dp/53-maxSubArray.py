#!/usr/bin/python3
from typing import List
import functools


# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
#  
#
# 示例 1：
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 暴力
# 超出时间限制
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        ans = nums[0]
        for win_len in range(1, len(nums) + 1):
            for j in range(0, len(nums) - win_len + 1):
                tmp = sum(nums[j:j + win_len])
                ans = tmp if tmp > ans else ans
        return ans


# dp
# f(i)=max{f(i−1)+nums[i],nums[i]}
# 状态：通过
# 执行用时: 52 ms
# 内存消耗: 15.3 MB

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + nums[i - 1] > nums[i]:
                nums[i] = nums[i] + nums[i - 1]
            ans = max(ans, nums[i])
        print(nums)
        return ans


print(Solution2().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
