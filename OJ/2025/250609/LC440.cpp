/*
 * @lc app=leetcode id=440 lang=cpp
 *
 * [440] K-th Smallest in Lexicographical Order
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int findKthNumber(int n, int k) {
        vector<int> prefix;
        return findKthNumberWPrefix(prefix, n, k);
    }

    long getNumberCountWPrefix(vector<int> prefix, int n) {
        int t = 0;
        for (int p : prefix) {
            t = t * 10 + p;
        }
        if (t > n) {
            return 0;
        }
        long count = 1;
        long base = 10;
        for (int b = 0; b < 10; ++b) {
            long t_min = t * base;
            long t_max = (t + 1) * base - 1;
            if (t_max < n) {
                count += t_max - t_min + 1;
            } else if (t_min <= n) {
                count += n - t_min + 1;
                return count;
            } else {
                return count;
            }
            base = base * 10;
        }
        return -1;
    }

    int findKthNumberWPrefix(vector<int> prefix, int n, int k) {
        int t = 0;
        for (int p : prefix) {
            t = t * 10 + p;
        }
        if (!prefix.empty()) {
            k = k - 1;
            if (k == 0) {
                return t;
            }
        }

        for (int i = 0; i < 10; ++i) {
            if (t == 0 && i == 0) {
                continue;
            }
            prefix.push_back(i);
            long count = getNumberCountWPrefix(prefix, n);
            if (k <= count) {
                return findKthNumberWPrefix(prefix, n, k);
            }
            k = k - count;
            prefix.pop_back();
        }
        return -1;
    }
};
// @lc code=end
int main() {
    cout << Solution().getNumberCountWPrefix({1}, 1100) << endl;
    cout << Solution().getNumberCountWPrefix({1, 1}, 1100) << endl;
    cout << Solution().findKthNumber(13, 2) << endl;
    cout << Solution().findKthNumber(1, 1) << endl;
    cout << Solution().findKthNumber(681692778, 351251360) << endl;
    return 0;
}
