/*
 * @lc app=leetcode id=2434 lang=cpp
 *
 * [2434] Using a Robot to Print the Lexicographically Smallest String
 */

#include <iostream>
#include <stack>

using namespace std;

// @lc code=start
class Solution {
public:
    string robotWithString(string s){
        int remain[26] = {0};
        for (char c: s) {
            ++remain[c - 'a'];
        }

        stack<char> stk;
        int ptr = 26;
        for (int i = 0; i < 26; ++i) {
            if (remain[i] > 0) {
                ptr = i;
                break;
            }
        }

        string ans;
        for (char c: s) {
            stk.push(c);
            --remain[c - 'a'];
            while (!stk.empty() && stk.top() <= 'a' + ptr) {
                ans += stk.top();
                stk.pop();
                while (ptr < 26 && remain[ptr] == 0) {
                    ptr++;
                }
            }
        }
        return ans;
    }
};
// @lc code=end

int main() {
    cout << Solution().robotWithString("zza") << endl;
    cout << Solution().robotWithString("bac") << endl;
    cout << Solution().robotWithString("bdda") << endl;
    return 0;
}
