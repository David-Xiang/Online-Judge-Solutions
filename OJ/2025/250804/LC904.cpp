/*
 * @lc app=leetcode.cn id=904 lang=cpp
 *
 * [904] Fruit Into Baskets
 */

#include <iostream>
#include <map>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int totalFruit(vector<int> &fruits) {
        int l = 0, r = 0;
        int ans = 0;
        unordered_map<int, int> cnt;
        for (; r < fruits.size(); ++r) {
            ++cnt[fruits[r]];
            while (cnt.size() > 2) {
                if ((--cnt[fruits[l]]) == 0) {
                    cnt.erase(fruits[l]);
                }
                l++;
            }
            ans = max(ans, r - l + 1);
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<int> nums = {1, 2, 1};
    cout << Solution().totalFruit(nums) << endl;
    nums = {0, 1, 2, 2};
    cout << Solution().totalFruit(nums) << endl;
    nums = {1, 2, 3, 2, 2};
    cout << Solution().totalFruit(nums) << endl;
    nums = {3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4};
    cout << Solution().totalFruit(nums) << endl;
}
