import java.util.Stack;

/**
 * LeetCodeOffer 30 Medium
 * Validate Stack Sequences
 * Topic
 * Remarks
 */

public class LCOF31 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.validateStackSequences(new int []{1, 2, 3, 4, 5}, new int []{4, 5, 3, 2, 1}));
        System.out.println(solution.validateStackSequences(new int []{1, 0}, new int []{1, 0}));
        System.out.println(solution.validateStackSequences(new int []{}, new int []{}));
    }

    static
    class Solution {
        public boolean validateStackSequences(int[] pushed, int[] popped) {
            Stack<Integer> stk = new Stack<>();
            int count = 0; // push/pop匹配的
            for (int value : pushed) {
                stk.push(value);
                while (count < pushed.length && !stk.empty() && popped[count] == stk.peek()) {
                    stk.pop();
                    count++;
                }
            }
            return count == pushed.length;
        }
    }
}