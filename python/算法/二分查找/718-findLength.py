#!/usr/bin/python3
from typing import List
import functools


# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#
#  
#
# 示例：
#
# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
#  
#
# 提示：
#
# 1 <= len(
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 暴力解法
class Solution1:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        set1, set2 = set(nums1), set(nums2)
        if not set1.intersection(set2):
            return 0
        p1, window = 0, 0
        while p1 <= len(nums1) - window - 1:
            p2 = 0
            while p2 <= len(nums2) - window - 1:
                if nums2[p2: p2 + window + 1] != nums1[p1:p1 + window + 1]:
                    p2 += 1
                else:
                    window += 1
            p1 += 1
        return window


# 窗口解法
class Solution2:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def compare(ind1, ind2, length):
            ret = i = 0
            while i < length:
                if nums1[ind1 + i] != nums2[ind2 + i] and ret > 0:
                    break
                if nums1[ind1 + i] != nums2[ind2 + i] and ret == 0:
                    ind2 += 1
                    length -= 1
                    ret += 1
                    continue
                i += 1
                ret += 1
            return ret

        set1, set2 = set(nums1), set(nums2)
        if not set1.intersection(set2):
            return 0
        ret = 0
        l1, l2 = len(nums1), len(nums2)
        for i in range(l1):
            length = min(l2, l1 - i)
            ret = max(ret, compare(i, 0, length))
        for i in range(l2):
            length = min(l1, l2 - i)
            ret = max(ret, compare(0, i, length))
        return ret


# # 动态规划
# class Solution2:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:


print(Solution2().findLength([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]))
