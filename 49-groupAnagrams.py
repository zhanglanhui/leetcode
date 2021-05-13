#!/usr/bin/python3
from typing import List


# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/group-anagrams
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        kk = defaultdict(list)
        for s in strs:
            tt = [0] * 26
            for x in s:
                tt[ord(x) - ord("a")]+=1
            kk[tuple(tt)].append(s)
        return list(kk.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
