#!/usr/bin/python3
from typing import List
import functools


# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
#  
#
# 示例 1：
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-prefix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 暴力解法，方法一：横向扫描
class Solution1:

    def getPrefix(self, a, b):
        p, length = 0, min(len(a), len(b))
        while p < length and a[p] == b[p]:
            p += 1
        return a[:p]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        ans = strs[0]
        for str in strs[1:]:
            ans = Solution1().getPrefix(ans, str)
            if not ans:
                return ans
        return ans


# 方法二：纵向扫描,做法与上类似


# 方法三：分治实际上就是将数组拆分计算前缀后合并
class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(a, start, end):
            if start == end:
                return a[start]
            p, mid = 0, (end + start) // 2
            (x, y) = (lcp(a, start, mid), lcp(a, mid + 1, end)) if end - start >= 2 else (a[start], a[end])
            length = min(len(x), len(y))
            while p < length and x[p] == y[p]:
                p += 1
            return x[:p]

        return "" if not strs else lcp(strs, 0, len(strs) - 1)


print(Solution3().longestCommonPrefix(["flower", "flow", "flight"]))
