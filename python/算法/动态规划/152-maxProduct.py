# name="111"
# print("hi there %s" % name )
# !/usr/bin/python3
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp2 = [0] * len(nums)
        max_num = nums[0]
        dp[0] = nums[0]
        dp2[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(max(nums[i], dp[i - 1] * nums[i]), dp2[i - 1] * nums[i])
            dp2[i] = min(min(nums[i], dp2[i - 1] * nums[i]), nums[i] * dp[i - 1])
            max_num = max(max_num, dp[i])
        return max_num


class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = prev1 = prev2 = nums[0]
        for i in range(1, len(nums)):
            tmp1 = max(max(nums[i], prev1 * nums[i]), prev2 * nums[i])
            tmp2 = min(min(nums[i], prev2 * nums[i]), nums[i] *  prev1)
            max_num = max(max_num, tmp1)
            prev1, prev2 = tmp1, tmp2
        return max_num


print(Solution().maxProduct([0, 3]))
