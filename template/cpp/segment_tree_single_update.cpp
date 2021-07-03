// Segment Tree Algo
// Single Point Update + Interval Query

#include <iostream>
#include <cstdio>
#include <cstring>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 10
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
    num = 10;
    buildtree(0, 1, num);

    for (int i = 1; i <= num; i++){
        insert(0, i, i);
    }
    
    cout << sum(0, 1, 5) << endl;
    cout << sum(0, 4, 10) << endl;
    insert(0, 7, 10);
    cout << sum(0, 6, 7) << endl;
}

int main(){
    solve();
    return 0;
}