/**
 * LeetCode 8 Medium
 * String to Integer (atoi)
 * String
 */

public class LC8 {
    public static void main(String [] args){
        String i1 = "42"; // return 42
        String i2 = "   -42"; // return -42
        String i3 = "4193 with words"; // return 4193
        String i4 = "words and 987"; // return 0
        String i5 =  "-91283472332"; // return Integer.MIN
        Solution solution = new Solution();
        System.out.println(solution.myAtoi(i1));
        System.out.println(solution.myAtoi(i2));
        System.out.println(solution.myAtoi(i3));
        System.out.println(solution.myAtoi(i4));
        System.out.println(solution.myAtoi(i5));

    }

    static
    class Solution {
        public int myAtoi(String str) {
            str = str.trim();
            // case for returning 0
            if (str.length() == 0) {
                return 0;
            } else if ("+-0123456789".indexOf((str.charAt(0))) == -1) {
                return 0;
            } else if ("+-".indexOf((str.charAt(0))) != -1 && str.length() > 1 && !Character.isDigit(str.charAt(1))) {
                return 0;
            }

            long val = 0;
            boolean positive = true;
            int start = 0;
            if (str.charAt(0) == '-') {
                positive = false;
                start = 1;
            } else if (str.charAt(0) == '+') {
                start = 1;
            }

            long max = (long) Integer.MAX_VALUE;
            long min = (long) Integer.MIN_VALUE;
            while (start < str.length() && Character.isDigit(str.charAt(start)) && val < max && val > min) {
                val = val * 10;
                if (positive) {
                    val += (int) str.charAt(start) - 48;
                } else {
                    val -= (int) str.charAt(start) - 48;
                }
                start++;
            }

            if (val > max) {
                return Integer.MAX_VALUE;
            } else if (val < min) {
                return Integer.MIN_VALUE;
            }
            return (int) val;
        }
    }
}