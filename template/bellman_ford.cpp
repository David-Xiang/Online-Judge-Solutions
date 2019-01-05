// Bellman-Ford Algo for detecting negative weight cycle
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#define INF (1 << 30)
#define MAXN 10
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
int n;
/*
    Another way to present a graph:
    typedef vector<int> Edge;
    vector<Edge> edges;
    edges[from].push_back(to);
*/

bool bf(int u){     // source is u
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
    edges.clear();
    memset(dist, INF, sizeof(dist));
    n = 3;
    edges.push_back(Edge(1, 2, 3));
    edges.push_back(Edge(2, 1, 3));
    edges.push_back(Edge(2, 3, 4));
    edges.push_back(Edge(3, 2, 4));
    edges.push_back(Edge(3, 1, -8));
}

int main(){
    init();
    if (bf(1))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}