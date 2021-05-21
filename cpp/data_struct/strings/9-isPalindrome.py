#!/usr/bin/python3
from typing import List
import functools


# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
#
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
#
#  
#
# 示例 1：
#
# 输入：x = 121
# 输出：true
# 示例 2：
#
# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 使用字符串，two_point
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x_str = str(x)
        p1, p2 = 0, len(x_str) - 1
        while p1 <= p2:
            if x_str[p1] != x_str[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True


# 反转一半数字
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        sub_num = x
        pal_num = 0
        while sub_num > pal_num:
            tmp = sub_num % 10
            pal_num = 10 * pal_num + tmp
            print(sub_num)
            sub_num = sub_num // 10
        print(sub_num)
        if sub_num == pal_num:
            return True
        if pal_num > sub_num:
            return pal_num // 10 == sub_num
        return False


print(Solution2().isPalindrome(10))
