/**
 * LeetCode 28 Simple
 * Implement strStr()
 * KMP
 */

public class LC28 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.strStr("ABCABABCABC", "ABCABC"));
        System.out.println(solution.strStr("BBC ABCDAB ABCDABCDABDE", "ABCDABD"));
        System.out.println(solution.strStr("aaabaaabbbabaa","babb"));
        System.out.println(solution.strStr("babbbbbabb", "bbab"));
        System.out.println(solution.strStr("aabaab", "aabaac"));
    }

    static
    class Solution {
        public int strStr(String str, String pattern) {
            if (pattern.length() == 0)
                return 0;

            final int [] next = genNext(pattern);

            int cur = -1; // 表示已经匹配的部分
            final int len = str.length();
            for (int i = 0; i < len; i++) {
                while (cur >= 0 && str.charAt(i) != pattern.charAt(cur+1)) {
                    cur = next[cur];
                }
                if (str.charAt(i) == pattern.charAt(cur+1)) {
                    cur++;
                }
                if (cur == pattern.length() - 1) {
                    return i - pattern.length() + 1;
                }
            }
            return -1;
        }

        private int[] genNext(String pattern) {
            // next[j] = i表示 0...i为0...j的后缀
            final int len = pattern.length();
            final int [] next = new int [pattern.length()];
            next[0] = -1;

            for (int i = 1; i < len; i++) {
                int k = next[i-1];
                while (k >= 0 && pattern.charAt(k+1) != pattern.charAt(i)) {
                    k = next[k];
                }
                if (pattern.charAt(k+1) == pattern.charAt(i)) {
                    next[i] = k + 1;
                } else {
                    next[i] = -1;
                }
            }
            return next;
        }
    }
}