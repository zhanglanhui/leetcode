#!/usr/bin/python3
from typing import List


# Solution1
# 执行用时： 44 ms , 在所有 Python3 提交中击败了 39.48% 的用户
# 内存消耗： 14.9 MB , 在所有 Python3 提交中击败了# 39.90%# 的用户
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 0 == len(nums):
            return []
        tmp = dict()
        for ind, n in enumerate(nums):
            kk = tmp.get(target - n)
            if kk is not None:
                return [ind, kk]
            tmp[n] = ind


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 0 == len(nums):
            return []
        tmp = dict()
        for ind, n in enumerate(nums):
            if target - n in tmp:
                return [ind, tmp[target - n]]
            tmp[n] = ind


print(Solution2().twoSum([1, 2, 3], 4))
