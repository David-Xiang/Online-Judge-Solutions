/*
 * @lc app=leetcode id=3442 lang=cpp
 *
 * [3442] Maximum Difference Between Even and Odd Frequency I
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxDifference(string s) {
        int count[26] = {0};
        for (char c: s) {
            ++count[c - 'a'];
        }
        int maxOdd = 0;
        int minEven = 1e9;
        for (int i = 0; i < 26; ++i) {
            if (count[i] == 0) {
                continue;
            }
            else if (count[i] % 2 == 0) {
                minEven = min(minEven, count[i]);
            } else {
                maxOdd = max(maxOdd, count[i]);
            }
        }
        return  maxOdd - minEven;
    }
};
// @lc code=end

int main() {
    cout << Solution().maxDifference("aaaaabbc") << endl;
    cout << Solution().maxDifference("abcabcab") << endl;
    return 0;
}