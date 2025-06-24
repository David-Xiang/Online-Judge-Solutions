/*
 * @lc app=leetcode.cn id=2200 lang=cpp
 *
 * [2200] Find All K-Distant Indices in an Array
 */

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> findKDistantIndices(vector<int> &nums, int key, int k) {
        int last = 0;
        vector<int> ans;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != key) {
                continue;
            }
            for (last = max(last, i - k); last <= i + k && last < nums.size();
                 ++last) {
                ans.push_back(last);
            }
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {3, 4, 9, 1, 3, 9, 5};
    cout << Solution().findKDistantIndices(nums, 9, 1).size() << endl;
    nums = {2, 2, 2, 2, 2};
    cout << Solution().findKDistantIndices(nums, 2, 2).size() << endl;
    return 0;
}
