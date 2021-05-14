#!/usr/bin/python3
from typing import List
import functools
from functools import reduce


# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 示例 2:
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(tmp, start):
            sum_num = sum(tmp) if tmp else 0
            if sum_num == target:
                ans.add(tuple(tmp[:]))
                return
            if sum_num > target:
                return
            for ind, x in enumerate(candidates[start::]):
                if sum_num + x > target:
                    continue
                tmp.append(x)
                backtrack(tmp, ind + start + 1)
                tmp.pop()

        if sum(candidates) < target: return []
        if sum(candidates) == target: return [candidates]
        candidates.sort()
        ans = set()
        start = 0
        backtrack([], start)
        return [list(x) for x in ans]


print(Solution().combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27))
