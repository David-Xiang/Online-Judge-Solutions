// openjudge 184
// NOI 2001!!!
// Foodchain
// union-find algo

#include <iostream>
#include <cstdio>
#define MAX 50000
using namespace std;
int parent[MAX+10];
int relation[MAX+10]; // 0-same, 1-me eat root, -1-root eat me
bool truth = true;
int AddRelation(int x, int y){
    if (x == 1 && y == 1)
        return -1;
    else if (x == -1 && y == -1)
        return 1;
    else
        return x + y;
}

int SubRelation(int x, int y){
    if (x == 1 && y == -1)
        return -1;
    else if (x == -1 && y == 1)
        return 1;
    else
        return x - y;
}

int Find(int a){
    if (parent[a] != a){
        int pa = parent[a];
        parent[a] = Find(parent[a]);
        relation[a] = AddRelation(relation[a], relation[pa]);
    }
    return parent[a];
}

void Union(int a, int b, int mode){ // // mode: 1-same, 2-a eat b
    int pa = Find(a);
    int pb = Find(b);
    
    if (pa != pb){
        // union
        parent[pb] = pa;
        if (mode == 1){ // a == b
            relation[pb] = SubRelation(relation[a], relation[b]);
        }else{ // a eat b
            int x = SubRelation(relation[a], relation[b]);
            if (x == 0)
                x = -1;
            else if(x == -1)
                x = 1;
            else
                x = 0;
            relation[pb] = x;
        }
    }else{ // pa == pb, only check
        if (mode == 1){ // a == b
            if (relation[a] != relation[b]){
                // wrong
                truth = false;
                return;
            }
        }else{ // a eat b
            if (relation[a] == 0 && relation[b] == -1)
                return;
            if (relation[a] == 1 && relation[b] == 0)
                return;
            if (relation[a] == -1 && relation[b] == 1)
                return;
            truth = false;
            return;
        }
    }
}

int main(){
    int n, k;
    int d, x, y;
    int count = 0;
    scanf("%d%d", &n, &k);
    for (int i = 1; i < n + 1; i++){ // init the arrays
        parent[i] = i;
        relation[i] = 0;
    }
    for (int testcase = 0; testcase < k; testcase++){
        scanf("%d%d%d", &d, &x, &y);
        if (x > n || y > n){
            count ++;
            continue;
        }
        if (x == y && d == 2){
            count ++;
            continue;
        }
        Union(x, y, d);
        if (truth == false)
            count++;
        truth = true;
    }
    printf("%d", count);
    return 0;
}
