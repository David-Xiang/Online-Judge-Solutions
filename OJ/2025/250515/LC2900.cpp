/*
 * @lc app=leetcode.cn id=2900 lang=cpp
 *
 * [2900] 最长相邻不相等子序列 I
 */

#include <iostream>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<string> getLongestSubsequence(vector<string> &words,
                                         vector<int> &groups) {
        vector<string> ans;
        for (int i = 0; i < groups.size(); ++i) {
            if (i == 0 || groups[i] != groups[i - 1]) {
                ans.push_back(words[i]);
            }
        }
        return ans;
    }
};
// @lc code=end

int main() {
    Solution s;

    vector<string> words = {"e", "a", "b"};
    vector<int> groups = {0, 0, 1};
    cout << s.getLongestSubsequence(words, groups).size() << endl;

    words = {"a", "b", "c", "d"};
    groups = {1, 0, 1, 1};
    cout << s.getLongestSubsequence(words, groups).size() << endl;
    return 0;
}