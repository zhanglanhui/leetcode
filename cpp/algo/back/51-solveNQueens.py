#!/usr/bin/python3
from typing import List
import functools


# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#  
#
# 示例 1：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/n-queens
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def backtrack(tmp):
            def is_not_valid(l, member):
                add_index = len(l)
                for index, x in enumerate(l):
                    sub = add_index - index
                    if member == x or x - sub == member or x + sub == member:
                        return True
                return False

            if len(tmp) == n:
                res = ["".join(["Q" if k == j else "." for k in range(0, n)]) for j in tmp]
                ans.append(res[:])
                return
            for x in range(0, n):  # 列
                if tmp and is_not_valid(tmp, x):
                    continue
                tmp.append(x)
                backtrack(tmp)
                tmp.pop()

        backtrack([])
        return ans


print(Solution1().solveNQueens(4))
