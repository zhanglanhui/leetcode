#!/usr/bin/python3
from typing import List
from collections import OrderedDict


# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 使用hashmap
class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 1
        sets = set(nums)
        if not nums:
            return 0
        for x in sets:
            if x - 1 not in sets:
                flag, offset = True, 0
                while flag:
                    offset += 1
                    flag = False if x + offset not in sets else True
                max_len = max(offset, max_len)
        return max_len


print(Solution1().longestConsecutive([100, 4, 200, 1, 3, 2]))


# hash
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        num_set = set(nums)
        max_len = 1
        for num in nums:
            print(type(num))
            if num - 1 not in num_set:
                tmp = num
                while tmp in num_set:
                    tmp += 1
                max_len = max(max_len, tmp - num)
        return max_len


print(Solution2().longestConsecutive([-1, 0]))
