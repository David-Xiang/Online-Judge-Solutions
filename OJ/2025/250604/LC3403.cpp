/*
 * @lc app=leetcode id=3403 lang=cpp
 *
 * [3403] Find the Lexicographically Largest String From the Box I
 */

#include <iostream>
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
    string answerString(string word, int numFriends) {
        if (numFriends == 1) {
            return word;
        }
        int ans = 0, len = word.length() - numFriends + 1;

        for (int i = 1; i < word.length(); ++i) {
            for (int j = 0; j < len; ++j) {
                if (i + j >= word.length()) {
                    break;
                }
                if (word[ans + j] > word[i + j]) {
                    break;
                }
                if (word[ans + j] < word[i + j]) {
                    ans = i;
                    len = i >= numFriends ? word.length() - i + 1
                                          : word.length() - numFriends + 1;
                    break;
                }
            }
        }
        return word.substr(ans, len);
    }
};
// @lc code=end

int main() {
    cout << Solution().answerString("dbca", 2) << endl;
    cout << Solution().answerString("gggg", 4) << endl;
    cout << Solution().answerString("gh", 1) << endl;
    return 0;
}