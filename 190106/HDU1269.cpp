// HDUOJ 1269
// Maze Castle
// Tarjan Algo

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <stack>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 10
using namespace std;

int n;
int id;
typedef vector<int> Edge;
vector<Edge> edges(MAXN);   // 这句是初始化！
int dfn[MAXN];
int low[MAXN];
bool visited[MAXN];
bool onstack[MAXN];
stack<int> stk;

inline int min(int a, int b){
    return a < b ? a : b;
}

int tarjan(int u){
    dfn[u] = low[u] = id++;
    visited[u] = true;
    onstack[u] = true;
    stk.push(u);
    
    for (int i = 0; i < edges[u].size(); i++){
        int v = edges[u][i];
        if (!visited[v]){
            tarjan(v);
            low[u] = min(low[u], low[v]);
        }else if(onstack[v]){
            low[u] = min(low[u], dfn[v]);
        }
    }
    int ans = 0;
    if (dfn[u] == low[u]){
        int lasttop = -1;
        while(lasttop != u){
            lasttop = stk.top();
            stk.pop();
            onstack[lasttop] = false;
            ans++;
        }
    }
    return ans;
}

void init(){
    id = 0;
    while(!stk.empty())
        stk.pop();
    for (int i = 0; i < edges.size(); i++)
        edges[i].clear();
    memset(dfn, 0, sizeof(dfn));
    memset(low, 0, sizeof(low));
    memset(visited, 0, sizeof(visited));
    memset(onstack, 0, sizeof(onstack));
}

bool solve(){
    init();
    int m;
    cin >> n >> m;
    if (n == 0)
        return false;
    for (int i = 0; i < m; i++){
        int u, v;
        cin >> u >> v;
        edges[u].push_back(v);
    }
    if (tarjan(1) == n)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
    return true;
}

int main(){
    ioOptimizer;
    while(solve()){}
    return 0;
}
