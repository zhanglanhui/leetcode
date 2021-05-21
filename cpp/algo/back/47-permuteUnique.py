#!/usr/bin/python3
from typing import List
import functools


# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# 示例 2：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
#
# 提示：
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
# 通过次数165,850提交次数262,457
# 请问您在哪类招聘中遇到此题？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# back+hash
class Solution1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(tmp):
            if len(tmp) == n:
                ans.add(tuple([x[1] for x in tmp[:]]))
                return
            for idx, x in enumerate(nums):
                if (idx, x) in set(tmp):
                    continue
                tmp.append((idx, x))
                backtrack(tmp)
                tmp.pop()

        n = len(nums)
        ans = set()
        backtrack([])
        return [list(x) for x in ans]


# back+hash
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(tmp):
            if len(tmp) == n:
                ans.append([x[1] for x in tmp[:]])
                return
            for idx, x in enumerate(nums):
                if set([(kk, x) for kk in range(idx + 1)]).intersection(set(tmp)):
                    continue
                tmp.append((idx, x))
                backtrack(tmp)
                tmp.pop()

        nums.sort()
        n = len(nums)
        ans = []
        backtrack([])
        return ans


print(Solution2().permuteUnique([1, 1, 2]))
