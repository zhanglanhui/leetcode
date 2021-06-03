#!/usr/bin/python3
from typing import List
import functools


# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#  
#
# 示例 1：
#
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 示例 2：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        is_in = False
        ans_tmp = 0
        ans = []
        last_num = min_price = prices[0]
        for x in prices[1:]:
            if is_in and x < last_num:
                ans.append(ans_tmp)
                ans_tmp = 0
                is_in = False
                min_price = x
            if x <= min_price:
                min_price = min(x, min_price)
            else:
                is_in = True
                last_num = x
                ans_tmp = max(ans_tmp, x - min_price)
        if ans_tmp > 0: ans.append(ans_tmp)
        ans.sort(reverse=True)
        print(ans)
        return sum(ans[:k])


print(Solution().maxProfit(k=2, prices=[1,2,4,2,5,7,2,4,9,0]))
