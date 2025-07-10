/*
 * @lc app=leetcode.cn id=3440 lang=cpp
 *
 * [3440] Reschedule Meetings for Maximum Free Time II
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxFreeTime(int eventTime, vector<int> &startTime,
                    vector<int> &endTime) {
        int l = startTime.size();
        vector<int> interval(l + 1);
        for (int i = 0; i < l + 1; ++i) {
            if (i == 0) {
                interval[i] = startTime[0];
            } else if (i == l) {
                interval[i] = eventTime - endTime[i - 1];
            } else {
                interval[i] = startTime[i] - endTime[i - 1];
            }
        }
        vector<int> sort_interval = interval;
        sort(sort_interval.begin(), sort_interval.end(), greater<int>());
        int ans = 0;
        for (int i = 1; i < l + 1; ++i) {
            int s = interval[i - 1] + interval[i];
            int m = sort_interval[0];
            if (m == max(interval[i - 1], interval[i])) {
                m = sort_interval[1];
            }
            if (m == min(interval[i - 1], interval[i])) {
                m = sort_interval[2];
            }
            if (m >= endTime[i - 1] - startTime[i - 1]) {
                s += endTime[i - 1] - startTime[i - 1];
            }
            ans = max(ans, s);
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<int> startTime = {1, 3};
    vector<int> endTime = {2, 5};
    cout << Solution().maxFreeTime(5, startTime, endTime) << endl;
    startTime = {0, 7, 9};
    endTime = {1, 8, 10};
    cout << Solution().maxFreeTime(10, startTime, endTime) << endl;
    startTime = {0, 3, 7, 9};
    endTime = {1, 4, 8, 10};
    cout << Solution().maxFreeTime(10, startTime, endTime) << endl;
}