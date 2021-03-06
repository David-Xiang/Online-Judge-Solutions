// Openjudge 275 Drainage Ditches
// Maximum Flow in weighted directed graph
// Edmond-Karp Algorithm

#include <iostream>
#include <queue>
#include <cstring>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 300
#define INF (1<<30)

using namespace std;
int g[MAXN][MAXN];  // edges(weight) of the graph
int pre[MAXN];      // preious node in each path
bool vis[MAXN];     // whether the node is visited
int n, e;           // number of nodes and edges
int src, sink;      // source and sink

int min(int a, int b){
    return a > b ? b : a;
}

unsigned augment(){      // find augmented path
    deque<int> q;
    memset(pre, 0, sizeof(pre));
    memset(vis, 0, sizeof(vis));

    pre[src] = src;
    vis[src] = true;
    q.push_back(src);

    bool foundpath = false;
    // use bfs to find a valid path from src to sink

    while (!q.empty() && !foundpath){
        int v = q.front();
        q.pop_front();
        for (int i = 0; i < n; i++){
            if (g[v][i] > 0 && vis[i] == false){
                // found an edge leading to an unvisted node
                pre[i] = v;
                vis[i] = true;
                if (i == sink){
                    foundpath = true;
                    q.clear();  // clear queue
                    break;
                }else{
                    q.push_back(i);
                }
            }
        }
    }

    if (!foundpath){
        return 0;
    }
    int minflow = INF;
    int v = sink;
    
    // find the min flow of augmented path (smallest weight of edge)
    while(v != src){
        minflow = min(minflow, g[pre[v]][v]);
        v = pre[v];
    }

    // add reverse edge along this path and modify all the capcity
    v = sink;
    while(v != src){
        g[pre[v]][v] -= minflow;
        g[v][pre[v]] += minflow;
        v = pre[v];
    }
    return minflow;
}

void init(){
    // construct the graph
    memset(g, 0, sizeof(g));
    src = 0;
    sink = n-1;
    for (int i = 0; i < e; i++){
        int u, v, w;
        cin >> u >> v >> w;
        g[u-1][v-1] += w;   // there may be more than 1 edge between 2 nodes
    }
}

int main(){
    ioOptimizer;
    int edges;
    while (cin >> e >> n){
        init();
        unsigned maxflow = 0;
        unsigned aug = 0;
        while((aug = augment()) != 0){
            maxflow += aug;
        }
        cout << maxflow << endl;
    }
    return 0;
}