/*
 * @lc app=leetcode id=1202 lang=cpp
 *
 * [1202] Smallest String With Swaps
 */

#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int find(vector<int> &p, int i) {
        if (p[i] != i) {
            p[i] = find(p, p[i]);
        }
        return p[i];
    }
    string smallestStringWithSwaps(string s, vector<vector<int>> &pairs) {
        vector<int> p;
        for (int i = 0; i < s.size(); ++i) {
            p.push_back(i);
        }
        for (vector<int> v : pairs) {
            int a = v[0];
            int b = v[1];
            p[find(p, a)] = find(p, b);
        }
        map<int, vector<char>> cluster;
        map<int, vector<char>::iterator> pointers;
        for (int i = 0; i < s.size(); ++i) {
            int root = find(p, i);
            if (cluster.find(root) == cluster.end()) {
                cluster[root] = vector<char>();
            }
            cluster[root].push_back(s[i]);
        }
        for (auto it = cluster.begin(); it != cluster.end(); ++it) {
            int root = it->first;
            vector<char> &chars = it->second;
            sort(chars.begin(), chars.end());
            pointers[root] = chars.begin();
        }
        string ans;
        ans.reserve(s.size());
        for (int i = 0; i < s.size(); ++i) {
            int root = find(p, i);
            ans.push_back(*(pointers[root]));
            ++(pointers[root]);
        }
        return ans;
    }
};
// @lc code=end

int main() {
    string s = "dcab";
    vector<vector<int>> pairs = {{0, 3}, {1, 2}};
    cout << Solution().smallestStringWithSwaps(s, pairs) << endl;
    s = "dcab";
    pairs = {{0, 3}, {1, 2}, {0, 2}};
    cout << Solution().smallestStringWithSwaps(s, pairs) << endl;
    s = "cba";
    pairs = {{0, 1}, {1, 2}};
    cout << Solution().smallestStringWithSwaps(s, pairs) << endl;
    return 0;
}