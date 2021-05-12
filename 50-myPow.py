#!/usr/bin/python3
from typing import List
import functools
from functools import reduce


# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
#
#  
#
# 示例 1：
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/powx-n
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 暴力解法，内存太大
class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        abs_n = abs(n)
        ans = reduce(lambda x, y: x * y, [x] * abs_n)
        return ans if n > 0 else 1 / ans


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        ans, abs_n, tmp = 1, abs(n), x
        while abs_n > 1:
            if 1 == abs_n % 2:
                ans = ans * tmp
            tmp = tmp * tmp
            abs_n = abs_n // 2
        ans = ans * tmp
        return ans if n > 0 else 1 / ans


print(Solution2().myPow(0.1, 555555))
