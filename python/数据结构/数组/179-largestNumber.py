#!/usr/bin/python3
from typing import List
import functools

# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
#
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#  
#
# 示例 1：
#
# 输入：nums = [10,2]
# 输出："210"
# 示例 2：
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
# 示例 3：
#
# 输入：nums = [1]
# 输出："1"
# 示例 4：
#
# 输入：nums = [10]
# 输出："10"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp1(x, y):
            str_x = str(x)
            str_y = str(y)
            p1 = p2 = 0
            while p1 < len(str_x) and p2 < len(str_y):
                if str_x[p1] == str_y[p2]:
                    p1 += 1
                    p2 += 1
                elif int(str_x[p1]) > int(str_y[p2]):
                    return 1
                else:
                    return -1
            return 1 if p1 == len(str_x) else -1

        tt = sorted(nums, key=cmp_to_key(lambda a, b: cmp1(a, b)), reverse=True)
        return "".join(map(str, tt))


print(Solution().largestNumber([3, 30, 34, 5, 9]))
