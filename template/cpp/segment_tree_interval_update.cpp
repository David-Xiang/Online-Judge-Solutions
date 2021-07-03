// Segment Tree Algo
// Single Point Update + Interval Query
// Lazy Update

#include <iostream>
#include <cstdio>
#include <cstring>
#define MAXN 10
using namespace std;

struct Node{
    int l, r;
    int sum, inc;
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

void update(int root, int i, int j, int delta){
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

int query(int root, int i, int j){
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
    
    num = 10;
    buildtree(0, 1, num);
    for (int i = 1; i <= num; i++){
        update(0, i, i, i);             // 将第i个到第i个的值加i（其实就是将第i个的值设为i）
    }

    update(0, 1, 2, 1);
    update(0, 3, 6, 10);
    printf("%d\n", (query(0, 2, 5)));     // ans = 45

    return 0;
}
