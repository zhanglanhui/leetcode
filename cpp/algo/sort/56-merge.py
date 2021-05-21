#!/usr/bin/python3
from typing import List
import functools


# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 排序法
class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        sorted_nums = sorted(intervals, key=lambda x: x[0])
        ans, tmp = [], sorted_nums[0]
        for x in sorted_nums[1::]:
            if tmp[1] >= x[0]:
                tmp[1] = max(x[1], tmp[1])
            else:
                ans.append(tmp)
                tmp = x
        if tmp: ans.append(tmp)
        return ans


print(Solution1().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
