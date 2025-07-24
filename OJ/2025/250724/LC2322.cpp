/*
 * @lc app=leetcode.cn id=2322 lang=cpp
 *
 * [2322] Minimum Score After Removals on a Tree
 */

#include <functional>
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int minimumScore(vector<int> &nums, vector<vector<int>> &edges) {
        vector<vector<int>> adj(nums.size());
        for (vector<int> &v : edges) {
            adj[v[0]].push_back(v[1]);
            adj[v[1]].push_back(v[0]);
        }
        int sum_all = 0;
        for (int n : nums) {
            sum_all ^= n;
        }

        int ans = INT_MAX;

        function<int(int, int, int)> dfs2 = [&](int n, int p, int sum1) {
            int sum2 = nums[n];
            for (int c : adj[n]) {
                if (c == p) {
                    continue;
                }
                sum2 ^= dfs2(c, n, sum1);
            }
            int sum3 = sum_all ^ sum1 ^ sum2;
            ans = min(ans,
                      max(sum1, max(sum2, sum3)) - min(sum1, min(sum2, sum3)));
            return sum2;
        };

        function<int(int, int)> dfs = [&](int n, int p) {
            int sum1 = nums[n];
            for (int c : adj[n]) {
                if (c == p) { // find parent
                    continue;
                }
                sum1 ^= dfs(c, n);
            }
            // calc the score of cut edge p-n
            for (int c : adj[p]) {
                if (c == n) {
                    continue;
                }
                dfs2(c, p, sum1);
            }
            return sum1;
        };

        for (int p : adj[0]) {
            dfs(p, 0);
        }
        return ans;
    }
};
// @lc code=end
int main() {
    vector<int> nums = {1, 5, 5, 4, 11};
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {1, 3}, {3, 4}};
    cout << Solution().minimumScore(nums, edges) << endl;
    nums = {5, 5, 2, 4, 4, 2};
    edges = {{0, 1}, {1, 2}, {5, 2}, {4, 3}, {1, 3}};
    cout << Solution().minimumScore(nums, edges) << endl;
    return 0;
}