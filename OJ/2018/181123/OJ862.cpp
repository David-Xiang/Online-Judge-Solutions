// Openjudge 862 Exchange Point
// Bellman-Ford
// 求正环，需要一定的转换
// 货币是图上的节点，兑换方式是图上的环
#include <iostream>
#include <cstring>
#include <vector>

#define MAXN 205
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
using namespace std;

struct EP{      // short for exchange point
    int from;
    int to;
    double fee;
    double rate;
    EP(int from, int to, double fee, double rate){
        this->from = from;
        this->to = to;
        this->fee = fee;
        this->rate = rate;
    }
};
vector<EP> g;
double dist[MAXN];

int n, e;
int src;    // curr currency
double m;   // amount of curr currency

void init(){
    for (int i = 0; i < e; i++){
        int f, t;
        double c, r;
        cin >> f >> t >> r >> c;
        g.push_back(EP(f, t, c, r));
        cin >> r >> c;
        g.push_back(EP(t, f, c, r));
    }

    memset(dist, 0, sizeof(dist));          // init all other currency with min dist 0
    dist[src] = m;                          // src currency's dist is m

}

bool bf(){
    bool flag;
    for (int i = 0; i < n-1; i++){
        flag = false;
        for (int j = 0; j < g.size(); j++){
            if (dist[g[j].to] < (dist[g[j].from] - g[j].fee) * g[j].rate){
                flag = true;    // prevent early stopping
                dist[g[j].to] = (dist[g[j].from] - g[j].fee) * g[j].rate;
            }
        }
        if (!flag)
                break;          // early stop
    }
    // BF判断负权环的思想：
    // 循环了n-1次之后，如没有负权环（这里是正权环），则无论再做多少次迭代，距离都不会继续减少

    // search for positive circle
    for (int i = 0; i < g.size(); i++){
        if (dist[g[i].to] < (dist[g[i].from] - g[i].fee) * g[i].rate)
            return true;
    }
    return false;
}

int main(){
    while(cin >> n >> e >> src >> m){
        init();
        if (bf())
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}