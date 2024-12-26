import java.util.Stack;

/**
 * LeetCodeOffer 30 Easy
 * Min Stack
 * Stack
 */

public class LCOF30 {
    public static void main(String [] args){
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        System.out.println(minStack.min()); // return -3
        minStack.pop();
        System.out.println(minStack.top()); // return 0
        System.out.println(minStack.min()); // return -2
    }

    static class MinStack {
        Stack<Integer> s, min;

        /** initialize your data structure here. */
        public MinStack() {
            s = new Stack<>();
            min = new Stack<>();
        }

        public void push(int x) {
            s.push(x);
            min.push(min.empty() ? x : Math.min(min.peek(), x));
        }

        public void pop() {
            s.pop();
            min.pop();
        }

        public int top() {
            return s.peek();
        }

        public int min() {
            return min.peek();
        }
    }
}