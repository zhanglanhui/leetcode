#!/usr/bin/python3
from typing import List
import functools


# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
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
# 链接：https://leetcode-cn.com/problems/remove-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 这道题原本想法是用尾部的数据替换需要remove的数字,做法太复杂了
class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        p1, p2 = 0, len(nums) - 1
        while val == nums[p2] and p2 >= 0:
            p2 -= 1
        if p2 < 0:
            nums[:] = []
            return 0
        while p1 <= p2:
            if val == nums[p1]:
                while val == nums[p2] and p1 < p2:
                    p2 -= 1
                if p1 == p2:
                    break
                nums[p1] = nums[p2]
                p2 -= 1
            p1 += 1
        nums[:] = nums[:p1]
        return p1


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        for x in nums:
            if x != val:
                p += 1
                nums[p] = x
        nums[:] = nums[:p]
        return p


a = [2, 3, 2, 3, 4, 2, 2, 2]
print(Solution1().removeElement(a, 2))
print(a)
