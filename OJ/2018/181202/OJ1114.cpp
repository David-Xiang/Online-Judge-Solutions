// Openjudge 1114 Optimal Milking
// Maxflow (Dinic) + Shortest Distance (Floyd)

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
int n;               // number of nodes and edges
int src, sink;          // source and sink

int k, c, m;            // k: #machines; c: #cows; m: max cows per machine

int dist[MAXN][MAXN];    // 0~k-1: machines, k~k+c-1: cows
int maxd, mind;

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

void floyd(){
    for (int l = 0; l < k + c; l++){    // 每次求中间标号点不超过l的最短路
        for (int i = 0; i < k + c; i++){
            for (int j = 0; j < k + c; j++){
                if (dist[i][l] == 0 || dist[l][j] == 0 || i == j)
                    continue;
                int len = dist[i][l] + dist[l][j];
                if (len < dist[i][j] || dist[i][j] == 0)
                    dist[i][j] = len;
            }
        }
    }

    maxd = 0, mind = INF;
    for (int i = k; i < k + c; i++){
        for (int j = 0; j < k; j++){
            int len = dist[i][j];
            if (len > maxd)
                maxd = len;
            if (len < mind && len != 0)
                mind = len;
        }
    }
}

void init(){
    // get dist info
    memset(dist, 0, sizeof(dist));
    cin >> k >> c >> m;
    for (int i = 0; i < k + c; i++){
        for (int j = 0; j < k + c; j++){
            cin >> dist[i][j];;
        }
    }

    /*
        Index used:
        0~k-1: machines
        k~k+c-1: cows
        k+c: src
        k+c+1: sink
    */
    n = k + c + 2;
    src = k + c;
    sink = k + c + 1;
}

void initgraph(int d){  // max dist to add an edge
    memset(g, 0, sizeof(g));

    // connect src and all cows
    for (int i = k; i < k + c; i++)
        g[src][i] = 1;
    
    // connect sink and all machines
    for (int i = 0; i < k; i++)
        g[i][sink] = m;

    // connect a machine and a cow if their distance <= d
    for (int i = 0; i < k; i++){
        for (int j = k; j < k + c; j++){
            if (dist[i][j] <= d && dist[i][j] > 0)
                g[j][i] = 1;
        }
    }
}

int main(){
    ioOptimizer;
    init();

    // get shortest distance
    floyd();

    // binary search for min maxdist
    while(maxd > mind + 1){
        int mid = (maxd + mind) / 2;

        // construct the graph and calculate maxflow
        initgraph(mid);
        int maxflow = dinic();

        if (maxflow < c){
            mind = mid;
        }else{
            maxd = mid;
        }
    }
    cout << maxd << endl;
    return 0;
}