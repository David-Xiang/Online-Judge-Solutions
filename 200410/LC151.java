package com.xiangdongwei;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * LeetCode 151 Medium
 * Reverse Words in a String
 * String
 */

public class LC151 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.reverseWords("the sky is blue"));
        System.out.println(solution.reverseWords("  hello world!  "));
        System.out.println(solution.reverseWords("a good   example"));
    }

    static
    class Solution {
        public String reverseWords(String s) {
            List<String> words = Arrays.asList(s.trim().split("\\s+"));
            Collections.reverse(words);
            return String.join(" ", words);
        }
    }
}