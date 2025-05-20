/*
 * @lc app=leetcode id=1094 lang=cpp
 *
 * [1094] Car Pooling
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    bool carPooling(vector<vector<int>> &trips, int capacity) {
        vector<int> diff = vector<int>(1001, 0);
        for (vector<int> &t : trips) {
            int num = t[0];
            int from = t[1];
            int to = t[2];
            diff[from] += num;
            diff[to] -= num;
        }
        int sum = 0;
        for (int i = 0; i < 1001; ++i) {
            sum = sum + diff[i];
            if (sum > capacity) {
                return false;
            }
        }
        return true;
    }
};
// @lc code=end
int main() {
    vector<vector<int>> trips = {{2, 1, 5}, {3, 3, 7}};
    cout << Solution().carPooling(trips, 4) << endl;
    cout << Solution().carPooling(trips, 5) << endl;
    return 0;
}
