#!/usr/bin/python3
from typing import List
import functools


# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
#
#  
#
# 示例 1:
#
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
# 示例 2:
#
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/contiguous-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one_sum = [0]
        for x in nums:
            if x == 1:
                one_sum.append(one_sum[-1] + 1)
            else:
                one_sum.append(one_sum[-1])
        hashs = dict()
        ans = 0
        hashs[0] = -1
        for i, x in enumerate(nums):
            tmp = i + 1 - 2 * (one_sum[i + 1])
            if tmp not in hashs:
                hashs[tmp] = i
            else:
                ans = max(ans, i - hashs[tmp])
        return ans


print(Solution().findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))
