#!/usr/bin/python3
from typing import List
import functools


# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#  
#
# 示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
# 示例 2：
#
# 输入：matrix = []
# 输出：0
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximal-rectangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass


print(Solution().maximalRectangle(
    matrix=[["1", "1", "1", "0", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "0", "1", "1"],
            ["1", "0", "0", "1", "0"]]))
