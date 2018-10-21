// opejudge 1184
// lost cows
// brutal force / interval tree

#include <iostream>
#include <algorithm>
#include <vector>
#define ioOptimzier ios_base::sync_with_stdio(0);cin.tie(0)
#define MAXN 10
using namespace std;

bool found[MAXN] = {0};
int pre[MAXN] = {0};
int act[MAXN] = {0};
int n;
int main(){
    scanf("%d", &n);
    pre[0] = 0;
    for (int i = 1; i < n; i++){
        scanf("%d", &pre[i]);
    }
    for (int i = n - 1; i >= 0; i--){
        int curr = 1;
        while (pre[i] > 0){
            if(found[curr++] == 0){
                pre[i]--;
            }
        }
        while(found[curr] != 0){
            curr++;
        }
        found[curr] = 1;
        act[i] = curr;
    }
    for (int i = 0; i < n; i++)
        cout <<act[i] <<endl;
    return 0;
}