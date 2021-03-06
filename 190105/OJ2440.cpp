// Openjudge 2440
// A Simple Problem with Integers
// Segment Tree Algo
// 重点是注意几个地方的更新操作为(r-l+1)*inc
#include <iostream>
#include <cstdio>
#include <cstring>
#define MAXN 10 // 100010
using namespace std;

struct Node{
    int l, r;
    long long sum, inc;
};

Node tree[MAXN*4];
int num;

void buildtree(int root, int l, int r){
    Node& n = tree[root];
    n.l = l;
    n.r = r;
    int mid = (l+r)/2;
    if (l != r){
        buildtree(2*root+1, l, mid);
        buildtree(2*root+2, mid+1, r);
    }
}

void update(int root, int i, int j, long long delta){
    Node& n = tree[root];
    if (n.l == i && n.r == j){
        n.inc += delta;
        return;
    }
    
    // else [i, j] < [n.l, n.r]
    n.sum += (j-i+1)*delta;             // !!!
    int mid = (n.l+n.r)/2;
    if (j <= mid)
        update(2*root+1, i, j, delta);
    else if(i > mid)
        update(2*root+2, i, j, delta);
    else{
        update(2*root+1, i, mid, delta);
        update(2*root+2, mid+1, j, delta);
    }
}

long long query(int root, int i, int j){
    Node& n = tree[root];
    if (n.l == i && n.r == j){
        return n.sum + (j-i+1)*n.inc;   // !!!
    }
    
    int mid = (n.r+n.l)/2;
    // finish lazy update
    if (n.inc != 0){
        n.sum += (n.r-n.l+1)*n.inc;     // !!!
        tree[2*root+1].inc += n.inc;
        tree[2*root+2].inc += n.inc;
        n.inc = 0;
    }
    
    if (j <= mid)
        return query(2*root+1, i, j);
    else if (i > mid)
        return query(2*root+2, i, j);
    else
        return query(2*root+1, i, mid) + query(2*root+2, mid+1, j);
}

int main(){
    memset(tree, 0, sizeof(tree));
    int testcase;
    scanf("%d%d\n", &num, &testcase);
    buildtree(0, 1, num);
    for (int i = 1; i <= num; i++){
        int t;
        scanf("%d", &t);
        update(0, i, i, t);
    }
    getchar();
    for (int i = 0; i < testcase; i++){
        char c[20];
        scanf("%s", c);
        if (c[0] == 'Q'){
            int l, r;
            scanf("%d%d", &l, &r);
            long long ans = query(0, l, r);
            printf("%lld\n", ans);
        }else{
            int l, r, d;
            scanf("%d%d%d", &l, &r, &d);
            update(0, l, r, d);
        }
    }
    return 0;
}
