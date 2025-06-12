/*
 * @lc app=leetcode id=3423 lang=cpp
 *
 * [3423] Maximum Difference Between Adjacent Elements in a Circular Array
 */

// @lc code=start
class Solution {
public:
    int abs(int a, int b) {
        return a > b ? a - b : b - a;
    }
    int maxAdjacentDistance(vector<int>& nums) {
        int ans = -1000;
        for (int i = 0; i < nums.size(); ++i) {
            ans = max(ans, abs(nums[i], nums[(i+1) % nums.size()]));
        }
        return ans;
    }
};
// @lc code=end

