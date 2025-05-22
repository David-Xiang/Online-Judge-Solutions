/*
 * @lc app=leetcode id=3362 lang=cpp
 *
 * [3362] Zero Array Transformation III
 */

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxRemoval(vector<int> &nums, vector<vector<int>> &queries) {
        sort(queries.begin(), queries.end(),
             [](const vector<int> &a, const vector<int> &b) {
                 return a[0] < b[0];
             });
        int q = 0;
        int num = 0;
        priority_queue<int> heap;
        vector<int> diff = vector<int>(nums.size() + 2, 0);
        for (int i = 0; i < nums.size(); ++i) {
            num = num + diff[i];
            while (q < queries.size() && queries[q][0] <= i) {
                heap.push(queries[q++][1]); // push right end
            }
            while (num < nums[i]) {
                if (heap.empty() || heap.top() < i) {
                    return -1;
                }
                ++num;
                int r = heap.top() + 1; // all the queries in heap meet
                                        // requirement, greedily get one
                heap.pop();
                --(diff[r]);
            }
        }
        return heap.size();
    }
};
// @lc code=end

int main() {
    vector<int> nums = {2, 0, 2};
    vector<vector<int>> queries = {{0, 2}, {0, 2}, {1, 1}};
    cout << Solution().maxRemoval(nums, queries) << endl;
    nums = {1, 1, 1, 1};
    queries = {{1, 3}, {0, 2}, {1, 3}, {1, 2}};
    cout << Solution().maxRemoval(nums, queries) << endl;
    nums = {1, 2, 3, 4};
    queries = {{0, 3}};
    cout << Solution().maxRemoval(nums, queries) << endl;
    nums = {0, 0, 3};
    queries = {{0, 2}, {1, 1}, {0, 0}, {0, 0}};
    cout << Solution().maxRemoval(nums, queries) << endl;
    return 0;
}
