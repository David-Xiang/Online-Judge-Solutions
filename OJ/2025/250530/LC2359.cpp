/*
 * @lc app=leetcode id=2359 lang=cpp
 *
 * [2359] Find Closest Node to Given Two Nodes
 */

#include <iostream>
#include <set>

using namespace std;

// @lc code=start
class Solution {
public:
    int closestMeetingNode(vector<int> &edges, int node1, int node2) {
        set<int> visited1;
        set<int> visited2;
        for (int step = 0; step < edges.size(); ++step) {
            visited1.emplace(node1);
            visited2.emplace(node2);
            int ans1 = -1;
            int ans2 = -1;
            if (node1 != -1) {
                if (visited2.find(node1) != visited2.end()) {
                    ans1 = node1;
                }
                node1 = edges[node1];
            }
            if (node2 != -1) {
                if (visited1.find(node2) != visited1.end()) {
                    ans2 = node2;
                }
                node2 = edges[node2];
            }
            if (ans1 >= 0 && ans2 >= 0) {
                return min(ans1, ans2);
            }
            if (ans1 >= 0) {
                return ans1;
            }
            if (ans2 >= 0) {
                return ans2;
            }
        }
        return -1;
    }
};
// @lc code=end

int main() {
    vector<int> edges = {2, 2, 3 - 1};
    int node1 = 0, node2 = 1;
    cout << Solution().closestMeetingNode(edges, node1, node2) << endl;

    edges = {1, 2, -1};
    node1 = 0, node2 = 2;
    cout << Solution().closestMeetingNode(edges, node1, node2) << endl;

    edges = {5, -1, 3, 4, 5, 6, -1, -1, 4, 3};
    node1 = 0, node2 = 0;
    cout << Solution().closestMeetingNode(edges, node1, node2) << endl;

    edges = {4, 4, 8, -1, 9, 8, 4, 4, 1, 1};
    node1 = 5, node2 = 6;
    cout << Solution().closestMeetingNode(edges, node1, node2) << endl;

    return 0;
}