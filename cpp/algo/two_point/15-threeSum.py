#!/usr/bin/python3
from typing import List
import functools


# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#  
#
# 示例 1：
#
# 输入：nu
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], target):
            if 0 == len(nums):
                return []
            tmp = dict()
            ans = []
            for ind, n in enumerate(nums):
                if target - n in tmp:
                    ans.append(sorted([-target, n, target - n]))
                tmp[n] = ind
            return ans

        if not nums or len(nums) < 3:
            return []
        nums_set = {-x for x in nums}
        ans = []
        for x in nums_set:
            aa = nums.copy()
            aa.remove(-x)
            ans.extend(twoSum(aa, x))
        return ans


# TODO:这个问题就是没有办法去重

print(Solution1().threeSum([-1, 0, 1, 2, -1, -4]))


# sort+two_point
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if not nums or len(nums) < 3:
            return ans
        nums.sort()
        for p1 in range(len(nums) - 1):
            if p1 != 0 and nums[p1 - 1] == nums[p1]:
                continue
            target1 = -nums[p1]
            p3 = len(nums) - 1
            for p2 in range(p1 + 1, len(nums) - 1):
                if p2 != p1 + 1 and nums[p2 - 1] == nums[p2]:
                    continue
                target2 = nums[p2]
                while p3 > p2 and target2 + nums[p3] > target1:
                    p3 -= 1
                if p3 > p2 and target1 == target2 + nums[p3]:
                    ans.append([-target1, target2, nums[p3]])
                if p3 == p2:
                    break
        return ans


print(Solution2().threeSum([-1, 0, 1, 2, -1, -4]))
