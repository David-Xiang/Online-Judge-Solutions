// AC automaton algorithm
// Multi pattern matching using trie
#include <iostream>
#include <memory>
#include <stack>
#include <queue>

#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define MAXN 1000           // num of nodes (sum of chars of all patterns)
#define LETTER 26
using namespace std;

struct Node{
    Node* next[LETTER];    // next pointer to all chilren (not NULL when valid)
    Node* prev;            // prev pointer
    bool bad;              // whether this node can be an end of pattern string
};

Node tree[MAXN];            // 所有的插入和搜索操都从root开始，*需要注意的是*， tree[1]才是root！
int nodecount;

void insert(Node* root, char* p){
    // insert pattern p into trie
    for (int i = 0; p[i]; i++){
        int index = p[i]-'a';
        if (root->next[index] == NULL){    // 易错之处：(char-'a')才是index
            root->next[index] = tree + nodecount;
            nodecount++;
        }
        root = root->next[index];
    }
    root->bad = true;       // mark the end of a pattern
}

void buildDFA(){
    for (int i = 0; i < LETTER; i++)
        tree[0].next[i] = tree + 1;   // all next of tree[0] points to root
    tree[0].prev = NULL;
    tree[1].prev = tree;    // root's prev pointer points to tree[0]
    
    // add prev pointer using BFS
    deque<Node*> q;
    q.push_back(tree+1);    // push back root
    while (!q.empty()){
        Node* root = q.front();
        q.pop_front();
        for (int i = 0; i < LETTER; i++){
            Node* child = root->next[i];
            if (child){      // p is not NULL, must find its prev pointer
                Node* prev = root->prev;
                while(prev->next[i] == NULL)
                    prev = prev->prev;
                child->prev = prev->next[i];
                if (child->prev->bad)
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
        while(p->next[index] == NULL)
            p = p->prev;
        p = p->next[index];
        if (p->bad)
            return true;
    }
    return false;
}

void init(){
    nodecount = 2;
    memset(tree, 0, sizeof(tree));
    Node* root = tree + 1;
    insert(root, "abc");
    insert(root, "def");
    insert(root, "gh");
    buildDFA();
}

int main(){
    ioOptimizer;
    init();
    if (searchDFA("abcddddddddddd"))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    if(searchDFA("akgggggg"))
        cout << "YES" << endl;
    else   
        cout << "NO" << endl;
    return 0;
}