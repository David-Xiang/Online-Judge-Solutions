/*
 * @lc app=leetcode id=3356 lang=cpp
 *
 * [3356] Zero Array Transformation II
 */

#include <iostream>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int validK(vector<int> &nums, vector<vector<int>> &queries, int k) {
        vector<int> diff = vector<int>(nums.size() + 2, 0);
        for (int i = 0; i < k; ++i) {
            vector<int> &q = queries[i];
            int l = q[0];
            int r = q[1];
            int val = q[2];
            diff[l] += val;
            diff[r + 1] -= val;
        }
        int sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            sum += diff[i];
            if (sum < nums[i]) {
                return false;
            }
        }
        return true;
    }
    int minZeroArray(vector<int> &nums, vector<vector<int>> &queries) {
        if (validK(nums, queries, 0)) {
            return 0;
        }
        if (!validK(nums, queries, queries.size())) {
            return -1;
        }
        int r = 0;
        int l = queries.size();
        while (r + 1 < l) {
            int mid = (r + l) / 2;
            if (validK(nums, queries, mid)) {
                l = mid;
            } else {
                r = mid;
            }
        }
        return l;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {2, 0, 2};
    vector<vector<int>> queries = {{0, 2, 1}, {0, 2, 1}, {1, 1, 3}};
    cout << Solution().minZeroArray(nums, queries) << endl;
    nums = {4, 3, 2, 1};
    queries = {{1, 3, 2}, {0, 2, 1}};
    cout << Solution().minZeroArray(nums, queries) << endl;
    nums = {5};
    queries = {{0, 0, 5}, {0, 0, 1}, {0, 0, 3}, {0, 0, 2}};
    cout << Solution().minZeroArray(nums, queries) << endl;
    nums = {7, 6, 8};
    queries = {{0, 0, 2}, {0, 1, 5}, {2, 2, 5}, {0, 2, 4}};
    cout << Solution().minZeroArray(nums, queries) << endl;
    return 0;
}