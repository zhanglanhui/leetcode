# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#  
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/edit-distance
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word2: return len(word1)
        if not word1: return len(word2)
        w1, w2 = word1, word2
        size1, size2 = len(w1), len(w2)
        dp = [[0] * size1 for _ in range(size2)]
        for i, k in enumerate(w1):
            dp[0][i] = i if w2[0] in w1[:i + 1] else i + 1
        for i, k in enumerate(w2):
            dp[i][0] = i if w1[0] in w2[:i + 1] else i + 1
        for j in range(1, size1):
            for i in range(1, size2):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + int(word1[j] != word2[i]))
        return dp[-1][-1]


print(Solution().minDistance(word1 = "intention", word2 = "execution"))
