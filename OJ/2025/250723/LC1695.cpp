/*
 * @lc app=leetcode.cn id=1695 lang=cpp
 *
 * [1695] Maximum Erasure Value
 */

#include <iostream>
#include <set>

using namespace std;

// @lc code=start
class Solution {
public:
    int maximumUniqueSubarray(vector<int> &nums) {
        vector<int>::iterator left = nums.begin(), right = nums.begin();
        set<int> s;
        int sum = 0;
        int ans = 0;
        while (right != nums.end()) {
            while (left < right && s.find(*right) != s.end()) {
                s.erase(*left);
                sum -= *left;
                ++left;
            }
            sum += *right;
            ans = max(ans, sum);
            s.insert(*right);
            ++right;
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {4, 2, 4, 5, 6};
    cout << Solution().maximumUniqueSubarray(nums) << endl;
    nums = {5, 2, 1, 2, 5, 2, 1, 2, 5};
    cout << Solution().maximumUniqueSubarray(nums) << endl;
    return 0;
}
