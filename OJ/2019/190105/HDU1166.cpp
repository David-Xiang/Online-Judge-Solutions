// HDUOJ 1166
// The Enemy Position
// Segment Tree Algo

#include <iostream>
#include <cstdio>
#include <cstring>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 50050
using namespace std;

struct Node{
    int l, r, val;
};
Node tree[MAXN*4];
int num;

void buildtree(int root, int i, int j){
    Node& n = tree[root];
    n.l = i;
    n.r = j;
    n.val = 0;
    if (i != j){
        buildtree(2*root+1, i, (i+j)/2);
        buildtree(2*root+2, (i+j)/2+1, j);
    }
}

void insert(int root, int i, int delta){
    Node& n = tree[root];
    n.val += delta;
    if (n.r == n.l)
        return;
    else if(i <= (n.r+n.l)/2)
        insert(2*root+1, i, delta);
    else
        insert(2*root+2, i, delta);
}

int sum(int root, int i, int j){
    Node& n = tree[root];
    if(n.l == i && n.r == j)
        return n.val;
    int mid = (n.r+n.l)/2;
    if(j <= mid)
        return sum(2*root+1, i, j);
    else if(i > mid)
        return sum(2*root+2, i, j);
    else
        return sum(2*root+1, i, mid) + sum(2*root+2, mid+1, j);
}

void solve(){
    memset(tree, 0, sizeof(tree));
    scanf("%d", &num);
    buildtree(0, 1, num);
    
    int tmp;
    char str[30];
    for (int i = 1; i <= num; i++){
        scanf("%d", &tmp);
        insert(0, i, tmp);
    }
    int i, j;
    while(1){
        scanf("%s", str);
        if (strcmp(str, "Query") == 0){
            scanf("%d%d", &i, &j);
            printf("%d\n", sum(0, i, j));
        }else if(strcmp(str, "Add") == 0){
            scanf("%d%d", &i, &j);
            insert(0, i, j);
        }else if(strcmp(str, "Sub") == 0){
            scanf("%d%d", &i, &j);
            insert(0, i, -j);
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