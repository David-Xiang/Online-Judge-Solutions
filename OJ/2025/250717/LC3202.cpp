/*
 * @lc app=leetcode.cn id=3202 lang=cpp
 *
 * [3202] Find the Maximum Length of Valid Subsequence II
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        vector<vector<int>> dp(k, vector<int>(k, 0));
        int ans = 0;
        for (int n: nums) {
            int mod = n % k;
            for (int prev = 0; prev < k; ++prev) {
                dp[prev][mod] = dp[mod][prev] + 1;
                ans = max(ans, dp[prev][mod]);
            }
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {1,2,3,4,5};
    cout << Solution().maximumLength(nums, 2) << endl;
    nums = {1,4,2,3,1,4};
    cout << Solution().maximumLength(nums, 3) << endl;
    return 0;
}
