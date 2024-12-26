/**
 * LeetCode 2 Medium
 * Add Two Numbers
 * Linked List
 */

public class LC2 {
    public static void main(String [] args){
        ListNode one = new ListNode(2);
        one.next = new ListNode(4);
        one.next.next = new ListNode(3);
        ListNode two = new ListNode(5);
        two.next = new ListNode(6);
        two.next.next = new ListNode(4);
        Solution solution = new Solution();
        ListNode res = solution.addTwoNumbers(one, two);
        do {
            System.out.println(res.val);
            res = res.next;
        } while(res != null);
    }

    static
    class Solution {
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            int carry = 0;
            ListNode head = new ListNode(0);
            ListNode curr = head;
            while(l1 != null | l2 != null | carry != 0) {
                curr.next = new ListNode(0);
                curr = curr.next;
                carry = singleAdd(l1, l2, curr, carry);

                if (l1 != null) {
                    l1 = l1.next;
                }
                if (l2 != null) {
                    l2 = l2.next;
                }
            }
            return head.next;
        }
        private int singleAdd(ListNode l1, ListNode l2, ListNode res, int carry) {
            int val1 = l1 == null ? 0 : l1.val;
            int val2 = l2 == null ? 0 : l2.val;
            res.val = val1 + val2 + carry;
            if (res.val < 10) {
                return 0;
            }
            res.val -= 10;
            return 1;
        }
    }

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }
}