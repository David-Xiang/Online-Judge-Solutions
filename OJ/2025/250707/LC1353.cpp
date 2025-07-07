/*
 * @lc app=leetcode.cn id=1353 lang=cpp
 *
 * [1353] Maximum Number of Events That Can Be Attended
 */

#include <algorithm>
#include <iostream>
#include <numeric>
#include <queue>
#include <utility>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxEvents(vector<vector<int>> &events) {
        sort(events.begin(), events.end(),
             [](vector<int> &a, vector<int> &b) { return a[0] < b[0]; });
        pair<int, int> bound = accumulate(
            events.begin(), events.end(), make_pair(1000000, 0),
            [](pair<int, int> p, vector<int> &v) {
                return make_pair(min(p.first, v[0]), max(p.second, v[1]));
            });
        int ans = 0;
        vector<vector<int>>::iterator event_it = events.begin();

        auto cmp = [](vector<int> a, vector<int> b) { return a[1] > b[1]; };
        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> pq(cmp);
        for (int i = bound.first; i <= bound.second; ++i) {
            while (event_it != events.end() && (*event_it)[0] <= i) {
                pq.push(*event_it);
                ++event_it;
            }
            while (!pq.empty() && pq.top()[1] < i) {
                pq.pop();
            }
            if (!pq.empty()) {
                ans++;
                pq.pop();
            }
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<vector<int>> events = {{1, 2}, {2, 3}, {3, 4}};
    cout << Solution().maxEvents(events) << endl;
    events = {{1, 2}, {2, 3}, {3, 4}, {1, 2}};
    cout << Solution().maxEvents(events) << endl;
    return 0;
}