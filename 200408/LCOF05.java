/**
 * LeetCodeOffer 05 Easy
 * Replace Space
 * String
 */

public class LCOF05 {
    public static void main(String [] args){
        String s = "We are happy.";
        Solution solution = new Solution();
        System.out.println(solution.replaceSpace(s));
    }

    static
    class Solution {
        public String replaceSpace(String s) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                if (c == ' ') {
                    sb.append("%20");
                } else {
                    sb.append(c);
                }
            }
            return sb.toString();
        }
    }
}