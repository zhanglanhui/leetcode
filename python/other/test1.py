class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        ans = ""
        max_len = 0
        dp = [[False] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = True
            if 1 > max_len:
                ans = s[i:i + 1]
                max_len = 1
        # for i in range(size - 1):
        #     if s[i] == s[i + 1]:
        #         dp[i][i + 1] = True
        #         if 3 > max_len:
        #             ans = s[i:i + 2]
        #             max_len = 2
        for i in range(size):
            for j in range(i, size):
                if j == i or (j == i + 1 and s[i] == s[j]):
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        ans = s[i:j + 1]
                        max_len = j - i + 1
        for win in range(2,size):
            for i in range(0, size):
                # if win ==0 or (win == 1 and s[i] == s[j]):
                #     dp[i][j] = True
                #     if j - i + 1 > max_len:
                #         ans = s[i:j + 1]
                #         max_len = j - i + 1
                # if j - 1 >= i + 1 and s[i] == s[j] and dp[i + 1][j - 1]:
                #     dp[i][j] = True
                #     if j - i + 1 > max_len:
                #         ans = s[i:j + 1]
                #         max_len = j - i + 1
                pass
        return ans


print(Solution().longestPalindrome("aaaaa"))
