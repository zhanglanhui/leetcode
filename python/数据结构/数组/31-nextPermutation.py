#!/usr/bin/python3
from typing import List


# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须 原地 修改，只允许使用额外常数空间。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/next-permutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 首先从后向前查找第一个顺序对 (i,i+1)(i,i+1)，满足 a[i] < a[i+1]a[i]<a[i+1]。这样「较小数」即为 a[i]a[i]。此时 [i+1,n)[i+1,n) 必然是下降序列。
#
# 如果找到了顺序对，那么在区间 [i+1,n)[i+1,n) 中从后向前查找第一个元素 jj 满足 a[i] < a[j]a[i]<a[j]。这样「较大数」即为 a[j]a[j]。
#
# 交换 a[i]a[i] 与 a[j]a[j]，此时可以证明区间 [i+1,n)[i+1,n) 必为降序。我们可以直接使用双指针反转区间 [i+1,n)[i+1,n) 使其变为升序，而无需对该区间进行排序。
#
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size <= 1: return
        p1 = cut = 0
        while p1 < size - 1:
            if nums[p1] < nums[p1 + 1]:
                cut = max(cut, p1)
            p1 += 1
        if not cut and nums[cut] >= nums[cut + 1]:
            tmp1, tmp2 = 0, size - 1
            while tmp1 <= tmp2:
                nums[tmp1], nums[tmp2] = nums[tmp2], nums[tmp1]
                tmp1 += 1
                tmp2 -= 1
            return
        p2, value = cut, nums[cut]
        while p2 < size - 1:
            p2 += 1
            if nums[p2] > value:
                nums[p2], nums[cut] = nums[cut], nums[p2]
        return


# 官方题解
class Solution2:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


nums = [2, 3, 1]
Solution().nextPermutation(nums)
print(nums)


class Solution3:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums or len(nums) == 1: return
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        size = len(nums)
        i = size - 2
        while i >= 0:
            if nums[i] >= nums[i + 1]:
                i -= 1
            else:
                break
        if i >= 0:
            j = size - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]
        left, right = i + 1, size - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return


nums = [2, 3, 1]
Solution3().nextPermutation(nums)
print(nums)
