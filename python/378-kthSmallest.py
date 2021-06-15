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


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pass


print(Solution().kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))