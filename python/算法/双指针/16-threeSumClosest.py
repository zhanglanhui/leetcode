#!/usr/bin/python3
from typing import List


# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#  
#
# 示例：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        nums.sort()
        ans, close_num = 0, float('inf')
        for p1 in range(size - 2):
            if p1 > 0 and nums[p1 - 1] == nums[p1]:
                continue
            p2 = p1 + 1
            p3 = size - 1
            while p2 < p3:
                adds = nums[p1] + nums[p2] + nums[p3]
                sub = abs(target - adds)
                if sub == 0: return adds
                if close_num > sub:
                    close_num = sub
                    ans = adds
                if adds < target:
                    tmp = p2 + 1
                    while tmp + 1 < p3 and nums[tmp] == nums[p2]:
                        tmp += 1
                    p2 = tmp
                if adds > target:
                    tmp = p3 - 1
                    while p2 < tmp - 1 and nums[tmp] == nums[p3]:
                        tmp -= 1
                    p3 = tmp
        return ans


print(Solution().threeSumClosest([3, 4, 5, 5, 7],
                                 13))
