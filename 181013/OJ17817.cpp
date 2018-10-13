// OpenJudge 17817
// Hard LIS
// Binary Indexed Array
#include <iostream>
#include <algorithm>
#include <vector>
#define ioOptimzier ios_base::sync_with_stdio(0);cin.tie(0)
#define MAXN 300010
using namespace std;
int arr[MAXN] = {};

class Elem{
public:
    int num;
    int pos;
    bool operator < (const Elem& e)const{
        return num < e.num;
    }

};
vector<Elem> elem(MAXN);
int BIT[MAXN] = {};

int lowbit(int x) { return x & (-x); }

int LIS(int pos){
    int maxlen = 0;
    for (; pos; pos -= lowbit(pos)){
        if (maxlen < BIT[pos])
            maxlen = BIT[pos];
    }
    return maxlen + 1;
}

int update(int pos, int len, int maxval){
    for (; pos <= len; pos += lowbit(pos)){
        if (BIT[pos] < maxval)
            BIT[pos] = maxval;
    }
}

int main(){
    ioOptimzier;
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++){
        cin >> arr[i];
        elem[n-i+1].num = arr[i];
        elem[n-i+1].pos = i;
        // statisfy constraint:
        // elems with equal value will be sort in reverse order
    }

    stable_sort(elem.begin(), elem.begin()+n+1);
    // elem[0] = 0

    int max = 0;
    for (int i = 1; i <= n; i++){
        int tmp = LIS(elem[i].pos);
        max = max < tmp ? tmp : max;
        update(elem[i].pos, n, tmp);
    }

    cout << max << endl;

    return 0;
}
