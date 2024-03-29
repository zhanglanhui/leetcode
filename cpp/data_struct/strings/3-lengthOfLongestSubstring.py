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
            while c in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            lookup.add(c)
        return max_len


print(Solution2().lengthOfLongestSubstring("au"))


# dict
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size <= 1: return size
        lo, hi = 0, 0
        pos_dic = dict()
        pos_dic[s[0]] = 0
        ans = 0
        for i, x in enumerate(s[1:]):
            if x not in pos_dic:
                pos_dic[x] = i + 1
                hi += 1
            else:
                lo = max(lo, pos_dic[x] + 1)
                # if lo >= hi:
                hi += 1
                # hi = max(hi, lo + 1)
                pos_dic[x] = i + 1
            # print(hi, lo,x)
            ans = max(ans, hi - lo + 1)
        return ans


print(Solution3().lengthOfLongestSubstring("pwwkew"))


# dict
class Solution4:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size <= 1: return size
        lo = 0
        pos_dic = dict()
        ans = 1
        for i, x in enumerate(s):
            if x in pos_dic:
                lo = max(lo, pos_dic[x] + 1)
            pos_dic[x] = i
            ans = max(ans, i - lo + 1)
        return ans


print(Solution4().lengthOfLongestSubstring("pwwkew"))
