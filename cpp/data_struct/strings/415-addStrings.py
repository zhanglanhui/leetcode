#!/usr/bin/python3
from typing import List
from collections import OrderedDict


# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
#  
#
# 提示：
#
# num1 和num2 的长度都小于 5100
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        l, carry = 1, 0
        ans = []
        while l <= l1 and l <= l2:
            tt = int(num1[l1 - l]) + int(num2[l2 - l]) + carry
            ans.append(str(tt % 10))
            carry = 1 if tt >= 10 else 0
            l += 1
        while l <= l1:
            tt = int(num1[l1 - l]) + carry
            ans.append(str(tt % 10))
            carry = 1 if tt >= 10 else 0
            l += 1
        while l <= l2:
            tt = int(num2[l2 - l]) + carry
            ans.append(str(tt % 10))
            carry = 1 if tt >= 10 else 0
            l += 1
        if carry > 0:
            ans.append("1")
        return "".join(ans[::-1])


print(Solution1().addStrings("99", "9"))
