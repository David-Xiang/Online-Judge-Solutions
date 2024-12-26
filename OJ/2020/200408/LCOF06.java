/**
 * LeetCodeOffer 06 Easy
 * Reverse LinkedList
 */

public class LCOF06 {
    public static void main(String [] args){
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        Solution solution = new Solution();
        int [] arr = solution.reversePrint(head);
        for (int i: arr) {
            System.out.println(i);
        }
    }

    static
    class Solution {
        public int[] reversePrint(ListNode head) {
            int count = 0;
            ListNode curr = head;
            while (curr != null) {
                count++;
                curr = curr.next;
            }
            int [] res = new int [count];
            curr = head;
            for (int i = count - 1; i >= 0 ; i--) {
                res[i] = curr.val;
                curr = curr.next;
            }
            return res;
        }
    }

    static
    class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {val = x;}
    }
}