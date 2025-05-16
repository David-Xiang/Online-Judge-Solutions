/*
 * @lc app=leetcode id=2901 lang=cpp
 *
 * [2901] Longest Unequal Adjacent Groups Subsequence II
 */

// @lc code=start

#include <algorithm>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    bool adj(string &a, string &b) {
        if (a.size() != b.size()) {
            return false;
        }
        int count = 0;
        for (int i = 0; i < a.size(); ++i) {
            if (a[i] != b[i]) {
                ++count;
            }
            if (count > 1) {
                return false;
            }
        }
        return count == 1;
    }
    vector<string> getWordsInLongestSubsequence(vector<string> &words,
                                                vector<int> &groups) {

        vector<int> dp = vector<int>(words.size(), 1);
        vector<int> last = vector<int>(words.size(), -1);
        int max_i = 0;
        for (int i = 1; i < words.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (groups[j] == groups[i]) {
                    continue;
                }
                if (!adj(words[j], words[i])) {
                    continue;
                }
                if (dp[j] + 1 < dp[i]) {
                    continue;
                }
                dp[i] = dp[j] + 1;
                last[i] = j;
                max_i = dp[i] > dp[max_i] ? i : max_i;
            }
        }

        // avoid using algorithm
        // vector<string> ans;
        // while (max_i != -1) {
        //     ans.push_back(words[max_i]);
        //     max_i = last[max_i];
        // }
        // reverse(ans.begin(), ans.end());
        stack<int> stk;
        while (max_i != -1) {
            stk.push(max_i);
            max_i = last[max_i];
        }

        vector<string> ans;
        while (!stk.empty()) {
            ans.push_back(words[stk.top()]);
            stk.pop();
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<string> words = {"a", "b", "c", "d"};
    vector<int> groups = {1, 2, 3, 4};
    vector<string> ans = Solution().getWordsInLongestSubsequence(words, groups);
    for (string s : ans) {
        cout << s << " ";
    }
    cout << endl;
    return 0;
}
