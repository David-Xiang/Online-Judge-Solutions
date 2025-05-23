/*
 * @lc app=leetcode id=3068 lang=cpp
 *
 * [3068] Find the Maximum Sum of Node Values
 */

#include <climits>
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    long long maximumValueSum(vector<int> &nums, int k,
                              vector<vector<int>> &edges) {
        vector<vector<int>> tree = vector<vector<int>>();
        for (int i = 0; i < nums.size(); ++i) {
            tree.push_back(vector<int>());
        }
        for (vector<int> &e : edges) {
            tree[e[0]].push_back(e[1]);
            tree[e[1]].push_back(e[0]);
        }
        vector<long long> memo_select = vector<long long>(nums.size(), -1);
        vector<long long> memo_not_select = vector<long long>(nums.size(), -1);
        return f(nums, k, tree, 0, -1, false, memo_select, memo_not_select);
    }

    long long f(vector<int> &nums, int k, vector<vector<int>> &tree, int node,
                int father, bool f_select, vector<long long> &memo_select,
                vector<long long> &memo_not_select) {
        int n = f_select ? nums[node] ^ k : nums[node];
        if (tree[node].size() == 1 && father != -1) {
            return n;
        }
        long long min_diff = LONG_LONG_MAX;
        long long sum = 0;
        for (int i = 0; i < tree[node].size(); ++i) {
            int child = tree[node][i];
            if (child == father) {
                continue;
            }

            long long sum_select = memo_select[child];
            if (sum_select == -1) {
                sum_select = f(nums, k, tree, child, node, true, memo_select,
                               memo_not_select);
                memo_select[child] = sum_select;
            }
            long long sum_not_select = memo_not_select[child];
            if (sum_not_select == -1) {
                sum_not_select = f(nums, k, tree, child, node, false,
                                   memo_select, memo_not_select);
                memo_not_select[child] = sum_not_select;
            }
            if (sum_select > sum_not_select) {
                sum += sum_select;
                n = n ^ k;
                min_diff = min(min_diff, sum_select - sum_not_select);
            } else {
                sum += sum_not_select;
                min_diff = min(min_diff, sum_not_select - sum_select);
            }
        }
        long long m = max(n + sum, (n ^ k) + sum - min_diff);
        return max(n + sum, (n ^ k) + sum - min_diff);
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