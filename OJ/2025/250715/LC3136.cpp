/*
 * @lc app=leetcode.cn id=3136 lang=cpp
 *
 * [3136] Valid Word
 */

#include <algorithm>
#include <iostream>
#include <set>
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
    bool isValid(string word) {
        set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        if (word.size() < 3) {
            return false;
        }
        if (!all_of(word.begin(), word.end(),
                    [](char c) { return isalnum(c); })) {
            return false;
        }
        if (!any_of(word.begin(), word.end(), [&vowels](char c) {
                return vowels.find(c) != vowels.end();
            })) {
            return false;
        }
        if (!any_of(word.begin(), word.end(), [&vowels](char c) {
                return isalpha(c) && vowels.find(c) == vowels.end();
            })) {
            return false;
        }
        return true;
    }
};
// @lc code=end

int main() {
    cout << Solution().isValid("234Adas") << endl;
    cout << Solution().isValid("b3") << endl;
    cout << Solution().isValid("a3$e") << endl;
    cout << Solution().isValid("UuE6") << endl;
    return 0;
}