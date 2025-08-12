/*
 * @lc app=leetcode.cn id=2787 lang=cpp
 *
 * [2787] Ways to Express an Integer as Sum of Powers
 */

#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int numberOfWays(int n, int x) {
        // dp[n][k] = dp[n-k^x][k-1] + dp[n][k-1]
        vector<vector<int>> dp =
            vector<vector<int>>(n + 1, vector<int>(n + 1, 0));
        dp[0][0] = 1;
        for (int i = 0; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                dp[i][j] = dp[i][j - 1];
                long long t = i - pow(j, x);
                if (t >= 0) {
                    dp[i][j] = (dp[i][j] + dp[t][j - 1]) % 1000000007;
                }
            }
        }
        return dp[n][n];
    }
};
// @lc code=end
int main() {
    cout << Solution().numberOfWays(10, 2) << endl;
    cout << Solution().numberOfWays(4, 1) << endl;
}
