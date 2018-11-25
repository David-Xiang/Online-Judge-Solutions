// Openjudge 525 Single Point of Failure
// Tarjan Algorithm: Cut vertexs of a undirected graph
// 对于原版的Tarjan算法稍微做了一下修改

#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>

#define MAXN 1010
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)

using namespace std;
typedef vector<int> Edge;
vector<Edge> edges(MAXN);

int dfn[MAXN];
int low[MAXN];
int res[MAXN];          // how many subnets will if the node is a cut vertex
int id;
int root;

inline int min(int a, int b){
    return a < b ? a : b;
}

void tarjan(int u, int fa){     // 相比原版的tarjan，可以去除stk的相应信息
    dfn[u] = low[u] = ++id;
    
    int len = edges[u].size();
    int count = 0;
    for (int i = 0; i < len; i++){
        int v = edges[u][i];
        if (!dfn[v]){
            tarjan(v, u);
            if (low[v] >= dfn[u])
                res[u] ++;      // 子节点只有一个路径到达u，因此u是割点
            
            low[u] = min(low[u], low[v]);
        }else if(v != fa){
            low[u] = min(low[u], dfn[v]);
        }
    }
    if (u == root && res[u] >= 1)
        res[u] --;             // 如果根节点是割点，则res-1才是对应的连通块数目
}

int main(){
    ioOptimizer;
    int testcase = 0;
    int from, to;
    cin >> from;
    while(from != 0){
        id = 0;
        root = from;
        cin >> to;

        edges.clear();              // 需要清除edges和它每一个元素（也是vector）的内容
        for (int i = 0; i < MAXN; i++)
            edges[i].clear();
        memset(dfn, 0, sizeof(dfn));
        memset(low, 0, sizeof(low));
        memset(res, 0, sizeof(res));

        edges[from].push_back(to);
        edges[to].push_back(from);
        cin >> from;
        while (from != 0){
            cin >> to;
            edges[from].push_back(to);
            edges[to].push_back(from);
            cin >> from;
        }
        cout << "Network #" << ++testcase << endl;
        
        // do tarjan from root
        tarjan(root, -1);
        
        int count = 0;
        for (int i = 0; i < MAXN; i++){
            if (res[i] >= 1){
                cout << "  SPF node " << i << " leaves " << res[i]+1 << " subnets" << endl;
                count ++;
            }
        }
        if (count == 0)
            cout << "  No SPF nodes" << endl;
        cout << endl;
        
        cin >> from;
    }
    return 0;
}
