/*
 * @lc app=leetcode id=3068 lang=cpp
 *
 * [3068] Find the Maximum Sum of Node Values
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    long long maximumValueSum(vector<int> &nums, int k,
                              vector<vector<int>> &edges) {
        vector<vector<int>> gain = vector<vector<int>>();
        long long sum = 0;
        for (int n : nums) {
            sum += n;
            gain.push_back({n, (n ^ k) - n});
        }
        sort(gain.begin(), gain.end(),
             [](const vector<int> &a, const vector<int> &b) {
                 return a[1] > b[1];
             });
        for (auto it = gain.begin(); it != gain.end(); (++it)) {
            int gain1 = (*it)[1];
            (++it);
            if (it == gain.end()) {
                break;
            }
            int gain2 = (*it)[1];
            if (gain1 + gain2 > 0) {
                sum += gain1 + gain2;
            }
        }
        return sum;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {2, 3};
    int k = 7;
    vector<vector<int>> edges = {{0, 1}};
    cout << Solution().maximumValueSum(nums, k, edges) << endl;

    nums = {1, 2, 1};
    k = 3;
    edges = {{0, 1}, {0, 2}};
    cout << Solution().maximumValueSum(nums, k, edges) << endl;

    nums = {7, 7, 7, 7, 7, 7};
    k = 3;
    edges = {{0, 1}, {0, 2}, {0, 3}, {0, 4}, {0, 5}};
    cout << Solution().maximumValueSum(nums, k, edges) << endl;
}