package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// LeetCodeOffer 18 Easy
// Delete Node
// Linked List
func LCOF18() {
	head := &ListNode{4, nil}
	head.Next = &ListNode(5, nil)
	head.Next.Next = &ListNode{1, nil}
	head.Next.Next.Next = &ListNode{9, nil}
	head = deleteNode(head, 5)
	head = deleteNode(head, 4)
}

func deleteNode(head *ListNode, val int) *ListNode {
	pre := &ListNode{}
	curr := head
	for curr != nil && curr.Val != val {
		pre = curr
		curr = curr.Next
	}
	if curr != nil && curr.Val == val {
		pre.Next = curr.Next
	}
	if curr == head {
		head = head.Next
	}
	return head
}
