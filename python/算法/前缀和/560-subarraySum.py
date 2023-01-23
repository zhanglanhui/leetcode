#!/usr/bin/python3
from typing import List
import functools
from functools import reduce
from collections import defaultdict


# 给你一个整数数组 nums 和一个目标数个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
#
# 输入：nums = [1,2,3], k = 3
# 输出：2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/subarray-sum-equals-k
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 回朔法，太慢了超时
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        tmp = []
        global ans
        ans = 0

        def backtrack(input, start, size):
            global ans
            # if len(tmp) > size or not input:
            #     return
            if sum([y[1] for y in input]) == k and len(input) == size:
                # print(start, size,input)
                ans += 1
                return
            if len(tmp) >= size:
                return
            for i, x in enumerate(nums[start:]):
                # if start + i in [y[0] for y in tmp]:
                #     continue
                if len(tmp) > 0 and tmp[-1][0] + 1 < i + start:
                    continue
                tmp.append((start + i, x))
                backtrack(tmp, start + i, size)
                tmp.pop()

        for x in range(1, len(nums) + 1):
            backtrack(tmp, 0, x)
        return ans


print(Solution().subarraySum([1], 0))


class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            else:
                return 0
        pre_sum = 0
        ans = 0
        set_dd = defaultdict(int)
        set_dd[0] = 1
        for x in nums:
            pre_sum += x
            if pre_sum - k in set_dd:
                ans += set_dd[pre_sum - k]
            set_dd[pre_sum] += 1
        return ans


print(Solution1().subarraySum([1, 1,1],2))
