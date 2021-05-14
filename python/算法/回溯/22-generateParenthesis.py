#!/usr/bin/python3
from typing import List
import functools


# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#  
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/generate-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 暴力解法
class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        @functools.lru_cache(100)
        def generate(n):
            if n == 1:
                return ["(", ")"]
            return [x + y for x in generate(n - 1) for y in ["(", ")"]]

        def isValid(str):
            if ")" == str[0]:
                return False
            tmp = []
            for x in str:
                if x == "(":
                    tmp.append(x)
                elif tmp and tmp[-1] == "(":
                    tmp.pop()
                else:
                    return False
            return True if not tmp else False

        return [x for x in generate(2 * n) if isValid(x)]



# 回溯解法
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        pass






print(Solution1().generateParenthesis(3))
