/*
 * @lc app=leetcode id=2616 lang=cpp
 *
 * [2616] Minimize the Maximum Difference of Pairs
 */

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int check(vector<int> &diff, int v, int p) {
        int cnt = 0;
        int last = -2;
        for (int i = 0; i < diff.size(); ++i) {
            if (diff[i] <= v && last + 1 < i) {
                ++cnt;
                last = i;
            }
        }
        return cnt >= p;
    }
    int minimizeMax(vector<int> &nums, int p) {
        int max_diff = 0;
        sort(nums.begin(), nums.end());
        vector<int> diff = vector<int>(nums.size() - 1, 0);
        for (int i = 0; i < nums.size() - 1; ++i) {
            diff[i] = nums[i + 1] - nums[i];
            max_diff = max(max_diff, diff[i]);
        }
        int min_diff = 0;
        while (min_diff < max_diff) {
            int mid = (min_diff + max_diff) / 2;
            if (check(diff, mid, p)) {
                max_diff = mid;
            } else {
                min_diff = mid + 1;
            }
        }
        return min_diff;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {10, 1, 2, 7, 1, 3};
    cout << Solution().minimizeMax(nums, 2) << endl;
    nums = {4, 2, 1, 2};
    cout << Solution().minimizeMax(nums, 1) << endl;
}