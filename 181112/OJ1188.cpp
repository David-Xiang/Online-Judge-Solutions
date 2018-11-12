// Openjudge 1188
// Popular Cows 
// graph connnectivity

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <stack>

#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 10010
#define SCC 10010
using namespace std;

typedef vector<int> Edge;
vector<Edge> edges(MAXN);
int in[MAXN];
int out[MAXN];
int N, M;
int id, sccCnt;

stack<int> stk;
int dfn[MAXN];
int low[MAXN];
int scc[MAXN];
bool onstack[MAXN];

inline int min(int a, int b){
    return a > b ? b : a;
}

void init(){
    memset(dfn, 0, sizeof(dfn));
    memset(low, 0, sizeof(low));
    memset(scc, 0, sizeof(scc));
    memset(onstack, 0, sizeof(onstack));
    memset(in, 0, sizeof(in));
    memset(out, 0, sizeof(out));

    id = 0;
    sccCnt = 0;
    cin >> N >> M;
    for (int i = 0; i < M; i++){
        int from, to;
        cin >> from >> to;
        edges[from].push_back(to);
    }
}

void Tarjan(int u){
    // template
    dfn[u] = low[u] = ++id;              // init dfn and low with index
    stk.push(u);
    onstack[u] = true;
    
    int len = edges[u].size();
    for (int i = 0; i < len; i++){
        int v = edges[u][i];
        if (!dfn[v]){
            Tarjan(v);
            low[u] = min(low[u], low[v]);
        }else if(onstack[v]){
            low[u] = min(low[u], dfn[v]);
        }
    }
    
    if (dfn[u] == low[u]){
        int top = -1;
        while(top != u){
            top = stk.top();
            stk.pop();
            onstack[top] = false;
            scc[top] = sccCnt;      
            // mark all strongly connected components
        }
        ++sccCnt;
    }
}

int main(){
    ioOptimizer;
    init();

    for(int i = 1; i <= N; i++){
        if (!dfn[i])
            Tarjan(i);
    }

    
    for (int i = 1; i <= N; i++){
        for (int j = 0; j < edges[i].size(); j++){
            int v = edges[i][j];
            if (scc[i] != scc[v]){
                in[scc[v]]++;
                out[scc[i]]++;
                // count in-degree and out-degree
            }
        }
    }

    int zeroCnt = 0;
    int lastScc = 0;
    for(int i = 0; i < sccCnt; i++){
        if (out[i] == 0){
            ++zeroCnt;
            lastScc = i;
        }
    }
    
    if (zeroCnt == 1){
        int count = 0;
        for (int i = 1; i <= N; i++){
            if (scc[i] == lastScc){
                ++count;
            }
        }
        cout << count << endl;
    }else{
        cout << 0 << endl;
    }

    return 0;
}