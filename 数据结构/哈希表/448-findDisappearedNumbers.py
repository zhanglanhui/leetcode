#!/usr/bin/python3
from typing import List
import functools


# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
#
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
#
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
#
# 示例:
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 行用时：# 88 ms# , 在所有 Python3 提交中击败了# 100.00%# 的用户
# 内存消耗：# 22.9 MB# , 在所有 Python3 提交中击败了# 37.39%# 的用户
class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if 0 == len(nums):
            return []
        size = len(nums)
        xx = set(range(1, size + 1))
        for n in nums:
            if n in xx:
                xx.remove(n)
        return list(xx)


print(Solution1().findDisappearedNumbers([1, 2, 2, 3, 5, 4, 1]))
