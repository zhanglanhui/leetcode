#!/usr/bin/python3
from typing import List


# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(i):
            l, r = 0, col - 1
            while l < r - 1:
                mid = l + (r - l) // 2
                if matrix[i][r] == target:
                    return r, r, True
                if matrix[i][l] == target:
                    return l, l, True
                if matrix[i][mid] == target:
                    return mid, mid, True
                if matrix[i][mid] > target:
                    r = mid
                if matrix[i][mid] < target:
                    l = mid
            return 0, min(l + 1, col - 1), False

        if not matrix or matrix[0][0] > target or matrix[-1][-1] < target: return False
        i = j = 0
        row, col = len(matrix), len(matrix[0])
        ans = False
        while i < row:
            if matrix[i][0] > target or matrix[i][-1] < target:
                i += 1
            else:
                break
        a, b, c = search(i)
        if c: return True
        for x in range(a, b + 1):
            l, r = i, row - 1
            while l <= r:
                mid = l + (r - l) // 2
                if matrix[mid][x] == target or matrix[l][x] == target or matrix[r][x] == target: return True
                if matrix[mid][x] > target: r = mid - 1
                if matrix[mid][x] < target: l = mid + 1
        return ans

# 官方题解
class Solution2:
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical:  # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else:  # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True

        return False

    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True

        return False




print(Solution().searchMatrix([[1], [3], [5]], 1))
