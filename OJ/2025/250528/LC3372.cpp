/*
 * @lc app=leetcode id=3372 lang=cpp
 *
 * [3372] Maximize the Number of Target Nodes After Connecting Trees I
 */

#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <tuple>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>> &edges1,
                               vector<vector<int>> &edges2, int k) {
        vector<int> target1(edges1.size() + 1, 0);
        vector<int> target2(edges2.size() + 1, 0);
        constructTarget(edges1, k, target1);
        int max_target2 = 0;
        if (k > 0) {
            constructTarget(edges2, k - 1, target2);
            max_target2 = *max_element(target2.begin(), target2.end());
        }

        for (int i = 0; i < edges1.size() + 1; ++i) {
            target1[i] += max_target2;
        }
        return target1;
    }

    int dfs(int i, int k, int p, vector<vector<int>> &adj) {
        int ans = 1;
        if (k == 0) {
            return ans;
        }
        
        for (int n : adj[i]) {
            if (n != p) {
                ans += dfs(n, k - 1, i, adj);
            }
        }
        return ans;
    }

    void constructTarget(vector<vector<int>> &edges, int k,
                         vector<int> &target) {
        int nums = edges.size() + 1;
        vector<vector<int>> adj(nums, vector<int>());
        for (vector<int> e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        for (int i = 0; i < nums; ++i) {
            target[i] = dfs(i, k, -1, adj);
        }
    }

    void constructTargetBFS(vector<vector<int>> &edges, int k,
                            vector<int> &target) {
        int nums = edges.size() + 1;
        vector<vector<int>> adj(nums, vector<int>());
        for (vector<int> e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }

        for (int i = 0; i < nums; ++i) {
            int ans = 0;
            set<int> visited;
            queue<tuple<int, int>> q;

            visited.emplace(i);
            q.push({i, 0});
            ans++;

            while (!q.empty()) {
                tuple<int, int> t = q.front();
                q.pop();
                int n = get<0>(t);
                int l = get<1>(t);
                if (l >= k) {
                    continue;
                }
                for (int m : adj[n]) {
                    if (visited.find(m) == visited.end()) {
                        visited.emplace(m);
                        ans++;
                        q.push({m, l + 1});
                    }
                }
            }
            target[i] = ans;
        }
    }

    void constructTargetDP(vector<vector<int>> &edges, int k,
                           vector<int> &target) {
        map<tuple<int, int>, int> edgeIndex;
        int numEdges = edges.size();
        vector<vector<int>> adj(numEdges + 1, vector<int>());
        for (int i = 0; i < numEdges; ++i) {
            int s = edges[i][0], t = edges[i][1];
            edgeIndex[{s, t}] = 2 * i;
            edgeIndex[{t, s}] = 2 * i + 1;
            adj[s].push_back(t);
            adj[t].push_back(s);
        }

        vector<vector<int>> dp(2 * numEdges, vector<int>(k + 1, 0));
        // 表示以s为起点，通过t达到target为k的节点数量
        for (int l = 1; l <= k; ++l) {
            for (int i = 0; i < numEdges; ++i) {
                for (int j = 0; j < 2; ++j) {
                    int s = edges[i][0];
                    int t = edges[i][1];
                    if (j == 1) {
                        s = edges[i][1];
                        t = edges[i][0];
                    }
                    int e = edgeIndex[{s, t}];
                    dp[e][l] = 1; // t本身
                    if (l == 1) {
                        continue;
                    }
                    for (int n : adj[t]) {
                        if (n == s) {
                            continue;
                        }
                        int en = edgeIndex[{t, n}];
                        dp[e][l] += dp[en][l - 1];
                    }
                }
            }
        }
        for (int i = 0; i < numEdges + 1; ++i) {
            target[i] = 1;
            for (int n : adj[i]) {
                int e = edgeIndex[{i, n}];
                target[i] += dp[e][k];
            }
        }
    }
};
// @lc code=end
int main() {
    vector<vector<int>> edges1 = {{0, 1}, {0, 2}, {2, 3}, {2, 4}};
    vector<vector<int>> edges2 = {{0, 1}, {0, 2}, {0, 3}, {2, 7},
                                  {1, 4}, {4, 5}, {4, 6}};
    vector<int> ans = Solution().maxTargetNodes(edges1, edges2, 2);
    for (int v : ans) {
        cout << v << " ";
    }
    cout << endl;

    edges1 = {{0, 1}, {0, 2}, {0, 3}, {0, 4}};
    edges2 = {{0, 1}, {1, 2}, {2, 3}};
    ans = Solution().maxTargetNodes(edges1, edges2, 1);
    for (int v : ans) {
        cout << v << " ";
    }
    cout << endl;
    return 0;
}