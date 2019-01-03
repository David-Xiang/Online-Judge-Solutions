// LeetCode 547
// Friends Circles

#include <iostream>
#include <vector>

using namespace std;

class Solution{
int parent[300];
public:
    int findCircleNum(vector<vector<int> >& M){
        int n = M.size();
        
        // init
        for (int i = 0; i < n; i++){
            parent[i] = i;
        }

        // Union Find
        for (int i = 0; i < n; i++){
            for (int j = 0; j < i; j++){
                if (M[i][j] == 1)
                    Union(i, j);
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++){
            if (parent[i] == i)
                ++ans;
        }
        return ans;
    }
    int Find(int a){
        if (parent[a] != a){
            parent[a] = Find(parent[a]);
        }
        return parent[a];
    }
    void Union(int a, int b){
        int pa = Find(a);   // !
        int pb = Find(b);   // !
        if (pa == pb)
            return;
        parent[pb] = pa;
    }
};

int main(){
    int a[4][4] = {
        {1, 0, 0, 1},
        {0, 1, 1, 0},
        {0, 1, 1, 1},
        {1, 0, 1, 1}
    };
    vector<vector<int> > M(4, vector<int>(4));

    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++)
            M[i][j] = a[i][j];
    }

    Solution s;
    cout << s.findCircleNum(M) << endl;
    return 0;
}