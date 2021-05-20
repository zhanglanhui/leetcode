#!/usr/bin/python3
from typing import List
import functools


# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 2: return max(nums)
        dp1 = [0] * size
        dp3 = [0] * size
        dp2 = [0] * size
        for i, x in enumerate(nums):
            if 0 == i:
                dp1[i] = nums[i]
                dp3[i] = nums[i]
                continue
            if 1 == i:
                dp1[i] = max(dp1[i - 1], nums[i])
                dp2[i] = nums[i]
                dp3[i] = max(dp3[i - 1], nums[i])
                continue
            dp3[i] = max(dp3[i - 1], nums[i] + dp3[i - 2])
            dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2])
            dp1[i] = max(dp3[i - 1], nums[i] + dp2[i - 2])
        return dp1[-1]


print(Solution().rob([2, 3, 2]))
