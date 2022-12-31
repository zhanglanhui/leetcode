#!/usr/bin/python3
from typing import List


# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(tmp, start, size):
            if len(tmp) == size:
                ans.append(list(tmp))
            for i, x in enumerate(nums[start:]):
                if x in tmp:
                    continue
                tmp.add(x)
                dfs(tmp, i + start, size)
                tmp.remove(x)
            return

        ans = []
        if not nums: return ans
        for l in range(len(nums) + 1):
            dfs(set(), 0, l)
        return ans


print(Solution().subsets(nums=[1, 2, 3]))


class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(num, l, h):
            # print(h)
            # if h==len(nums):
            #
            if len(num) >= h:
                out.append(list(num))
                return
            # if
            for i, x in enumerate(nums[l:]):
                if x in num:
                    continue
                num.append(x)
                backtrack(num, i + l, h)
                num.pop()

        # tmp = []
        out = []
        for x in range(0, len(nums)):
            backtrack([], 0, x)
        out.append(nums)
        return out


print(Solution1().subsets(nums=[1, 2, 3, 4]))
