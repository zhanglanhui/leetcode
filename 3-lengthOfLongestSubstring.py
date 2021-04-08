#!/usr/bin/python3
from typing import List
import functools


# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        f,e=0,1
        m=1
        while e<len(s):
            s[f:e]
        return e-f


print(Solution1().lengthOfLongestSubstring("abcabcbb"))