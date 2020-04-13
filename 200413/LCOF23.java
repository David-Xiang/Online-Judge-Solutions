/**
 * LeetCodeOffer 23 Easy
 * Reverse Linked List
 * Linked List
 * Remarks
 */

public class LCOF23 {
    public static void main(String [] args){
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        Solution solution = new Solution();
        head = solution.reverseList(head);
        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }

    static
    class Solution {
        public ListNode reverseList(ListNode head) {
            return reverseListInternal(head, null);
        }
        private ListNode reverseListInternal(ListNode head, ListNode prev) {
            if (head == null || head.next == null) {
                return head;
            }
            ListNode next = head.next;
            ListNode newHead = reverseListInternal(head.next, head);
            next.next = head;
            head.next = prev;
            return newHead;
        }
    }

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }
}