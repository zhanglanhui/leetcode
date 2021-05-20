#!/usr/bin/python3
from typing import List
import functools
from collections import defaultdict


# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#  
#
# 示例 1：
#
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 深度优先搜索
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[i]) and grid[x][y] == "1":
                    dfs(x, y)
            islands[tuple([i, j])] = island_num
            return

        island_num = 0
        islands = defaultdict()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and tuple([i, j]) not in islands:
                    island_num += 1
                    dfs(i, j)
        return island_num

# 广度优先搜索
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands



print(Solution().numIslands(grid=
    [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
))
