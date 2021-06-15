#!/usr/bin/python3
from typing import List
import functools


# 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
#
# B.length >= 3
# 存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
#
# 给出一个整数数组 A，返回最长 “山脉” 的长度。
#
# 如果不含有 “山脉” 则返回 0。
#
#  
#
# 示例 1：
#
# 输入：[2,1,4,7,3,2,5]
# 输出：5
# 解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
# 示例 2：
#
# 输入：[2,2,2]
# 输出：0
# 解释：不含 “山脉”。
#  
#
# 提示：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-mountain-in-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) <= 2: return 0
        ans = 0
        hash_set = dict()
        i = 0
        while i < len(arr) - 1:
            if arr[i + 1] > arr[i]:
                j = i
                while j < len(arr) - 1 and arr[j + 1] > arr[j]:
                    j += 1
                hash_set[j] = j - i + 1
                i = j
            i += 1
        i = len(arr) - 1
        while i >= 1:
            if arr[i - 1] > arr[i]:
                j = i
                while j >= 1 and arr[j - 1] > arr[j]:
                    j -= 1
                if j in hash_set:
                    ans = max(ans, i - j + hash_set[j])
                i = j
            i -= 1
        return ans


print(Solution().longestMountain([2, 1, 4, 7, 3, 2, 5]))
