#!/usr/bin/python3
from typing import List
import functools


# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
#  
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/median-of-two5-sorted-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 归并，合并有序数组
# 执行用时：# 60 ms# , 在所有 Python3 提交中击败了# 35.79%# 的用户
# 内存消耗：# 15.2 MB# , 在所有 Python3 提交中击败了# 14.34%# 的用户
# TODO:使用归并合并两个有序数组，时间复杂度O（m+n），空间复杂度O（m+n）
class Solution1:
    def swap(self, alist, blist, m, n):
        alist[m], alist[n] = blist[n], blist[m]

    @staticmethod
    def merge(alist, start, mid, end):
        blist = alist[start:end + 1]
        # print(blist)
        p1, p2, pos = 0, mid + 1 - start, start
        while pos <= end:
            if p1 == mid + 1 - start:
                alist[pos] = blist[p2]
                p2 += 1
            elif p2 == end + 1 - start:
                alist[pos] = blist[p1]
                p1 += 1
            elif blist[p1] <= blist[p2]:
                alist[pos] = blist[p1]
                p1 += 1
            elif blist[p1] > blist[p2]:
                alist[pos] = blist[p2]
                p2 += 1
            pos += 1

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = len(nums1), len(nums2)
        nums1.extend(nums2)
        Solution1.merge(nums1, 0, a - 1, a + b - 1)
        if (a + b) % 2:
            return nums1[(a + b) // 2]
        else:
            return (nums1[(a + b + 1) // 2] + nums1[(a + b - 1) // 2]) / 2


# # # merge test
a = [1, 2, 3, 4, -1, 1, 40, 60]
# print(a)
Solution1().merge(a, 0, 3, 7)
print(a)


# a = [1, 2, 3, 4]
# b = [-1, 1, 40, 60]
# print(Solution1().findMedianSortedArrays(a, b))


# 不需要合并两个有序数组，只要找到中位数的位置即可
# TODO:双指针方法
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = len(nums1), len(nums2)
        p1 = p2 = pos = 0
        if (a + b) % 2:
            tmp = 0
            # 合并后数组是奇数，只需要找到(a+b)//2的数值就可以
            while pos <= (a + b) // 2:
                if p1 == len(nums1):
                    tmp = nums2[p2]
                    p2 += 1
                elif p2 == len(nums2):
                    tmp = nums1[p1]
                    p1 += 1
                elif nums1[p1] <= nums2[p2]:
                    tmp = nums1[p1]
                    p1 += 1
                else:
                    tmp = nums2[p2]
                    p2 += 1
                pos += 1
            return tmp
        else:
            # 合并后数组是偶数，需要找到(a+b)//2，(a+b)//2+1的数值和一半
            tmp1 = tmp2 = 0
            while pos <= (a + b) // 2:
                tmp1 = tmp2
                if p1 == len(nums1):
                    tmp2 = nums2[p2]
                    p2 += 1
                elif p2 == len(nums2):
                    tmp2 = nums1[p1]
                    p1 += 1
                elif nums1[p1] <= nums2[p2]:
                    tmp2 = nums1[p1]
                    p1 += 1
                else:
                    tmp2 = nums2[p2]
                    p2 += 1
                pos += 1
            return (tmp1 + tmp2) / 2


a = [1, 2, 3, 4]
b = [-1, 1, 40, 60]
print(Solution2().findMedianSortedArrays(a, b))


# 二分
# TODO:这种方式需要在练练
class Solution3:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2



# 需要重点练习归并和二分法