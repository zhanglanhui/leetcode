#!/usr/bin/python3
from typing import List
import functools


# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
# https://leetcode-cn.com/problems/climbing-stairs/

# 递归
# 超出时间限制
class Solution1:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 加上缓存装饰器
# 执行用时：# 40 ms# , 在所有 Python3 提交中击败了# 57.93%# 的用户
# 内存消耗：# 14.6 MB# , 在所有 Python3 提交中击败了# 98.36%# 的用户
class Solution2:
    @functools.lru_cache(100)
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 斐波那契数列
# 执行用时：# 36 ms# , 在所有 Python3 提交中击败了# 81.01%# 的用户
# 内存消耗：# 14.8 MB# , 在所有 Python3 提交中击败了# 59.46%# 的用户
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        p, q, r = 1, 1, 0
        for x in range(0, n - 1):
            r = p + q
            p = q
            q = r
        return r


print(Solution2().climbStairs(10))
