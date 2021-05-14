#!/usr/bin/python3
from typing import List
import functools


#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
# 通过次数309,062提交次数397,086
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 回溯法
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(tmp):
            if len(tmp) == n:
                ans.append(tmp[:])
                return
            for x in nums:
                if x in set(tmp):
                    continue
                tmp.append(x)
                backtrack(tmp)
                tmp.pop()

        n = len(nums)
        ans = []
        backtrack([])
        return ans
        # def backtrack(first=0):
        #     # 所有数都填完了
        #     if first == n:
        #         res.append(nums[:])
        #     for i in range(first, n):
        #         # 动态维护数组
        #         nums[first], nums[i] = nums[i], nums[first]
        #         # 继续递归填下一个数
        #         backtrack(first + 1)
        #         # 撤销操作
        #         nums[first], nums[i] = nums[i], nums[first]
        #
        # n = len(nums)
        # res = []
        # backtrack()
        # return res


print(Solution1().permute([1, 2, 3]))
