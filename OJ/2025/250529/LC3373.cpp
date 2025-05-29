/*
 * @lc app=leetcode id=3373 lang=cpp
 *
 * [3373] Maximize the Number of Target Nodes After Connecting Trees II
 */
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>> &edges1,
                               vector<vector<int>> &edges2) {
        vector<vector<int>> adj1(edges1.size() + 1, vector<int>());
        vector<vector<int>> adj2(edges2.size() + 1, vector<int>());
        vector<int> color1(edges1.size() + 1, -1);

        for (vector<int> &e : edges1) {
            adj1[e[0]].push_back(e[1]);
            adj1[e[1]].push_back(e[0]);
        }
        for (vector<int> &e : edges2) {
            adj2[e[0]].push_back(e[1]);
            adj2[e[1]].push_back(e[0]);
        }

        int max_target2 = dfs(adj2, 0, -1, false);
        max_target2 = max(max_target2, int(edges2.size()) + 1 - max_target2);

        colorDFS(adj1, color1, 0, -1, 0);
        int target_even = dfs(adj1, 0, -1, true);
        int target_odd = int(edges1.size()) + 1 - target_even;
        target_even += max_target2;
        target_odd += max_target2;
        vector<int> ans;
        for (int i = 0; i < edges1.size() + 1; ++i) {
            ans.push_back(color1[i] == 0 ? target_even : target_odd);
        }
        return ans;
    }

    void colorDFS(vector<vector<int>> &adj, vector<int> &color, int node,
                  int father, int colorValue) {
        color[node] = colorValue;
        for (int next : adj[node]) {
            if (next == father) {
                continue;
            }
            colorDFS(adj, color, next, node, 1 - colorValue);
        }
    }

    int dfs(vector<vector<int>> &adj, int node, int father, bool even) {
        int ans = even ? 1 : 0;
        for (int next : adj[node]) {
            if (next == father) {
                continue;
            }
            ans += dfs(adj, next, node, !even);
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<vector<int>> edges1 = {{0, 1}, {0, 2}, {2, 3}, {2, 4}};
    vector<vector<int>> edges2 = {{0, 1}, {0, 2}, {0, 3}, {2, 7},
                                  {1, 4}, {4, 5}, {4, 6}};
    vector<int> ans = Solution().maxTargetNodes(edges1, edges2);
    for (int v : ans) {
        cout << v << " ";
    }
    cout << endl;

    edges1 = {{0, 1}, {0, 2}, {0, 3}, {0, 4}};
    edges2 = {{0, 1}, {1, 2}, {2, 3}};
    ans = Solution().maxTargetNodes(edges1, edges2);
    for (int v : ans) {
        cout << v << " ";
    }
    cout << endl;
    return 0;
}