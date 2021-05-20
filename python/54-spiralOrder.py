#!/usr/bin/python3
from typing import List
import functools
from collections import defaultdict


# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
#  
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/spiral-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 模拟
class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        ans, history_path = [], set()
        col_flag = False
        chang_times = 0
        last_i, last_j = 0, 0
        r, c = len(matrix), len(matrix[0])
        while len(history_path) < r * c:
            i, j = last_i, last_j
            while 0 <= i < r and 0 <= j < c:
                tmp = tuple([i, j])
                if tmp not in history_path:
                    last_i, last_j = i, j
                    ans.append(matrix[i][j])
                    history_path.add(tmp)
                if chang_times % 4 < 2:
                    j = j + 1 if not col_flag else j
                    i = i + 1 if col_flag else i
                else:
                    j = j - 1 if not col_flag else j
                    i = i - 1 if col_flag else i
            col_flag = ~col_flag
            chang_times += 1
        return ans


# 按层模拟
class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1


print(Solution2().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
