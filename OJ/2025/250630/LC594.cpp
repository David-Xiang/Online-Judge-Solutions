/*
 * @lc app=leetcode.cn id=594 lang=cpp
 *
 * [594] Longest Harmonious Subsequence
 */

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int findLHS(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int last_start = 0;
        int i = 0;
        int ans = 0;
        while (i < nums.size() && nums[i] == nums[last_start]) {
            ++i;
        }
        int this_start = i;
        while (i < nums.size()) {
            if ((i < nums.size() - 1 && nums[i] != nums[i + 1]) ||
                (i == nums.size() - 1)) {
                if (nums[last_start] + 1 == nums[this_start]) {
                    ans = max(ans, i - last_start + 1);
                }
                last_start = this_start;
                this_start = i + 1;
            }
            ++i;
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {1, 3, 2, 2, 5, 2, 3, 7};
    cout << Solution().findLHS(nums) << endl;
    nums = {1, 2, 3, 4};
    cout << Solution().findLHS(nums) << endl;
    nums = {1, 1, 1, 1};
    cout << Solution().findLHS(nums) << endl;
    nums = {1, 3, 5, 7, 9, 11, 13, 15, 17};
    cout << Solution().findLHS(nums) << endl;
    return 0;
}
