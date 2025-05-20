/*
 * @lc app=leetcode id=3355 lang=cpp
 *
 * [3355] Zero Array Transformation I
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    bool isZeroArray(vector<int> &nums, vector<vector<int>> &queries) {
        vector<int> diff = vector<int>(nums.size() + 1, 0);
        for (vector<int> &q : queries) {
            int l = q[0];
            int r = q[1];
            ++diff[l];
            --diff[r + 1];
        }
        int elem = 0;
        for (int i = 0; i < nums.size(); ++i) {
            elem = elem + diff[i];
            if (elem < nums[i]) {
                return false;
            }
        }
        return true;
    }
};
// @lc code=end
int main() {
    vector<int> nums = {1, 2, 1, 0, 0, 0};
    vector<vector<int>> queries = {{0, 3}, {2, 4}};
    cout << Solution().isZeroArray(nums, queries) << endl;
    nums = {4, 3, 2, 1};
    queries = {{1, 3}, {0, 2}};
    cout << Solution().isZeroArray(nums, queries) << endl;
    nums = {2};
    queries = {{0, 0}, {0, 0}};
    cout << Solution().isZeroArray(nums, queries) << endl;
    return 0;
}
