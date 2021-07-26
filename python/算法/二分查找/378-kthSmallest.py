#!/usr/bin/python3
from typing import List
import functools


# 给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
#
#  
#
# 示例 1：
#
# 输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# 输出：13
# 解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 归并
class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pass


# 二分查找
# 非常巧妙
class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


print(Solution2().kthSmallest(matrix=[[1, 5, 9], [13, 14, 17], [15, 15, 15]], k=4))
