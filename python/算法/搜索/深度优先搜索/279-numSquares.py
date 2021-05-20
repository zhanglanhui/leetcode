# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#
#  
#
# 示例 1：
#
# 输入：n = 12
# 输出：3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/perfect-squares
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 贪心枚举
import math


# 贪心 + BFS（广度优先搜索）
class Solution1:
    def numSquares(self, n: int) -> int:
        self.ans = float('inf')

        def dfs(tmp, ssss):
            if ssss == n:
                self.ans = min(self.ans, len(tmp))
                return
            if len(tmp) >= self.ans - 1:
                return
            for kk in gg:
                if kk + ssss > n:
                    continue
                tmp.append(kk)
                dfs(tmp, ssss + kk)
                tmp.pop()

        if n in set([i * i for i in range(1, 100)]): return 1
        gg = [i * i for i in range(1, int(math.sqrt(n)) + 1)][::-1]
        dfs([], 0)
        return int(self.ans)


# 动态规划 递归方式超时
class Solution2:
    def numSquares(self, n: int) -> int:
        self.ans = float('inf')

        def fffffffff(n2):
            if n2 in gg:
                return 1
            lll = [fffffffff(n2 - x) for x in gg if x < n2]
            return min(lll) + 1 if lll else 1

        gg = set([i * i for i in range(1, int(math.sqrt(n)) + 1)])
        if n in gg: return 1
        return fffffffff(n)

# 动态规划
class Solution21:
    def numSquares(self, n: int) -> int:
        gg = set([i * i for i in range(1, int(math.sqrt(n)) + 1)])
        if n in gg: return 1
        dp = [0] * (n+1)
        for x in range(1, n + 1):
            dp[x] = min([dp[x - k] for k in gg if x >= k]) + 1
        return dp[-1]


print(Solution21().numSquares(54))
