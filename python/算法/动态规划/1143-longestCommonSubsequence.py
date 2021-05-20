# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
#
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
#
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
#
#  
#
# 示例 1：
#
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
# 示例 2：
#
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。
# 示例 3：
#
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from collections import defaultdict
        size1, size2 = len(text1), len(text2)
        set1, set2 = set(text1), set(text2)
        if not set1.intersection(set2): return 0
        dp = [(0, 0)] * min(size1, size2)
        t1 = text1 if size1 >= size2 else text2
        t2 = text1 if size2 > size1 else text2
        index = defaultdict(list)
        for i, x in enumerate(t1):
            index[x].append(i)
        for i, x in enumerate(t2):
            if x not in index:
                dp[i] = dp[i - 1] if i >= 1 else (0, 0)
            else:
                id = index[x]
                if i == 0 or dp[i - 1][0] == 0:
                    dp[i] = (1, min(id))
                    continue
                id_last = dp[i - 1][1]
                if id[-1] > id_last:
                    dp[i] = (dp[i - 1][0] + 1, min([i for i in id if i > id_last]))
                else:
                    dp[i] = (dp[i - 1][0], id[0]) if dp[i - 1][0] == 1 else dp[i - 1]
        return dp[-1][0]


print(Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))
