#!/usr/bin/python3
from typing import List
import functools


# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
#
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
#
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
#
# 请你返回「表现良好时间段」的最大长度。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-well-performing-interval
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        tttt = [1 if x > 8 else -1 for x in hours]
        presum = [0]
        for x in tttt: presum.append(presum[-1] + x)
        ans = 0
        stack = []
        # 顺序生成单调栈，栈中元素从第一个元素开始严格单调递减，最后一个元素肯定是数组中的最小元素所在位置
        for i in range(len(presum)):
            if not stack or presum[stack[-1]] > presum[i]:
                stack.append(i)
        i = len(hours)
        while i > ans:
            con
            while stack and presum[i] > presum[stack[-1]]:
                ans = max(ans, i - stack[-1])
                stack.pop()
            i -= 1
        return ans


print(Solution().longestWPI([6, 9, 9]))
