// POJ 3259
// Wormholes
// Bellman-Ford Algo for detecting negative weight cycle
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#define INF (1 << 30)
#define MAXN 10
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
using namespace std;

struct Edge{
    int from, to, weight;
    Edge(int f, int t, int w){
        from = f;
        to = t;
        weight = w;
    }
    Edge(){ }
};
vector<Edge> edges;
int dist[MAXN];
int n, m, w;        // number of vertex, pos-weight edge(half) and neg-weight edge
/*
    Another way to present a graph:
    typedef vector<int> Edge;
    vector<Edge> edges;
    edges[from].push_back(to);
*/

bool bf(int u){
    dist[u] = 0;
    for (int i = 1; i < n; i++){    // 经过至多i条边到达u的最短距离（经过n条边则说明存在回路）
        for (int j = 0; j < edges.size(); j++){
            int from = edges[j].from;
            int to = edges[j].to;
            if(dist[from] < INF && dist[from] + edges[j].weight < dist[to])
                dist[to] = dist[from] + edges[j].weight;
        }
    }

    for (int i = 0; i < edges.size(); i++){
        int from = edges[i].from;
        int to = edges[i].to;
        if(dist[from] < INF && dist[from] + edges[i].weight < dist[to])
            return true;
    }
    return false;
}

void init(){
    cin >> n >> m >> w;
    edges.clear();

    int from, to, weight;
    for (int i = 0; i < m; i++){
        cin >> from >> to >> weight;
        edges.push_back(Edge(from, to, weight));
        edges.push_back(Edge(to, from, weight));
    }

    for (int i = 0; i < w; i++){
        cin >> from >> to >> weight;
        edges.push_back(Edge(from, to, -weight));
    }

    memset(dist, INF, sizeof(dist));
}

int main(){
    int testcase;
    cin >> testcase;
    for (int i = 0; i < testcase; i++){
        init();
        if(bf(1))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}