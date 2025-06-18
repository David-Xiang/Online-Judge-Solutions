/*
 * @lc app=leetcode id=2966 lang=cpp
 *
 * [2966] Divide Array Into Arrays With Max Difference
 */

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for (int i = 0; i < nums.size(); i += 3) {
            if (nums[i+2] - nums[i] > k) {
                return vector<vector<int>>();
            }
            ans.push_back(vector<int>{nums[i], nums[i+1], nums[i+2]});
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {1,3,4,8,7,9,3,5,1};
    cout << Solution().divideArray(nums, 2).size() << endl;
    nums = {2,4,2,2,5,2};
    cout << Solution().divideArray(nums, 2).size() << endl;
    nums = {4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11};
    cout << Solution().divideArray(nums, 14).size() << endl;
    return 0;
}