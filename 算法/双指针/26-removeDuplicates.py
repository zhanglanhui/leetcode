#!/usr/bin/python3
from typing import List
import functools


# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
#
#  
#
# 说明:
#
# 为什么返回数值是整数，但输出的答案是数组呢?
#
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
#
# 你可以想象内部操作如下:
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        if not nums:
            return length
        p1 = p2 = 1
        tmp = nums[0]
        while p2 < len(nums):
            if tmp != nums[p2]:
                tmp = nums[p1] = nums[p2]
                p1 += 1
            p2 += 1
        nums[p1:] = []
        return p1


a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution1().removeDuplicates(a))
print(a)
