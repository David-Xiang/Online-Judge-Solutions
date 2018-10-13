// OpenJudge 197
// Mobile Phones IOI2001
// Binary Indexed Array
#include <cstdio>
#define MAXN 1025
using namespace std;
int len;
int BIT[MAXN][MAXN] = {};

int lowbit(int x){
    return x & (-x);
}

int sum(int r, int t){
    int sum = 0;
    for (int i = r; i; i -= lowbit(i))
        for (int j = t; j; j -= lowbit(j))
            sum += BIT[i][j];
    return sum;
}

void update(int m, int n, int add){
    for (int i = m; i <= len; i += lowbit(i))
        for (int j = n; j <= len; j += lowbit(j))
            BIT[i][j] += add;
}

int sumRange(int l, int b, int r, int t){
    return sum(r, t) - sum(l - 1, t) - sum(r, b - 1) + sum(l - 1, b - 1);
}

int main(){
    scanf("0 %d", &len);
    int ins;
    scanf("%d", &ins);
    while(ins != 3){
        if (ins == 1) {
            int m, n, val;
            scanf("%d %d %d", &m, &n, &val);
            update(m+1, n+1, val);
        }else if(ins == 2){
            int l, b, r, t;
            scanf("%d %d %d %d", &l, &b, &r, &t);
            printf("%d\n", sumRange(l+1, b+1, r+1, t+1));
        }
        
        scanf("%d", &ins);
    }
    return 0;
}
