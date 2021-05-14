#!/usr/bin/python3
from typing import List
import functools


# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# TODO:暴力解法，先生成z形矩阵，然后按照顺序读出来
class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        if l <= numRows or numRows <= 1:
            return s
        mat = []
        for ind, x in enumerate(s):
            mod = ind % (numRows + numRows - 2)
            if not mod:
                mat.append([])
            if mod >= numRows:
                ttt = [""] * numRows
                ttt[numRows - (mod - numRows) - 2] = x
                mat.append(ttt)
            else:
                mat[-1].append(x)
        out = []
        for x in range(0, numRows):
            for y in mat:
                if x < len(y) and y[x]:
                    out.append(y[x])
        return "".join(out)


# 方法一：按行排序
# 简易做法
# https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/
# 思路
#
# 通过从左向右迭代字符串，我们可以轻松地确定字符位于 Z 字形图案中的哪一行。
class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)


# 方法二：按行访问
# 思路
# 按照与逐行读取 Z 字形图案相同的顺序访问字符串。
class Solution3:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        ret, l, cycleLen = [], len(s), 2 * (numRows - 1)
        for x in range(0, numRows):
            p1, p2 = x, -x
            while p1 < l:
                ret.append(s[p1])
                p2 += cycleLen
                if 0 < p2 < l and 0 < x < numRows - 1:
                    ret.append(s[p2])
                p1 += cycleLen
        return "".join(ret)

print(Solution1().convert("PAYPALISHIRING", 4))
print(Solution2().convert("PAYPALISHIRING", 4))
print(Solution3().convert("PAYPALISHIRING", 4))
