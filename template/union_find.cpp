// Union Find algo

#include <iostream>
#include <cstdio>
#include <cstring>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 50

using namespace std;

int parent[MAXN];

int Find(int a){
    if (parent[a] != a){
        parent[a] = Find(parent[a]);
    }
    return parent[a];
}

void Union(int a, int b){
    int pa = Find(a);
    int pb = Find(b);

    if(pa != pb)
        parent[pb] = pa;
}

void solve(){
    int n = 4;
    for (int i = 0; i < n; i++){
        parent[i] = i;
    }

    Union(0, 1);
    Union(2, 3);

    int ans = 0;
    for (int i = 0; i < n; i++){
        if (parent[i] == i)
            ++ans;
    }
    printf("%d\n", ans);
}

int main(){
    ioOptimizer;
    solve();
    return 0;
}