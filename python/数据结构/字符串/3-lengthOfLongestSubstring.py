#!/usr/bin/python3
from typing import List
import functools


# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


# 暴力解法
# 执行用时：# 372 ms# , 在所有 Python3 提交中击败了# 14.36%# 的用户
# 内存消耗：# 15 MB# , 在所有 Python3 提交中击败了# 42.82%# 的用户
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        p, ret = 0, 1
        while p < len(s):
            tmp, xxx = dict(), 0
            for x in s[p:]:
                if x in tmp:
                    break
                else:
                    tmp[x] = 0
                    xxx += 1
            ret = xxx if xxx > ret else ret
            p += 1
        return ret


# 优化1：利用双指针
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        lookup = set()
        left, max_len, cur_len = 0, 0, 0
        for c in s:
            cur_len += 1
            if c in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
                continue
            if cur_len > max_len: max_len = cur_len
            lookup.add(c)
        return max_len


print(Solution2().lengthOfLongestSubstring("auag"))


# 优化1：利用双指针
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        p, ans = 0, 1
        lookup = dict()
        for ind, x in enumerate(s):
            if x in lookup and lookup[x] >= p:
                p = lookup[x] + 1
                lookup.pop(x)
            lookup[x] = ind
            ans = max(ans, ind - p + 1)
        return ans


print(Solution3().lengthOfLongestSubstring("abcabcbb"))
