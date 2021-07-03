// Binary Indexed Tree Template
// NOTE: array starts from 1 (NOT 0)

#include <iostream>
#include <cstdio>
#include <cstring>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 20
using namespace std;
 
int num;        // length of array
int bit[MAXN];  // binary indexed array

int lowbit(int n){
    return n & (-n);
}

void update(int n, int delta){
    for (int i = n; i <= num; i += lowbit(i))  // i "<=" num!!!!
        bit[i] += delta;
}

int sum(int n){
    int ans = 0;
    for (int i = n; i > 0; i -= lowbit(i))    // i > 0
        ans += bit[i];
    return ans;
}

int sumRange(int i, int j){                     // a[i] + ... + a[j]
    return sum(j) - sum(i - 1);
}

int main(){
    memset(bit, 0, sizeof(bit));

    num = 10;
    for (int i = 1; i <= num; i++)
        update(i, i);
    printf("1+...+10=%d\n", sumRange(1, num));
    return 0;
}