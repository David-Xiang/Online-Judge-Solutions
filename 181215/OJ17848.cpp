// Openjudge 17848
// template of AC automaton
// 垃圾题目，数据范围有问题！

#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 30000
#define LETTER 26

using namespace std;

struct Node{
    Node* child[LETTER];
    Node* prev;
    bool bad;
    Node(){
        memset(child, 0, sizeof(child));
        prev = NULL;
        bad = false;
    }
};

Node tree[MAXN];
int nodecount = 2;

void insert(Node* root, char* s){
    int l = strlen(s);
    for (int i = 0; s[i]; i++){
        int index = s[i] - 'a';
        if (root->child[index] == NULL){
            root->child[index] = tree + nodecount;
            nodecount++;
        }
        root = root->child[index];
        if (i == l-1)
            root->bad = true;
    }
}

void buildDFA(){
    for (int i = 0; i < LETTER; i++){
        tree[0].child[i] = tree + 1;
    }
    tree[0].prev = NULL;
    tree[1].prev = tree;

    deque<Node*> q;
    q.push_back(tree + 1);
    while (!q.empty()){
        Node * root = q.front();
        q.pop_front();
        for (int i = 0; i < LETTER; i++){
            Node* child = root->child[i];
            if (child != NULL){
                Node* prev = root->prev;
                while(prev->child[i] == NULL)
                    prev = prev->prev;
                child->prev = prev->child[i];
                if (child->prev->bad)           //这句话容易出错
                    child->bad = true;
                q.push_back(child);
            }
        }
    }
}

bool searchDFA(char* s){
    Node* p = tree + 1;
    for (int i = 0; s[i]; i++){
        int index = s[i] - 'a';
        while(p->child[index] == NULL)
            p = p->prev;
        p = p->child[index];
        if (p->bad)
            return true;
    }
    return false;
}

void init(){
    int n;
    scanf("%d", &n);

    char s[3000];
    for (int i = 0; i < n; i++){
        scanf("%s", s);
        insert(tree + 1, s);
    }
    buildDFA();
}

int main(){
    ioOptimizer;
    init();
    int m;
    scanf("%d", &m);
    for (int i = 0; i < m; i++){
        char query[1020];
        scanf("%s", query);
        if (searchDFA(query))
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}