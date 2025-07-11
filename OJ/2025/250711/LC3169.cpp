/*
 * @lc app=leetcode.cn id=3169 lang=cpp
 *
 * [3169] Count Days Without Meetings
 */

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int countDays(int days, vector<vector<int>> &meetings) {
        sort(meetings.begin(), meetings.end(),
             [](vector<int> &a, vector<int> &b) {
                 return a[0] < b[0];
             }); // sort by start day
        int day = 0;
        int meet_pos = 0;
        int count = 0;
        while (day < days && meet_pos < meetings.size()) {
            if (meetings[meet_pos][0] > day) {
                count += meetings[meet_pos][0] - day - 1;
            }
            day = max(day, meetings[meet_pos][1]);
            ++meet_pos;
        }
        if (day < days) {
            count += days - day;
        }
        return count;
    }
};
// @lc code=end

int main() {
    vector<vector<int>> meetings = {{5, 7}, {1, 3}, {9, 10}};
    cout << Solution().countDays(10, meetings) << endl;
    meetings = {{2, 4}, {1, 3}};
    cout << Solution().countDays(5, meetings) << endl;
    meetings = {{1, 6}};
    cout << Solution().countDays(6, meetings) << endl;
}
