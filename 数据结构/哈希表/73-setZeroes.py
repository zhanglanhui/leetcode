#!/usr/bin/python3
from typing import List
from collections import OrderedDict


# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
#
# 进阶：
#
# 一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个仅使用常量空间的解决方案吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/set-matrix-zeroes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        d1, d2 = set(), set()
        for i, x in enumerate(matrix):
            for j, y in enumerate(x):
                if not y:
                    d1.add(i)
                    d2.add(j)
        for i, x in enumerate(matrix):
            for j, y in enumerate(x):
                if i in d1 or j in d2:
                    matrix[i][j] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(Solution1().setZeroes(matrix))
print(matrix)
