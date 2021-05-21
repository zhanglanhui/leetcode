# !/usr/bin/python3
from typing import List
import functools


# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
#  
#
# 进阶：
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
#  
#
# 示例 1:
#
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotate-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rrr(numsss, start, end):
            p1, p2 = start, end
            while p1 <= p2:
                numsss[p1], numsss[p2] = numsss[p2], numsss[p1]
                p1 += 1
                p2 -= 1
            return

        size = len(nums)
        kk = k % size
        if kk == 0:
            return
        mid = size - kk
        rrr(nums, 0, mid - 1)
        rrr(nums, mid, size - 1)
        rrr(nums, 0, size - 1)
        return


nums = [1, 2, 3, 4, 5, 6, 7]
print(Solution().rotate(nums=nums, k=2))
print(nums)
