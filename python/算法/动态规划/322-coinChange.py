#!/usr/bin/python3
from typing import List
import functools


# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 你可以认为每种硬币的数量是无限的。
#
#  
#
# 示例 1：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/coin-change
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 超时了
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(tmp: List[int], count):
            if count == amount:
                ret.append(len(tmp[:]))
                return
            for x in coins:
                if x + count > amount:
                    continue
                if x + count == amount:
                    if ret:
                        ret.append(min(len(tmp[:]) + 1, ret[-1]))
                    else:
                        ret.append(len(tmp[:]) + 1)
                    return
                if (ret and len(tmp) + 1 >= ret[-1]):
                    return
                tmp.append(x)
                dfs(tmp, count + x)
                tmp.pop()
            return

        if 0 == amount:
            return 0
        if min(coins) > amount:
            return -1
        coins.sort(reverse=True)
        ret = []
        dfs([], 0)
        return min(ret) if ret else -1


# 动态规划
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


print(Solution2().coinChange(coins=[1, 2, 5], amount=210))
