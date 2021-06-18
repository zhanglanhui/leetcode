#!/usr/bin/python3
from typing import List
import functools


# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[1 ,3 ,1] ,[1 ,5 ,1] ,[4 ,2 ,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * (len(grid[0])) for _ in range(len(grid))]
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if i == 0:
                    if j >= 1:
                        dp[i][j] = dp[i][j - 1] + grid[i][j]
                    else:
                        dp[i][j] = grid[0][0]
                else:
                    if j >= 1:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                    else:
                        dp[i][j] = dp[i - 1][j] + grid[i][j]
        return dp[-1][-1]


print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))


class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if i == 0 and j == 0:
                    dp[j][i] = grid[j][i]
                    continue
                if j == 0:
                    dp[j][i] = dp[j][i - 1] + grid[j][i]
                    continue
                if i == 0:
                    dp[j][i] = dp[j - 1][i] + grid[j][i]
                    continue
                dp[j][i] = min(dp[j - 1][i], dp[j][i - 1]) + grid[j][i]
        return dp[-1][-1]

print(Solution2().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
