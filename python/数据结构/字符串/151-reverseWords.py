# 给定一个字符串，逐个翻转字符串中的每个单词。
#
# 说明：
#
# 无空格字符构成一个 单词 。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#  
#
# 示例 1：
#
# 输入："the sky is blue"
# 输出："blue is sky the"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(strs, a, b):
            if a == b: return
            p1, p2 = a, b
            while p1 <= p2:
                strs[p1], strs[p2] = strs[p2], strs[p1]
                p1 += 1
                p2 -= 1

        empty_str, p, ans = " ", 0, []
        flag = back = False
        while p < len(s):
            x = s[p]
            if x == empty_str and flag:
                back = True
            if x != empty_str:
                if back:
                    ans.append(" ")
                    back = False
                ans.append(x)
                flag = True
            p += 1
        last = j = 0
        while j < len(ans):
            if ans[j] == empty_str:
                reverse(ans, last, j - 1)
                last = j + 1
            j += 1
        reverse(ans, last, len(ans) - 1)
        reverse(ans, 0, len(ans) - 1)
        return "".join(ans)


print(Solution().reverseWords("  addsaf    b   c"))
