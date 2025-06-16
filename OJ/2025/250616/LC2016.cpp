/*
 * @lc app=leetcode id=2016 lang=cpp
 *
 * [2016] Maximum Difference Between Increasing Elements
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maximumDifference(vector<int> &nums) {
        int min_elem = 1e9 + 10;
        int ans = -1;
        for (int n : nums) {
            if (n - min_elem > 0) {
                ans = max(ans, n - min_elem);
            }
            min_elem = min(n, min_elem);
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {7, 1, 5, 4};
    cout << Solution().maximumDifference(nums) << endl;
    nums = {9, 4, 3, 2};
    cout << Solution().maximumDifference(nums) << endl;
    nums = {1, 5, 2, 10};
    cout << Solution().maximumDifference(nums) << endl;
    return 0;
}