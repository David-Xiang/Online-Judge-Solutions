import java.util.HashSet;
import java.util.Set;

/**
 * LeetCode 3 Medium
 * Longest Substring Without Repeating Characters
 * Sliding Window
 */

public class LC3 {
    public static void main(String [] args){
        String s1 = "abcabcbb", s2 = "bbbbb", s3 = "pwwkew";
        Solution solution = new Solution();
        System.out.println(solution.lengthOfLongestSubstring(s1));
        System.out.println(solution.lengthOfLongestSubstring(s2));
        System.out.println(solution.lengthOfLongestSubstring(s3));
    }

    static
    class Solution {
        public int lengthOfLongestSubstring(String s) {
            Set<Character> set = new HashSet<>();
            int l = 0, r = 0; // l包含，r不包含
            int lmax = 0, rmax = 0;
            while(r < s.length()) {
                while (r < s.length() && !set.contains(s.charAt(r))) {
                    set.add(s.charAt(r++));
                    if (r - l > rmax - lmax) {
                        rmax = r; lmax = l;
                    }
                }
                while (r < s.length() && set.contains(s.charAt(r)) && l < r) {
                    set.remove(s.charAt(l++));
                }
            }
            return rmax - lmax;
        }
    }
}