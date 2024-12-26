// Openjudge 2524
// Ubiquitous Religion
// Union Find algo

#include <iostream>
#include <cstdio>
#include <cstring>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 50010

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

void solve(int testcase, int n, int m){
    for (int i = 0; i < n; i++){
        parent[i] = i;
    }

    int a, b;
    for (int i = 0; i < m; i++){
        cin >> a >> b;
        Union(a-1, b-1);
    }

    int ans = 0;
    for (int i = 0; i < n; i++){
        if (parent[i] == i)
            ++ans;
    }
    printf("Case %d: %d\n", testcase, ans);
}

int main(){
    ioOptimizer;
    int n, m;
    int testcase = 1;
    while(1){
        cin >> n >> m;
        if (n == 0)
            break;
        solve(testcase, n, m);
        ++testcase;
    }
    return 0;
}