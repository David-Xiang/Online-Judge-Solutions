// Maximum Flow in weighted directed graph
// Dinic Algorithm

#include <iostream>
#include <cstring>
#include <cstdio>
#include <set>
#include <vector>
#include <queue>

#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 10
#define INF (1<<30)

using namespace std;
int g[MAXN][MAXN];      // edges(weight) of the graph
bool vis[MAXN];         // whether the node is visited
int layer[MAXN];        // node i is in which layer
int n, e;               // number of nodes and edges
int src, sink;          // source and sink

bool countlayer(){
    deque<int> q;
    memset(layer, -1, sizeof(layer));
    
    // init
    layer[src] = 0;
    q.push_back(src);

    while (!q.empty()){
        int v = q.front();
        q.pop_front();
        for (int j = 0; j < n; j++){
            if (g[v][j] > 0 && layer[j] == -1){
                // layer[j] == -1 means it's not visited
                layer[j] = layer[v] + 1;
                if (j == sink)
                    return true;
                else
                    q.push_back(j);
            }
        }
    }
    return false;
}

int dinic(){
    int maxflow = 0;
    deque<int> q;           // stack used by DFS
    while(countlayer()){    // src and sink are connected
        q.push_back(src);
        memset(vis, 0, sizeof(vis));
        vis[src] = true;

        while (!q.empty()){
            int nd = q.back();
            if (nd == sink){    // nd is sink 
                // find the min flow of the path
                int minc = INF;
                int minc_u;    // "from node" of min flow edge
                for (int i = 1; i < q.size(); i++){
                    int u = q[i-1];
                    int v = q[i];
                    if (g[u][v] > 0){   // found an edge
                        if (minc > g[u][v]){
                            minc = g[u][v];
                            minc_u = u;
                        }
                    }
                }

                // use this augmented path and modify the graph
                maxflow += minc;
                for (int i = 1; i < q.size(); i++){
                    int u = q[i-1];
                    int v = q[i];
                    g[u][v] -= minc;
                    g[v][u] += minc;
                }

                // pop stack until "minc_u" becomes top of stack
                // and continue DFS
                while (!q.empty() && q.back() != minc_u){
                    vis[q.back()] = 0;
                    q.pop_back();
                }
            }else{
                // nd is not sink
                // do DFS
                int i = 0;
                for (i = 0; i < n; i++){
                    if (g[nd][i] > 0 && layer[i] == layer[nd] + 1 && !vis[i]){
                        // must satisfy these three conditions
                        vis[i] = 1;
                        q.push_back(i);
                        break;
                    }
                }
                
                if (i >= n){
                    // there's no next node
                    q.pop_back();
                    // go back
                }
            }
        }
    }
    return maxflow;
}

void init(){
    // construct the graph
    memset(g, 0, sizeof(g));
    n = 4;
    e = 5;
    src = 0;
    sink = 3; 
    g[0][1] = 40;
    g[0][3] = 20;
    g[1][3] = 20;
    g[1][2] = 30;
    g[2][3] = 10;

    //for (int i = 0; i < e; i++){
    //    int u, v, w;
    //    cin >> u >> v >> w;
    //    g[u][v] += w;   // there may be more than 1 edge between 2 nodes
    //}
}

int main(){
    ioOptimizer;
    init();
    cout << dinic() << endl;
    return 0;
}