import java.util.Stack;

/**
 * LeetCodeOffer 09 Easy
 * Queue by Two Stack
 * Stack
 */

public class LCOF09 {
    public static void main(String [] args){
        CQueue queue = new CQueue();
        queue.appendTail(3);
        System.out.println(queue.deleteHead());
        System.out.println(queue.deleteHead());
        queue = new CQueue();
        System.out.println(queue.deleteHead());
        queue.appendTail(5);
        queue.appendTail(2);
        System.out.println(queue.deleteHead());
        System.out.println(queue.deleteHead());
    }

    static
    class CQueue {
        Stack<Integer> head, tail;
        public CQueue() {
            head = new Stack<>();
            tail = new Stack<>();
        }

        public void appendTail(int value) {
            tail.push(value);
        }

        public int deleteHead() {
            if (!head.empty()) {
                return head.pop();
            }
            while (!tail.empty()) {
                head.push(tail.pop());
            }
            if (head.empty()){
                return -1;
            }
            return head.pop();
        }
    }
}