#!/usr/bin/python3
from typing import List
import functools


# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
#
# 如果数组元素个数小于 2，则返回 0。
#
# 示例 1:
#
# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-gap
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        pass