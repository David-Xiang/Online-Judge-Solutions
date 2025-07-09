/*
 * @lc app=leetcode.cn id=3439 lang=cpp
 *
 * [3439] Reschedule Meetings for Maximum Free Time I
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int> &startTime,
                    vector<int> &endTime) {
        vector<int> interval(startTime.size() + 1, 0);
        for (int i = 0; i < startTime.size() + 1; ++i) {
            if (i == 0) {
                interval[i] = startTime[0];
                continue;
            }
            if (i == startTime.size()) {
                interval[i] = eventTime - endTime[i - 1];
                continue;
            }
            interval[i] = startTime[i] - endTime[i - 1];
        }
        int pos = 0;
        int sum = 0;
        while (pos < k + 1) {
            sum += interval[pos];
            ++pos;
        }
        int ans = sum;
        while (pos < startTime.size() + 1) {
            sum += (interval[pos] - interval[pos - k - 1]);
            ans = max(sum, ans);
            ++pos;
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<int> startTime = {1, 3};
    vector<int> endTime = {2, 5};
    cout << Solution().maxFreeTime(5, 1, startTime, endTime) << endl;
    startTime = {0, 2, 9};
    endTime = {1, 4, 10};
    cout << Solution().maxFreeTime(10, 1, startTime, endTime) << endl;
    startTime = {0, 1, 2, 3, 4};
    endTime = {1, 2, 3, 4, 5};
    cout << Solution().maxFreeTime(5, 2, startTime, endTime) << endl;
    return 0;
}
