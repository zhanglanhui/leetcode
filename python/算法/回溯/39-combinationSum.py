#!/usr/bin/python3
from typing import List
import functools


# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1：
#
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(tmp):
            if sum(tmp) > target:
                return
            if sum(tmp) == target:
                ans.append(tmp[:])
                return
            for x in candidates:
                if tmp and x < tmp[-1]:
                    continue
                tmp.append(x)
                backtrack(tmp)
                tmp.pop()

        backtrack([])
        return ans


print(Solution1().combinationSum([2, 6, 3, 7], 7))
