/*
 * @lc app=leetcode.cn id=3443 lang=cpp
 *
 * [3443] Maximum Manhattan Distance After K Changes
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxDistance(string s, int k) {
        int N = 0, S = 0, W = 0, E = 0;
        int ans = 0;
        for (char c: s) {
            int k_tmp = k;
            if (c == 'N') {
                ++N;
            }
            if (c == 'S') {
                ++S;
            }
            if (c == 'W') {
                ++W;
            }
            if (c == 'E') {
                ++E;
            }
            int vd = min(min(N, S), k_tmp);
            int vmax = abs(N-S) + 2 * vd;
            k_tmp = k_tmp - vd;
            int hd = min(min(W, E), k_tmp);
            int hmax = abs(W-E) + 2 * hd;
            ans = max(ans, vmax + hmax);
        }
        return ans;
    }
};
// @lc code=end

int main() {
    cout << Solution().maxDistance("NWSE", 1) << endl;
    cout << Solution().maxDistance("NSWWEW", 3) << endl;
    return 0;
}