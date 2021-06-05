#!/usr/bin/python3
from typing import List
import functools

# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
#
#  
#
# 示例 1：
#
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 示例 2：
#
# 输入：target = 4, nums = [1,4,4]
# 输出：1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import bisect


# 前缀和+二分查找
class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums: return 0
        sums = [0]
        ans = float('inf')
        for x in nums:
            sums.append(sums[-1] + x)
        for i in range(1, len(nums) + 1):
            t = sums[i - 1] + target
            index = bisect.bisect_left(sums, t)
            if index <= len(sums) - 1 and nums[index] >= t:
                ans = min(ans, index - i + 1)
        return ans


# 滑动窗口法
class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums: return 0
        ans = len(nums) + 1
        start, end = 0, 0
        tmp = 0
        while end < len(nums):
            tmp += nums[end]
            while tmp >= target:
                ans = min(ans, end - start + 1)
                tmp -= nums[start]
                start += 1
            end += 1
        return ans if ans < len(nums) + 1 else 0


print(Solution2().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
