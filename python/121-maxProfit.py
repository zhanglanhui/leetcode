#!/usr/bin/python3
from typing import List
import functools


# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
#
#  
#
# 示例 1：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 暴力解法  超时
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        tmp = []
        for i, x in enumerate(prices):
            if i > 0:
                tmp.append(max([x - k for k in prices[:i]]))
        return max(max(tmp), 0)


# 优化
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_value = prices[0]
        max_profit = 0
        for x in prices[1:]:
            min_value = min(x, min_value)
            max_profit = max(max_profit, x - min_value)
        return max_profit


print(Solution2().maxProfit([3, 2, 3, 1, 2, 4, 5, 5, 6]))
