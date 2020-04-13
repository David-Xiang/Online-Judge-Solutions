/**
 * LeetCodeOffer 22 Easy
 * Last K Node in Linked List
 * Linked List
 */

public class LCOF22 {
    public static void main(String [] args){
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        Solution solution = new Solution();
        System.out.println(solution.getKthFromEnd(head, 2).val);
    }

    static
    class Solution {
        public ListNode getKthFromEnd(ListNode head, int k) {
            ListNode fast, slow;
            fast = head; slow = head;
            for (int i = 0; i < k; i++) {
                fast = fast.next;
            }
            while (fast != null) {
                fast = fast.next;
                slow = slow.next;
            }
            return slow;
        }
    }

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }
}