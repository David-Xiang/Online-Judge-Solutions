// HDUOJ 1166
// The Enemy Position
// Binary Indexed Tree Template
#include <iostream>
#include <cstdio>
#include <cstring>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 50050
using namespace std;
 
int num;
int bit[MAXN];

int lowbit(int n){
    return n & (-n);
}

void update(int n, int add){
    for (int i = n; i <= num; i += lowbit(i)){
        bit[i] += add;
    }
}

int sum(int n){
    int ans = 0;
    for (int i = n; i > 0; i -= lowbit(i)){
        ans += bit[i];
    }
    return ans;
}

int sumRange(int i, int j){
    // a[i] + ... + a[j]
    return sum(j) - sum(i - 1);
}

void solve(){
    memset(bit, 0, sizeof(bit));
    scanf("%d", &num);
    int tmp;
    char str[30];
    for (int i = 1; i <= num; i++){
        scanf("%d", &tmp);
        update(i, tmp);
    }
    int i, j;
    while(1){
        scanf("%s", str);
        if (strcmp(str, "Query") == 0){
            scanf("%d%d", &i, &j);
            printf("%d\n", sumRange(i, j));
        }else if(strcmp(str, "Add") == 0){
            scanf("%d%d", &i, &j);
            update(i, j);
        }else if(strcmp(str, "Sub") == 0){
            scanf("%d%d", &i, &j);
            update(i, -j);
        }else if(strcmp(str, "End") == 0){
            return;
        }
    }

}

int main(){
    int testcase;
    scanf("%d", &testcase);
    for(int i = 0; i < testcase; i++){
        printf("Case %d:\n", i+1);
        solve();
    }
    return 0;
}