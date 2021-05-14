#!/usr/bin/python3
from typing import List
import functools


# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 进阶：
#
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#  
#
# 示例 1：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchR(i):
            p1 = p2 = i
            while p1 >= 0:
                if nums[p1] != target:
                    break
                p1 -= 1
            while p2 < len(nums):
                if nums[p2] != target:
                    break
                p2 += 1
            return [min(p1 + 1, len(nums) - 1), min(max(p2 - 1, 0), len(nums) - 1)]

        size = len(nums)
        l, h = 0, size - 1
        ttt = -1
        while l <= h:
            mid = l + (h - l) // 2
            if nums[mid] == target:
                ttt = mid
                break
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                h = mid - 1
        return [-1, -1] if ttt < 0 else searchR(ttt)


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchR(is_low: bool):
            size = len(nums)
            l, h = 0, size - 1
            while l <= h:
                if l == h: return l
                mid = l + (h - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                if nums[mid] > target:
                    h = mid - 1
                if nums[mid] == target:
                    if is_low:
                        h = mid
                        if nums[mid - 1] == target:
                            h = mid - 1
                        else:
                            return h
                    else:
                        l = mid
                        if nums[mid + 1] == target:
                            l = mid + 1
                        else:
                            return l
            return l

        if not nums: return [-1, -1]
        l = searchR(True)
        r = searchR(False)
        if nums[l] != target or nums[r] != target:
            return [-1, -1]
        return [l, r]


print(Solution2().searchRange(nums=[2, 2], target=2))
