// Openjudge 1492
// A Bug's Life
// union-find algo

#include <iostream>
#include <cstdio>
#define MAX 2000
using namespace std;
int parent[MAX+10];
bool relation[MAX+10]; // relation to root: 0 is same, 1 not same
bool suspicious = false;
int Find(int a){
    if (parent[a] != a){
        int pa = parent[a];
        parent[a] = Find(parent[a]);
        relation[a] = relation[a] ^ relation[pa];
    }
    return parent[a];
}
void Union(int a, int b){
    int pa = Find(a);
    int pb = Find(b);
    
    if (pa != pb){
        parent[pb] = pa;
        relation[pb] = !(relation[b] ^ relation[a]);
    }else if(relation[a] == relation[b]){ // pa == pb
        suspicious = true;
    }
}
int main(){
    int testcase = 0;
    int num = 0;
    int interaction = 0;
    int a, b;
    scanf("%d", &testcase);
    for(int i = 0; i < testcase; i++){
        scanf("%d %d", &num, &interaction);
        suspicious = false;
        for (int j = 1; j < num + 1; j++){
            parent[j] = j;
            relation[j] = 0;
        }
        printf("Scenario #%d:\n", i + 1);
        for (int j = 0; j < interaction; j++){
            scanf("%d%d", &a, &b);
            Union(a, b);
        }
        if (suspicious == true){
            printf("Suspicious bugs found!\n\n");
        }else{
            printf("No suspicious bugs found!\n\n");
        }
    }
    return 0;
}
