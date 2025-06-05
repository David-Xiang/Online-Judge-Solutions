/*
 * @lc app=leetcode id=1061 lang=cpp
 *
 * [1061] Lexicographically Smallest Equivalent String
 */

#include <iostream>
#include <map>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int find(int a, vector<int> &f) {
        if (f[a] != a) {
            f[a] = find(f[a], f);
        }
        return f[a];
    }
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        vector<int> f(26, 0);
        for (int i = 0; i < 26; ++i) {
            f[i] = i;
        }
        for (int i = 0; i < s1.size(); ++i) {
            int p1 = find(s1[i] - 'a', f);
            int p2 = find(s2[i] - 'a', f);
            if (p1 != p2) {
                f[p2] = p1;
            }
        }

        map<int, int> m;
        for (int i = 0; i < 26; ++i) {
            int fi = find(i, f);
            if (m.find(find(i, f)) == m.end()) {
                m[fi] = i;
            }
            m[fi] = min(m[fi], i);
        }

        string res;
        for (int i = 0; i < baseStr.size(); ++i) {
            res.push_back(m[find(baseStr[i] - 'a', f)] + 'a');
        }
        return res;
    }
};
// @lc code=end

int main() {
    cout << Solution().smallestEquivalentString("parker", "morris", "parser")
         << endl;
    cout << Solution().smallestEquivalentString("hello", "world", "hold")
         << endl;
    cout << Solution().smallestEquivalentString("leetcode", "programs",
                                                "sourcecode")
         << endl;
    return 0;
}
