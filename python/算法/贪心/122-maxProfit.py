# !/usr/bin/python3
from typing import List
import functools


# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#  
#
# 示例 1:
#
# 输入: prices = [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        is_in = False
        ans = ans_tmp = 0
        last_num = min_price = prices[0]
        for x in prices[1:]:
            if is_in and x < last_num:
                ans += ans_tmp
                ans_tmp = 0
                is_in = False
                min_price = x
            if x <= min_price:
                min_price = min(x, min_price)
            else:
                is_in = True
                last_num = x
                ans_tmp = max(ans_tmp, x - min_price)
        if ans_tmp > 0: ans += ans_tmp
        return ans


print(Solution().maxProfit([1, 2, 3, 5, 1, 2]))
