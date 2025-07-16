/*
 * @lc app=leetcode.cn id=3201 lang=cpp
 *
 * [3201] Find the Maximum Length of Valid Subsequence I
 */

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maximumLength(vector<int> &nums) {
        vector<int> dp0 = vector<int>(nums.size(), 0);
        vector<int> dp1 = vector<int>(nums.size(), 0);
        int last_odd = -1;
        int last_even = -1;
        for (int i = 0; i < nums.size(); ++i) {
            int n = nums[i];
            if (n % 2 == 0) {
                dp0[i] = last_even >= 0 ? dp0[last_even] + 1 : 1;
                dp1[i] = last_odd >= 0 ? dp1[last_odd] + 1 : 1;
                last_even = i;
            } else {
                dp0[i] = last_odd >= 0 ? dp0[last_odd] + 1 : 1;
                dp1[i] = last_even >= 0 ? dp1[last_even] + 1 : 1;
                last_odd = i;
            }
        }
        return max(*max_element(dp0.begin(), dp0.end()),
                   *max_element(dp1.begin(), dp1.end()));
    }
};
// @lc code=end
int main() {
    vector<int> nums = {1, 2, 3, 4};
    // cout << Solution().maximumLength(nums) << endl;
    nums = {1, 2, 1, 1, 2, 1, 2};
    // cout << Solution().maximumLength(nums) << endl;
    nums = {1, 3};
    // cout << Solution().maximumLength(nums) << endl;
    nums = {1, 1, 7, 3, 2};
    cout << Solution().maximumLength(nums) << endl;
    return 0;
}
