/*
 * @lc app=leetcode.cn id=3487 lang=cpp
 *
 * [3487] Maximum Unique Subarray Sum After Deletion
 */

#include <set>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxSum(vector<int> &nums) {
        set<int> s;
        int ans = 0;
        for (int n : nums) {
            if (n > 0 && s.find(n) == s.end()) {
                ans += n;
                s.insert(n);
            }
        }
        if (s.size() == 0) {
            return *max_element(nums.begin(), nums.end());
        }
        return ans;
    }
};
// @lc code=end
