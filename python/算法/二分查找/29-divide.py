#!/usr/bin/python3
from typing import List
import functools


# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
#
#  
#
# 示例 1:
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/divide-two-integers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def divide(self, dividend: int, divisor: int) -> int:
        xxx = 1 << 31
        ggg = xxx - 1
        sign = True if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else False
        dividend_abs, divisor_abs = abs(dividend), abs(divisor)
        if 0 == dividend_abs or dividend_abs < divisor_abs:
            return 0
        if dividend_abs == divisor_abs:
            return 1 if sign else -1
        if divisor_abs == 1:
            ans = min(dividend_abs, ggg)
            return ans if sign else -dividend_abs
        dividend2, ans = dividend_abs, 0
        while True:
            times, cut = 1, divisor_abs
            while True:
                tmp = cut << 1
                if tmp > dividend2:
                    break
                cut = tmp
                times = times << 1
            dividend2 = dividend2 - cut
            ans += times
            if dividend2 < divisor_abs:
                break
            if dividend2 < divisor_abs + divisor_abs:
                ans += 1
                break
        aaa = ans if sign else -ans
        return min(aaa, ggg) if sign else aaa


# 2147483647
# 2
print(Solution1().divide(2147483647, 2))
