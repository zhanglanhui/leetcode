#!/usr/bin/python3
from typing import List
import functools


# 已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
#
# 不要使用系统的 Math.random() 方法。
#
#  
#
# 示例 1:
#
# 输入: 1
# 输出: [7]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-rand10-using-rand7
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# The rand7() API is already defined for you.
def rand7():
    return 1


# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        k = 0
        while k < 40:
            k = 7 * (rand7() - 1) + rand7()
        return (k - 39)



class Solution2:
    def rand10(self):
        """
        :rtype: int
        """
        k = 41
        while k > 40:
            k = 7 * (rand7() - 1) + rand7()
        return 1+(k - 1)//4
