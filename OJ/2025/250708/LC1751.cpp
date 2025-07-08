/*
 * @lc app=leetcode.cn id=1751 lang=cpp
 *
 * [1751] Maximum Number of Events That Can Be Attended II
 */

// 给你一个 events 数组，其中 events[i] = [startDayi, endDayi, valuei] ，表示第
// i 个会议在 startDayi 天开始，第 endDayi
// 天结束，如果你参加这个会议，你能得到价值 valuei 。同时给你一个整数 k
// 表示你能参加的最多会议数目。

// 你同一时间只能参加一个会议。如果你选择参加某个会议，那么你必须 完整
// 地参加完这个会议。会议结束日期是包含在会议内的，也就是说你不能同时参加一个开始日期与另一个结束日期相同的两个会议。

// 请你返回能得到的会议价值 最大和 。

#include <algorithm>
#include <iostream>
#include <ranges>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxValue(vector<vector<int>> &events, int k) {
        int l = events.size();

        // 按照结束日期排序
        sort(events.begin(), events.end(),
             [](vector<int> &a, vector<int> &b) { return a[1] < b[1]; });

        // dp[i][j]前i个会议中选j个参加 = max(dp[i-1][j], dp[p][j-1] +
        // value[i]), end[p] <  start[i] 把0作为默认值, 下标从1开始 dp[i+1][j] =
        // max(dp[i][j], dp[p+1][j-1] + value[i]), end[p] <  start[i]
        vector<vector<int>> dp = vector<vector<int>>(l + 1, vector<int>(k + 1));
        for (int i = 1; i <= l; ++i) {
            int p =
                lower_bound(
                    events.begin(), events.begin() + i, events[i - 1][0],
                    [](vector<int> &e, int lower) { return e[1] < lower; }) -
                events.begin();
            for (int j = 1; j <= k; ++j) {
                dp[i][j] = max(dp[i - 1][j], dp[p][j - 1] + events[i - 1][2]);
            }
        }
        return dp[l][k];
    }
};
// @lc code=end

int main() {
    vector<vector<int>> events = {{1, 2, 4}, {3, 4, 3}, {2, 3, 1}};
    cout << Solution().maxValue(events, 2) << endl;
    events = {{1, 2, 4}, {3, 4, 3}, {2, 3, 10}};
    cout << Solution().maxValue(events, 2) << endl;
    events = {{1, 1, 1}, {2, 2, 2}, {3, 3, 3}, {4, 4, 4}};
    cout << Solution().maxValue(events, 3) << endl;
    return 0;
}