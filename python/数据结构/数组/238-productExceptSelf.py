#!/usr/bin/python3
from typing import List


# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
#  
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
#  
#
# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
#
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
# 进阶：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/product-of-array-except-self
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [0] * size
        tmp = 1
        for i, x in enumerate(nums[::-1]):
            res[i] = tmp
            tmp = tmp * x
        res = res[::-1]
        tmp = 1
        for i, x in enumerate(nums):
            res[i] = res[i] * tmp
            tmp = tmp * x
        return res


print(Solution().productExceptSelf([1, 2, 3, 4]))
