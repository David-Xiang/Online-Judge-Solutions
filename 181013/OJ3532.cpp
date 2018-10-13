#include <iostream>
#include <cstdio>
#include <vector>
#define MAXN 100010
using namespace std;
int in[MAXN] = {}; // "in index" of node i
int out[MAXN] = {}; // "out index" of node i
int a[2*MAXN+1] = {};
int c[2*MAXN+1] = {};
int n;
int length = 0;


struct EdgeNode{
    EdgeNode* next;
    int index;
};
vector<EdgeNode*> adjlist;

int lowbit(int x){
    return x & (-x);
}
void init(){
    // construct c[]
    for (int i = 1; i <= length; i++){
        a[i] = 1;
    }
    for (int i = 1; i <= length; i++){
        for (int j = i - lowbit(i) + 1; j <= i; j++){
            c[i] += a[j];
        }
    }
}

void update(int i, int val){
    int delta = val - a[i];
    a[i] = val;
    
    int j = i;
    while (j <= length){
        c[j] += delta;
        j = j + lowbit(j);
    }
}

int sum(int i){
    if (i == 0)
        return 0;
    
    int s = 0;
    int j = i;
    while(j != lowbit(j)){
        s += c[j];
        j = j - lowbit(j);
    }
    return s + c[j];
}

int sumRange(int i, int j){
    return sum(j) - sum(i - 1);
}

void dfs(int index){
    static int curr = 1;
    in[index] = curr++;
    EdgeNode* tmp = adjlist[index];
    while (tmp->next != NULL){
        tmp = tmp->next;
        dfs(tmp->index);
    }
    out[index] = curr++;
}

int main(){
    scanf("%d", &n);
    length = 2 * n;
    
    // initialize header pointers
    adjlist.resize(n+1);
    for (int i = 0; i <= n; i++){
        adjlist[i] = new EdgeNode();
    }
    
    int u, v;
    for (int i = 0; i < n - 1; i++){
        scanf("%d%d", &u, &v);
        EdgeNode* tmp = new EdgeNode();
        tmp->next = adjlist[u]->next;
        tmp->index = v;
        adjlist[u]->next = tmp;
    }
    
    // construct in/out
    dfs(1);
    
    // construct indexed array
    init();
    
    int testcase = 0;
    scanf("%d", &testcase);
    getchar();
    char c;
    int q;
    while(testcase--){
        scanf("%c %d", &c, &q);
        getchar();
        // when scanf is reading numbers,
        // it ignores space, tab and enter.
        // however when it's reading char,
        // we have to use getchar() to skip '\n'.
        if(c == 'Q'){
            cout << sumRange(in[q], out[q]) / 2 << endl;
        }else if(c == 'C'){
            if (a[in[q]] == 1){
                update(in[q], 0);
                update(out[q], 0);
            }else{
                update(in[q], 1);
                update(out[q], 1);
            }
        }
    }
    return 0;
}
