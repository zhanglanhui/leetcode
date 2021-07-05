package leetcode

/**
 * Definition for singly-linked list. */
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	newHead := reverseList(head.Next)
	head.Next.Next = head
	head.Next = nil
	return newHead
}

func reverseList2(head *ListNode) *ListNode {
	var prev *ListNode
	var p = head
	for p != nil {
		_next := p.Next
		p.Next = prev
		prev = p
		p = _next
	}
	return prev
}
