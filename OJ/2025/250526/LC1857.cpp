/*
 * @lc app=leetcode id=1857 lang=cpp
 *
 * [1857] Largest Color Value in a Directed Graph
 */

#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>> &edges) {
        int visited = 0;
        queue<int> to_visit = {};
        map<int, int> in_degree = {};
        map<int, vector<int>> adj_to = {};
        map<int, vector<int>> adj_from = {};
        vector<vector<int>> dp = {};

        for (int i = 0; i < colors.length(); ++i) {
            in_degree[i] = 0;
            adj_to[i] = vector<int>();
            adj_from[i] = vector<int>();
            dp.emplace_back(vector<int>(26, 0));
        }

        for (vector<int> &e : edges) {
            int from = e[0];
            int to = e[1];
            ++in_degree[to];
            adj_to[from].push_back(to);
            adj_from[to].push_back(from);
        }

        for (int i = 0; i < colors.length(); ++i) {
            if (in_degree[i] == 0) {
                to_visit.push(i);
            }
        }

        int ans = 0;
        while (!to_visit.empty()) {
            int p = to_visit.front();
            for (int i = 0; i < 26; ++i) {
                int max_c = 0;
                for (int f : adj_from[p]) {
                    max_c = max(dp[f][i], max_c);
                }
                dp[p][i] = max_c + (colors[p] == ('a' + i));
                ans = max(ans, dp[p][i]);
            }
            for (int n : adj_to[p]) {
                --in_degree[n];
                if (in_degree[n] == 0) {
                    to_visit.push(n);
                }
            }
            to_visit.pop();
            ++visited;
        }

        if (visited < colors.length()) {
            return -1;
        }

        return ans;
    }
};
// @lc code=end

int main() {
    string colors = "abaca";
    vector<vector<int>> edges = {{0,1}, {0,2}, {2,3}, {3,4}};
    cout << Solution().largestPathValue(colors, edges) << endl;
    colors = "a";
    edges = {{0,0}};
    cout << Solution().largestPathValue(colors, edges) << endl;
    return 0;
}