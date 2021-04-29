#!/usr/bin/python3
from typing import List
import functools

# from bitarray import bitarray
#
# #初始化一个有10个bit位的数组，初始值为0
# a = bitarray(10)
#
# #可以像操作list一样操作bitarray对象
# a[1:8] = 1
#
# #bitarray还提供了一些特殊的方法，如：all()
# #当bitarray中所有的元素都为1时，all()返回为True
# if a.all():
#     print("all bits are True.")

# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 231.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/hamming-distance
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


print(Solution1().hammingDistance(1, 4))
