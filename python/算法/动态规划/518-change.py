#!/usr/bin/python3
from typing import List
import functools


# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
#
#  
#
# 示例 1:
#
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 示例 2:
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/coin-change-2
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         if amount == 0: return 0
#         min_coin = min(coins)
#         dp = [0] * (amount + 1)
#         dp[0] = 1
#         dp[min_coin] = 1
#         for i in range(min_coin + 1, amount + 1):
#             tmp = [dp[i - j] for j in coins if j<=i]
#             dp[i] = sum(tmp)
#         print(dp)
#         return dp[-1]


class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
                # if x==2:
                #     print(dp)
        # print(dp)
        return dp[amount]


print(Solution1().change(amount=5, coins=[1, 2, 5]))
