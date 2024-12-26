// Openjudge 2439
// Banlanced Lineup
// Segment Tree

#include <iostream>
#include <cstring>
#include <cstdio>
#define MAXN 50050
#define INF (1 << 30)
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
using namespace std;

struct Node{
    int l, r;
    int max, min;
};
Node tree[MAXN*4];
int num;

void buildtree(int root, int i, int j){
    Node& n = tree[root];
    n.l = i;
    n.r = j;
    n.min = INF;
    n.max = 0;
    if (i != j){
        buildtree(2*root+1, i, (i+j)/2);
        buildtree(2*root+2, (i+j)/2+1, j);
    }
}

void insert(int root, int i, int val){
    Node& n = tree[root];
    if(val > n.max)
        n.max = val;
    if(val < n.min)
        n.min = val;
    
    if (n.l == n.r)
        return;
    
    int mid = (n.l+n.r)/2;
    if (i <= mid)
        insert(2*root+1, i, val);
    else
        insert(2*root+2, i, val);
}

int querymax(int root, int i, int j){
    Node& n = tree[root];
    if (n.l == i && n.r == j)
        return n.max;
    
    int mid = (n.l+n.r)/2;
    if (j <= mid)
        return querymax(2*root+1, i, j);
    else if(i > mid)
        return querymax(2*root+2, i, j);
    else{
        int max1 = querymax(2*root+1, i, mid);
        int max2 = querymax(2*root+2, mid+1, j);
        return max1 > max2 ? max1 : max2;
    }
}

int querymin(int root, int i, int j){
    Node& n = tree[root];
    if (n.l == i && n.r == j)
        return n.min;
    
    int mid = (n.l+n.r)/2;
    if (j <= mid)
        return querymin(2*root+1, i, j);
    else if(i > mid)
        return querymin(2*root+2, i, j);
    else{
        int min1 = querymin(2*root+1, i, mid);
        int min2 = querymin(2*root+2, mid+1, j);
        return min1 < min2 ? min1 : min2;
    }
}

int main(){
    int query;
    scanf("%d%d", &num, &query);
    buildtree(0, 1, num);
    for (int i = 0; i < num; i++){
        int t;
        scanf("%d", &t);
        insert(0, i+1, t);
    }
    while(query--){
        int i, j;
        scanf("%d%d", &i, &j);
        printf("%d\n", querymax(0, i, j) - querymin(0, i, j));
    }
    return 0;
}