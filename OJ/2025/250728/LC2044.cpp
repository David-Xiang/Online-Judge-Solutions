/*
 * @lc app=leetcode.cn id=2044 lang=cpp
 *
 * [2044] Count Number of Maximum Bitwise-OR Subsets
 */

#include <algorithm>
#include <functional>
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int countMaxOrSubsets(vector<int> &nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0,
                             [](int a, int b) { return a | b; });
        int ans = 0;
        vector<int> sum_remaining(nums.size(), 0);
        for (int i = nums.size() - 2; i >= 0; --i) {
            sum_remaining[i] = sum_remaining[i + 1] | nums[i + 1];
        }
        function<void(int, int)> dfs = [&](int i, int acc) {
            if (i == nums.size()) {
                return;
            }
            // dont choose i
            if ((acc | sum_remaining[i]) == sum) { // prune 1
                dfs(i + 1, acc);
            }

            // choose i
            acc |= nums[i];
            if (acc == sum) { // prune 2
                ans += 1 << (nums.size() - i - 1);
                return;
            }
            dfs(i + 1, acc);
        };
        dfs(0, 0);
        return ans;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {3, 1};
    cout << Solution().countMaxOrSubsets(nums) << endl;
    nums = {2, 2, 2};
    cout << Solution().countMaxOrSubsets(nums) << endl;
    nums = {3, 2, 1, 5};
    cout << Solution().countMaxOrSubsets(nums) << endl;
}