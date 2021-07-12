package leetcode

import (
	"math/rand"
	"time"
)

func random_partition(nums []int, lo, hi int) int {
	rand.Seed(time.Now().Unix())
	pivot := int(rand.Float32()*float32(hi-lo) + float32(lo))
	nums[pivot], nums[hi] = nums[hi], nums[pivot]
	i := lo
	for j := lo; j < hi; j++ {
		if nums[j] > nums[hi] {
			nums[i], nums[j] = nums[j], nums[i]
			i++
		}
	}
	nums[i], nums[hi] = nums[hi], nums[i]
	return i
}

func quick_sort(nums []int, k, lo, hi int) {
	if lo >= hi {
		return
	}
	pivot := random_partition(nums, lo, hi)
	if pivot == k-1 {
		return
	} else if pivot < k-1 {
		quick_sort(nums, k, pivot+1, hi)
	} else {
		quick_sort(nums, k, lo, pivot-1)
	}
	return
}

func FindKthLargest(nums []int, k int) int {
	quick_sort(nums, k, 0, len(nums)-1)
	return nums[k-1]
}
