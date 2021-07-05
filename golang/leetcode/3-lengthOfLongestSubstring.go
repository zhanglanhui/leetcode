package leetcode

//# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
//# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
//
//
//# 暴力解法
//# 执行用时：# 372 ms# , 在所有 Python3 提交中击败了# 14.36%# 的用户
//# 内存消耗：# 15 MB# , 在所有 Python3 提交中击败了# 42.82%# 的用户
func LengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}
	var freq [256]int
	result, left, right := 0, 0, -1

	for left < len(s) {
		if right+1 < len(s) && freq[s[right+1]-'a'] == 0 {
			freq[s[right+1]-'a']++
			right++
		} else {
			freq[s[left]-'a']--
			left++
		}
		result = max(result, right-left+1)
	}
	return result
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LengthOfLongestSubstring2(s string) int {
	if len(s) == 0 {
		return 0
	}
	ans, p := 1, 0
	lookup := map[uint8]int{}
	for i := 0; i < len(s); i++ {
		if ind, ok := lookup[s[i]]; ok && ind >= p {
			p = ind + 1
			lookup[s[i]] = -1
		}
		lookup[s[i]] = i
		ans = max(ans, i-p+1)
	}
	return ans
}
