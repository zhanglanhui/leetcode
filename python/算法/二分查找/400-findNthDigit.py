#!/usr/bin/python3
from typing import List
import functools
from functools import reduce
from collections import defaultdict


# 给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位上的数字。
#
#  
#
# 示例 1：
#
# 输入：n = 3
# 输出：3
# 示例 2：
#
# 输入：n = 11
# 输出：0
# 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
#  
#
# 提示：
#
# 1 <= n <= 231 - 1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/nth-digit
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def findNthDigit(self, n: int) -> int:
        # # if n < 10: return n
        # weishu = 0
        # tmp = n
        # while tmp > 0:
        #     tmp = tmp - 9 * (weishu + 1) * 10 ** weishu
        #     weishu += 1
        # tmp = tmp + 9 * weishu * 10 ** (weishu - 1)
        # dd = tmp // weishu + 10 ** (weishu - 1) - 1
        # kk = tmp % weishu
        # pp = dd // (10 ** kk)
        # print(tmp, weishu, dd, kk, pp)
        # return pp % 10
        d, count = 1, 9
        while n > d * count:
            n -= d * count
            d += 1
            count *= 10
        index = n - 1
        start = 10 ** (d - 1)
        num = start + index // d
        digitIndex = index % d
        return num // 10 ** (d - digitIndex - 1) % 10


print(Solution().findNthDigit(10))
