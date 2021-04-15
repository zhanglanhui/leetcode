#!/usr/bin/python3
from typing import List


# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def isValid(self, s: str) -> bool:
        paris = {")": "(", "}": "{", "]": "["}
        tmp = []
        for x in s:
            if x in paris:
                if not tmp:
                    return False
                if tmp[-1] == paris[x]:
                    tmp = tmp[:-1]
                else:
                    return False
            else:
                tmp.append(x)
        return False if len(tmp) > 0 else True


class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        paris = {")": "(", "}": "{", "]": "["}
        tmp = []
        for x in s:
            if x in paris:
                if not tmp or tmp[-1] != paris[x]:
                    return False
                tmp.pop()
            else:
                tmp.append(x)
        return not tmp


print(Solution2().isValid("()[]{}"))
