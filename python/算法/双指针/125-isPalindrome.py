class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            while p1 < p2:
                tmp = s[p1].lower()
                if 0 <= ord(tmp) - ord("0") <= 9 or 0 <= ord(tmp) - ord("a") <= 25:
                    break
                p1 += 1
            while p1 < p2:
                tmp = s[p2].lower()
                if 0 <= ord(tmp) - ord("0") <= 9 or 0 <= ord(tmp) - ord("a") <= 25:
                    break
                p2 -= 1
            if p1 == p2:
                return True
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True


print(ord("0"))
print(ord("A") - ord("a"))
print(Solution().isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))
