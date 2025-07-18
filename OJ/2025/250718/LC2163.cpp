/*
 * @lc app=leetcode.cn id=2163 lang=cpp
 *
 * [2163] Minimum Difference in Sums After Removal of Elements
 */

#include <functional>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    long long minimumDifference(vector<int> &nums) {
        int n = nums.size() / 3;
        vector<long long> min_sum_forward(nums.size(), 0);
        priority_queue<int> max_heap;
        long long sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            if (i < n) {
                sum += num;
                max_heap.push(num);
                if (i == n - 1) {
                    min_sum_forward[i] = sum;
                }
            } else {
                if (num < max_heap.top()) {
                    sum += (num - max_heap.top());
                    max_heap.pop();
                    max_heap.push(num);
                }
                min_sum_forward[i] = sum;
            }
        }

        vector<long long> max_sum_backward(nums.size(), 0);
        priority_queue<int, vector<int>, greater<int>> min_heap;
        sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[nums.size() - i - 1];
            if (i < n) {
                sum += num;
                min_heap.push(num);
                if (i == n - 1) {
                    max_sum_backward[nums.size() - i - 1] = sum;
                }
            } else {
                if (num > min_heap.top()) {
                    sum += (num - min_heap.top());
                    min_heap.pop();
                    min_heap.push(num);
                }
                max_sum_backward[nums.size() - i - 1] = sum;
            }
        }

        long long ans = LONG_LONG_MAX;
        for (int i = n - 1; i < 2 * n; ++i) {
            ans = min(ans, min_sum_forward[i] - max_sum_backward[i + 1]);
        }
        return ans;
    }
};
// @lc code=end
int main() {
    vector<int> nums = {3, 1, 2};
    cout << Solution().minimumDifference(nums) << endl;
    nums = {7, 9, 5, 8, 1, 3};
    cout << Solution().minimumDifference(nums) << endl;
    nums = {16, 46, 43, 41, 42, 14, 36, 49, 50, 28, 38,
            25, 17, 5,  18, 11, 14, 21, 23, 39, 23};
    cout << Solution().minimumDifference(nums) << endl;
}