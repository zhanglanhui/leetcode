#!/usr/bin/python3
from typing import List
import functools


# hash 暴力解法
# 执行用时：# 48 ms# , 在所有 Python3 提交中击败了# 74.42%# 的用户
# 内存消耗：# 16 MB# , 在所有 Python3 提交中击败了# 45.56%# 的用户
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        size = len(nums) / 2
        for k, v in dict(Counter(nums)).items():
            if v > size:
                return k


# sort
# 执行用时：# 40 ms# , 在所有 Python3 提交中击败了# 94.70%# 的用户
# 内存消耗：# 15.9 MB# , 在所有 Python3 提交中击败了# 91.51%# 的用户
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[int(len(nums) / 2)]


# 摩尔投票法
# Boyer-Moore 投票算法
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        # # 第一次尝试
        # tmp = [nums[0]]
        # for x in nums[1::]:
        #     if not tmp or x == tmp[0]:
        #         tmp.append(x)
        #     elif len(tmp) > 0:
        #         tmp = tmp[:-1]
        # return tmp[0]
        tmp, count = 0, 0
        for x in nums:
            if not count:
                tmp = x
            count += (1 if x == tmp else -1)
        return tmp


# 随机化
# 随机解法，比较另类
# 执行用时：# 52 ms# , 在所有 Python3 提交中击败了# 57.41%# 的用户
# 内存消耗：# 16.1 MB# , 在所有 Python3 提交中击败了# 32.94%# 的用户
class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        import random
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate


# TODO: 这个算法计算复杂度O（nlogn），需要理解下
class Solution5:
    def majorityElement(self, nums: List[int]) -> int:
        def majority_element_rec(lo, hi) -> int:
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)


print(Solution3().majorityElement([2, 2, 1, 1, 1, 2, 2]))
