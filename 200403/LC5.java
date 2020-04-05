/**
 * LeetCode 5 Medium
 * Longest Palindromic Substring
 * String
 */

public class LC5 {
    public static void main(String [] args){
        String s1 = "babad", s2 = "cbbd";
        Solution solution = new Solution();
        System.out.println(solution.longestPalindrome(s1));
        System.out.println(solution.longestPalindrome(s2));
    }

    static
    class Solution {
        public String longestPalindrome(String s) {
            if (s.length() == 0) {
                return s;
            }
            int rmax = 0, lmax = 0;
            // 奇数
            for (int mid = 1; mid < s.length() - 1; mid++) {
                int w = 1;
                for (; mid - w >= 0 && mid + w < s.length(); w++) {
                    if (s.charAt(mid - w) != s.charAt(mid + w)) {
                        break;
                    }
                }
                if (2 * w - 1 > lmax - rmax + 1) {
                    rmax = mid - w + 1;
                    lmax = mid + w - 1;
                }
            }

            // 偶数
            for (int l = 0; l < s.length() - 1; l++) {
                int w = 0;
                for (; l - w >= 0 && l + 1 + w < s.length(); w++) {
                    if (s.charAt(l - w) != s.charAt(l + 1 + w)) {
                        break;
                    }
                }
                if (2 * w > lmax - rmax + 1) {
                    rmax = l - w + 1;
                    lmax = l + w;
                }
            }
            return s.substring(rmax, lmax + 1);
        }
    }
}