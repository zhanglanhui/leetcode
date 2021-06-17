#!/usr/bin/python3
from typing import List
import functools


# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 动态规划
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans


# 中心扩展算法
# 执行用时：# 1168 ms# , 在所有 Python3 提交中击败了# 57.87%# 的用户
# 内存消耗：# 15 MB# , 在所有 Python3 提交中击败了# 63.12%# 的用户
class Solution2:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]


# 动态规划
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1: return s
        size = len(s)
        dp = [[False] * size for _ in range(size)]
        ans = s[0]
        for i in range(size):
            dp[i][i] = True
        for i in range(size - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = s[i:i + 2]
        for win in range(2, size):
            for j in range(0, size - win):
                if dp[j + 1][j + win - 1] and s[j] == s[j + win]:
                    dp[j][j + win] = True
                    if win + 1 > len(ans): ans = s[j:j + win + 1]
        return ans


# 动态规划
class Solution4:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(i, j):
            if i >= size or j >= size or s[i] != s[j]: return ""
            left, right = i - 1, j + 1
            while 0 <= left and right < size:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            return s[left + 1:right]

        if not s or len(s) == 1: return s
        size = len(s)
        ans = s[0]
        for i in range(size):
            one = expandAroundCenter(i, i)
            two = expandAroundCenter(i, i + 1)
            ans = one if len(one) > len(ans) else ans
            ans = two if len(two) > len(ans) else ans
        return ans


print(Solution4().longestPalindrome("abcbadd"))
