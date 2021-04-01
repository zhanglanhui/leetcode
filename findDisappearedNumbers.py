#!/usr/bin/python3
from typing import List
import functools


# 行用时：# 88 ms# , 在所有 Python3 提交中击败了# 100.00%# 的用户
# 内存消耗：# 22.9 MB# , 在所有 Python3 提交中击败了# 37.39%# 的用户
class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if 0 == len(nums):
            return []
        size = len(nums)
        xx = set(range(1, size + 1))
        for n in nums:
            if n in xx:
                xx.remove(n)
        return list(xx)


print(Solution1().findDisappearedNumbers([1, 2, 2, 3, 5, 4, 1]))
