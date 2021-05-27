#!/usr/bin/python3
from typing import List
import functools


# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
#
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
#
#  
#
# 示例 1：
#
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        size = len(triangle)
        if size <= 1: return triangle[0][0]
        dp = [[0] * len(x) for x in triangle]
        for i, x in enumerate(triangle):
            for j, y in enumerate(x):
                if i == 0: dp[i][j] = y
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + y
                elif j >= len(x) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + y
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + y
        return min(dp[-1])


print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
