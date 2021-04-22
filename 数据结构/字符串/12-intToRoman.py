#!/usr/bin/python3
from typing import List
import functools


# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/integer-to-roman
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution1:
    def intToRoman(self, num: int) -> str:
        normal_dict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        others_dict = {
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
        }
        ans = []
        while num > 0:
            for cut in [1000, 100, 10, 1]:
                if num > cut:
                    times = num // cut
                    step = times * cut
                    others = others_dict.get(step)
                    if others:
                        ans.append(others)
                        num -= step
                    elif num >= 5 * cut:
                        ans.append(normal_dict[5 * cut])
                        num -= 5 * cut
                    else:
                        ans.append(times * normal_dict[cut])
                        num -= step
                    break
        return "".join(ans)


# 贪心解法，官方做法
class Solution2:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                  (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        roman_digits = []
        # Loop through each symbol.
        for value, symbol in digits:
            # We don't want to continue looping if we're done.
            if num == 0: break
            count, num = divmod(num, value)
            # Append "count" copies of "symbol" to roman_digits.
            roman_digits.append(symbol * count)
        return "".join(roman_digits)


print(Solution1().intToRoman(3))
