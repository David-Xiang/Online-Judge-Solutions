// Openjudge 2188 ACM Computer Factory
// Max FLow Algorithm
// 这道题比较有意思的是，输出可以不按照顺序
// 解法：将每一台机器拆成输入节点和输出节点（限制在此）
//      麻烦的地方是建图，需要判断哪些节点相连
//      最后的输出是需要使用原图的备份来做差，找出所有最大流会使用的边

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <set>

#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 200
#define MAXM 10
#define INF (1 << 30)

using namespace std;
int g[MAXN][MAXN];
int go[MAXN][MAXN]; // backup of g, used to find each edge's flow
bool vis[MAXN];
int layer[MAXN];
int n;
int src, sink;
int p;          // how many parts in a computer
int input[MAXN][MAXM];  // input pattern of each node
int output [MAXN][MAXM];// output pattern of each node
int r[MAXN];    // restrict on each node

bool countlayer(){
    deque<int> q;
    memset(layer, -1, sizeof(layer));

    layer[src] = 0;
    q.push_back(src);

    while (!q.empty()){
        int v = q.front();
        q.pop_front();
        for (int j = 0; j < n; j++){
            if (g[v][j] > 0 && layer[j] == -1){
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
    deque<int> q;
    while(countlayer()){
        q.push_back(src);
        memset(vis, 0, sizeof(vis));
        vis[src] = true;

        while (!q.empty()){
            int nd = q.back();
            if (nd == sink){
                int minc = INF;
                int minc_u;
                for (int i = 1; i < q.size(); i++){
                    int u = q[i-1];
                    int v = q[i];
                    if (g[u][v] > 0){
                        if (g[u][v] < minc){
                            minc = g[u][v];
                            minc_u = u;
                        }   
                    }
                }

                maxflow += minc;
                for (int i = 1; i < q.size(); i++){
                    int u = q[i-1];
                    int v = q[i];
                    g[u][v] -= minc;
                    g[v][u] += minc;
                }

                while (!q.empty()){
                    vis[q.back()] = 0;
                    q.pop_back();
                }
            }else{
                int i = 0;
                for (i = 0; i < n; i++){
                    if (g[nd][i] > 0 && layer[i] == layer[nd] + 1 && !vis[i]){
                        vis[i] = true;
                        q.push_back(i);
                        break;
                    }
                }
                
                if (i >= n){
                    q.pop_back();
                }
            }
        }
    }
    return maxflow;
}

void init(){
    /*
        node:
            input: 0, ..., num-1
            output: n, ..., 2num-1
            src: 2num
            sink: 2num+1
    */
    memset(g, 0, sizeof(g));
    memset(g, 0, sizeof(go));
    memset(input, 0, sizeof(input));
    memset(output, 0, sizeof(output));
    memset(r, 0, sizeof(r));

    // input
    int num;
    cin >> p >> num;
    for (int i = 0; i < num; i++){
        cin >> r[i];
        for (int j = 0; j < p; j++)
            cin >> input[i][j];
        for (int j = 0; j < p; j++)
            cin >> output[i][j];
    }

    // construct the graph
    src = 2 * num;
    sink = 2 * num + 1;
    n = 2 * num + 2;
    
    for (int i = 0; i < num; i++){
        // (input)i --> (output)i
        g[i][i+num] = r[i];
        
        // src --> (input)i
        bool flag = true;
        for (int k = 0; k < p; k++){
            if (input[i][k] == 1){
                flag = false;
                break;
            }
        }
        if (flag)
            g[src][i] = INF;
        
        // (output)i --> sink
        flag = true;
        for (int k = 0; k < p; k++){
            if (output[i][k] != 1){
                flag = false;
                break;
            }
        }
        if (flag)
            g[i+num][sink] = INF;
    }

    // (output)i --> (input)j
    for (int i = 0; i < num; i++){
        for (int j = 0; j < num; j++){
            if (i == j)
                continue;
            bool flag = true;
            for (int k = 0; k < p; k++){
                if (input[j][k] != 2 && input[j][k] != output[i][k]){
                    flag = false;
                    break;
                }
            }
            if (flag)
                g[i+num][j] = INF;
        }
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++)
            go[i][j] = g[i][j];
    }
}

int main(){
    ioOptimizer;
    init();
    cout << dinic();

    // find which edges are used
    int a[MAXN];
    int b[MAXN];
    int w[MAXN];
    int count = 0;
    int num = n/2 - 1;
    for (int i = 0; i < num; i++){
        for(int j = 0; j < num; j++){
            int s = go[i+num][j] - g[i+num][j];
            if (s > 0){
                a[count] = i;
                b[count] = j;
                w[count] = s;
                ++count;
            }
        }
    }
    cout << " " << count << endl;
    for (int i = 0; i < count; i++)
        cout << a[i]+1 << " " <<  b[i]+1 << " " << w[i] << endl;
    return 0;
}