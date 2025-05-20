/*
 * @lc app=leetcode id=54 lang=cpp
 *
 * [54] Spiral Matrix
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix) {
        vector<int> ans;
        int row = matrix.size();
        int col = matrix[0].size();
        vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int dir_idx = 0;
        int max_layer = min((row + 1) / 2, (col + 1) / 2);
        int p_x = 0;
        int p_y = -1;
        for (int layer = 0; layer < max_layer; ++layer) {
            p_y += 1;
            for (int d = 0; d < 4; ++d) {
                if (row - 2 * layer == 1 && d == 2) {
                    continue;
                }
                if (col - 2 * layer == 1 && d == 3) {
                    continue;
                }
                int len = d % 2 == 0 ? col - 2 * layer : row - 2 * (layer + 1);
                int count = 0;
                for (int i = 0; i < len; ++i) {
                    ans.push_back(matrix[p_x][p_y]);
                    int t = d;
                    if (i == len - 1 && d == 3) {
                        continue;
                    }
                    if (i == len - 1 && d % 2 == 0) {
                        t = (d + 1) % 4;
                    }
                    p_x += dirs[t][0];
                    p_y += dirs[t][1];
                }
            }
        }

        return ans;
    }
};
// @lc code=end

int main() {
    vector<vector<int>> matrix = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    Solution().spiralOrder(matrix);
    matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    Solution().spiralOrder(matrix);
    matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}};
    Solution().spiralOrder(matrix);
    matrix = {{7}, {9}, {6}};
    Solution().spiralOrder(matrix);
    return 0;
}