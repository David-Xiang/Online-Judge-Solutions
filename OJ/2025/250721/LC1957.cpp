/*
 * @lc app=leetcode.cn id=1957 lang=cpp
 *
 * [1957] Delete Characters to Make Fancy String
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    string makeFancyString(string s) {
        vector<char> vec;
        for (char c : s) {
            if (vec.size() > 1 && vec[vec.size() - 1] == c &&
                vec[vec.size() - 2] == c) {
                continue;
            }
            vec.push_back(c);
        }
        return string(vec.begin(), vec.end());
    }
};
// @lc code=end

int main() {
    cout << Solution().makeFancyString("leeetcode") << endl;
    cout << Solution().makeFancyString("aaabaaaa") << endl;
    cout << Solution().makeFancyString("aab") << endl;
}