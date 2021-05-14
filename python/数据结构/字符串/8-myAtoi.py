#!/usr/bin/python3
from typing import List
import functools


# 请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
#
# 函数 myAtoi(string s) 的算法如下：
#
# 读入字符串并丢弃无用的前导空格
# 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
# 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
# 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
# 如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
# 返回整数作为最终结果。
# 注意：
#
# 本题中的
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/string-to-integer-atoi
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s: return 0
        numeral_set = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        # 判断前置空格
        j = 0
        for x in s:
            if x == " ":
                j += 1
            else:
                break
        # 判断符号
        if j >= len(s):
            return 0
        sign = True
        if s[j] in ("-", "+"):
            sign = False if s[j] == "-" else True
            j += 1
        tmp = []
        for x in s[j::]:
            if x in numeral_set:
                tmp.append(int(x))
            else:
                break
        ans = sum([value * (10 ** order) for order, value in enumerate(tmp[::-1]) if value != 0])
        return min(2 ** 31 - 1, ans) if sign else max(-ans, -2 ** 31)


print(Solution().myAtoi("   "))
