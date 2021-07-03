// Tarjan algorithm
// Graph strongly connected components
#include <iostream>
#include <memory>
#include <stack>
#include <vector>

#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 10
using namespace std;

typedef vector<int> Edge;
vector<Edge> edges(MAXN);

stack<int> stk;
int dfn[MAXN];
int low[MAXN];
bool visited[MAXN];
bool onstack[MAXN];
int id;
int n;

inline int min(int a, int b){
    return a > b ? b : a;
}
void init(){
    memset(dfn, 0, sizeof(dfn));
    memset(low, 0, sizeof(low));
    memset(visited, 0, sizeof(visited));
    memset(onstack, 0, sizeof(onstack));
    for (int i = 0; i < edges.size(); i++)
        edges[i].clear();
    while(!stk.empty())
        stk.pop();
    
    // example
    id = 0;
    n = 7;
    edges[0].push_back(1);
    edges[0].push_back(5);
    edges[1].push_back(2);
    edges[2].push_back(3);
    edges[2].push_back(4);
    edges[3].push_back(1);
    edges[3].push_back(4);
    edges[5].push_back(6);
    edges[6].push_back(0);
}

void Tarjan(int u){
    visited[u] = true;
    dfn[u] = low[u] = ++id;              // init dfn and low with index
    stk.push(u);
    onstack[u] = true;
    
    int len = edges[u].size();
    for (int i = 0; i < len; i++){
        int v = edges[u][i];
        if (!visited[v]){
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
            cout << top << " ";   
            // mark all strongly connected components
        }
        cout << endl;
        // output: each line is a strongly connected component
    }
}

int main(){
    ioOptimizer;
    init();
    for (int i = 0; i < n; i++){
        if (!visited[i])
            Tarjan(i);
    }
    return 0;
}
