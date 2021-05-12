# 二分法
class Solution1:
    def pow(self, x, n):
        return x ** n

    def mySqrt(self, x: int) -> int:
        if x <= 0: return 0
        if x <= 3: return 1
        n = 0
        while True:
            if self.pow(2, n) >= x:
                break
            else:
                n += 1
        low, high = self.pow(2, (n - 1) // 2), self.pow(2, (n // 2) + 1)
        while low < high - 1:
            mid = low + (high - low) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid
            else:
                low = mid
        return low


# 牛顿法
class Solution2:
    def mySqrt(self, x: int) -> int:
        if x <= 0: return 0
        if x <= 3: return 1
        ans = 1
        while abs(x - ans * ans) > 0.5:
            ans = float(ans * ans + x) / (2 * ans)
        return int(ans)


print(Solution2().mySqrt(1836583659))
