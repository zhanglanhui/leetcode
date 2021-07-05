package leetcode

//给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

//动态规划
func MaxSubArray(nums []int) int {
	ans := nums[0]
	dp := make([]int, len(nums))
	dp[0] = ans
	for i := 1; i < len(nums); i++ {
		dp[i] = max(nums[i], dp[i-1]+nums[i])
		ans = max(ans, dp[i])
	}
	return ans
}

func MaxSubArray2(nums []int) int {
	ans := nums[0]
	last := ans
	for i := 1; i < len(nums); i++ {
		if last > 0 {
			last += nums[i]
		} else {
			last = nums[i]
		}
		ans = max(ans, last)
	}
	return ans
}
