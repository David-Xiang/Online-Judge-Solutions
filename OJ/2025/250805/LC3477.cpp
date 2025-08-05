/*
 * @lc app=leetcode.cn id=3477 lang=cpp
 *
 * [3477] Fruits Into Baskets II
 */

#include <iostream>
#include <set>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int numOfUnplacedFruits(vector<int> &fruits, vector<int> &baskets) {
        set<int> used;
        int cnt = 0;
        for (int f : fruits) {
            bool found = false;
            for (int i = 0; i < baskets.size(); ++i) {
                int b = baskets[i];
                if (b >= f && used.find(i) == used.end()) {
                    found = true;
                    used.emplace(i);
                    break;
                }
            }
            if (!found) {
                ++cnt;
            }
        }
        return cnt;
    }
};
// @lc code=end
int main() {
    vector<int> fruits = {4, 2, 5};
    vector<int> baskets = {3, 5, 4};
    cout << Solution().numOfUnplacedFruits(fruits, baskets) << endl;
    fruits = {3, 6, 1};
    baskets = {6, 4, 7};
    cout << Solution().numOfUnplacedFruits(fruits, baskets) << endl;
}
