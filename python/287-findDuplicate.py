#!/usr/bin/python3
from typing import List
import functools


# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
#
# 假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-the-duplicate-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        xx = set(range(1, len(nums)))
        for x in nums:
            if x in xx:
                xx.remove(x)
            else:
                return x
        return -1


print(Solution1().findDuplicate([1, 3, 4, 2, 2]))
