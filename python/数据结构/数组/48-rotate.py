#!/usr/bin/python3
from typing import List
import functools


# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
#
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotate-image
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 做矩阵的上下调换
        p1 = 0
        p2 = len(matrix) - 1
        n = len(matrix)
        while p1 <= p2:
            matrix[p1], matrix[p2] = matrix[p2], matrix[p1]
            p1 += 1
            p2 -= 1
        # 矩阵对称变换
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().rotate(matrix))
print(matrix)
