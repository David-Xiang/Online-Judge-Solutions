/*
 * @lc app=leetcode.cn id=3330 lang=cpp
 *
 * [3330] Find the Original Typed String I
 */

// @lc code=start
class Solution {
public:
    int possibleStringCount(string word) {
        int ans = 1;
        for (int i = 1; i < word.size(); ++i) {
            if (word[i] == word[i-1]) {
                ans++;

            }
        }
        return ans;
    }
};
// @lc code=end

