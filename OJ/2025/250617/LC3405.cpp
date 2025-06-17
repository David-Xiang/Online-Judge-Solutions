/*
 * @lc app=leetcode id=3405 lang=cpp
 *
 * [3405] Count the Number of Arrays with K Matching Adjacent Elements
 */

#include <iostream>

using namespace std;

// @lc code=start
class Solution {
public:
    int countGoodArrays(int n, int m, int k) {
        // 选k个位置，数字固定。剩下n-k个位置可以随便放
        // C(n-1, k) * m * ((m - 1) ** (n - k - 1))
        int mod = 1000000007;
        long ans = factorial(n - 1, mod);
        int div1 = factorial(k, mod);
        int div2 = factorial(n - 1 - k, mod);
        ans = (ans * inv(div1, mod)) % mod;
        ans = (ans * inv(div2, mod)) % mod;
        ans = (ans * m) % mod;
        ans = (ans * fast_pow(m - 1, n - k - 1, mod)) % mod;
        return int(ans);
    }
    int fast_pow(int b, int k, int mod) {
        long ans = 1;
        long pow = b;
        while (k) {
            if (k & 1) {
                ans = (ans * pow) % mod;
            }
            k = k >> 1;
            pow = (pow * pow) % mod;
        }
        return int(ans);
    }
    int inv(int a, int mod) { return fast_pow(a, mod - 2, mod); }
    int factorial(int n, int mod) {
        long ans = 1;
        for (int i = 2; i <= n; ++i) {
            ans = (ans * i) % mod;
        }
        return int(ans);
    }
};
// @lc code=end
int main() {
    cout << Solution().countGoodArrays(3, 2, 1) << endl;
    cout << Solution().countGoodArrays(4, 2, 2) << endl;
    cout << Solution().countGoodArrays(5, 2, 0) << endl;
    cout << Solution().countGoodArrays(5581, 58624, 4766) << endl;
    // cout << Solution().fast_pow(2, 10, 1000007) << endl;
    // cout << Solution().factorial(5, 100007) << endl;
    return 0;
}
