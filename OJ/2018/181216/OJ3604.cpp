// Openjudge 3604 Computer Virus on Planet Pandora
// AC automaton algorithm
// reverse串也算感染病毒，这样就需要str和reverse(str)都在trie上走一遍
// 错误做法：用pattern和reverse(pattern)建图
// 另外，需要正确计数有多少匹配的模式串，详见searchDFA
// 难点有三个！！
// 1. 不能因为要找出哪些匹配模式串，因此danger只记录终止节点
// 2. 回溯路径需要剪枝，回溯到covered的节点就不需要继续回溯了
// 3. string = string + char => 最后需要加一个'\0'，很好奇C++库为什么这么奇怪。。。

#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <queue>
#include <algorithm>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 250020
#define MAXM 250 // num of virus
#define MAXLEN 1024
#define LETTER 26

using namespace std;

struct Node{
    Node* next[LETTER];
    Node* prev;
    bool danger;
    bool covered;
};

Node tree[MAXN];
char str[MAXLEN];
char query[MAXLEN];
int ans;
int nodecount;

void insert(Node* root, char* s){
    Node* now = root;
    int i = 0;
    for (i = 0; s[i]; i++){
        int index = s[i] - 'A';
        if (now->next[index] == NULL){
            now->next[index] = tree + nodecount;
            nodecount++;
        }
        now = now->next[index];
    }
    now->danger = true;
}

void buildDFA(){
    for (int i = 0; i < LETTER; i++)
        tree[0].next[i] = tree + 1;
    tree[0].prev = NULL;
    tree[1].prev = tree;    
    
    deque<Node*> q;
    q.push_back(tree + 1);
    while (!q.empty()){
        Node* now = q.front();
        q.pop_front();
        for (int i = 0; i < LETTER; i++){
            Node* child = now->next[i];
            if (child){
                Node* prev = now->prev;
                while (prev->next[i] == NULL)
                    prev = prev->prev;
                child->prev = prev->next[i];
                q.push_back(child);
            }
        }
    }
}

void searchDFA(string s){
    Node* now = tree + 1;
    for (int i = 0; s[i]; i++){
        int index = s[i] - 'A';
        while(now->next[index] == NULL)
            now = now->prev;
        now = now->next[index];
        
        Node* p = now;
        while(p && !p->covered){            // !!!
            if (p->danger)
                ans += 1;
            p->covered = true;
            p = p->prev;
        }
    }
}

void init(){
     memset(tree, 0, sizeof(tree));
    memset(str, 0, sizeof(str));
    nodecount = 2;
    ans = 0;
    
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        scanf("%s", str);
        insert(tree + 1, str);
    }
    buildDFA();
    getchar();
    
    string query;
    char c;
    c = getchar();
    while(c != '\n'){
        int count = 1;
        
        if (c == '['){
            scanf("%d", &count);
            c = getchar();
            getchar();
        } // or count = 1, c is the original char
        
        for (int i = 0; i < count; i++)
            query += c;
        c = getchar();
    }
    
    query += '\0';                  // ???
    searchDFA(query);
    
    int len = query.size() - 1;     // ???
    reverse(&query[0], &query[len]);
    searchDFA(query);
    printf("%d\n", ans);
}

int main(){
    int testcase;
    scanf("%d", &testcase);
    while(testcase--){
        init();
    }
    return 0;
}
