/*
 * @lc app=leetcode id=2966 lang=cpp
 *
 * [2294] Partition Array Such That Maximum Difference Is K
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int start = nums[0];
        int count = 1;
        for (int i = 0; i < nums.size(); ++i) {
            int n = nums[i];
            if (n > start + k) {
                start = n;
                count++;
            }
        }
        return count;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {3,6,1,2,5};
    cout << Solution().partitionArray(nums, 2) << endl;
    nums = {1,2,3};
    cout << Solution().partitionArray(nums, 1) << endl;
    nums = {2,2,4,5};
    cout << Solution().partitionArray(nums, 0) << endl;
    return 0;
}