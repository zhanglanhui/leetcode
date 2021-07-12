package leetcode

//给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
//
//子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
//
//来源：力扣（LeetCode）
//链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
//著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
func LengthOfLIS(nums []int) int {
	dp := make([]int, len(nums))
	ans := 1
	for ind, num := range nums {
		dp[ind] = 1
		for i := 0; i < ind; i++ {
			if num > nums[i] {
				dp[ind] = max(dp[i]+1, dp[ind])
			}
		}
		ans = max(ans, dp[ind])
	}
	return ans
}

func LengthOfLIS2(nums []int) int {
	stack := make([]int, 0, len(nums))
	size := 0
	for _, num := range nums {
		if len(stack) == 0 || num > stack[size-1] {
			stack = append(stack, num)
			size += 1
		} else {
			left, right := 0, len(stack)
			for left < right {
				mid := (left + right) >> 1
				if stack[mid] < num {
					left = mid + 1
				} else {
					right = mid
				}
			}
			stack[right] = num
		}
	}
	return size
}
