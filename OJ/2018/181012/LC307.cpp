#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

class NumArray{
    // binary indexed tree
private:
    vector<int> c; // index array
    vector<int> a; // original arry
    int length;
public:
    NumArray(vector<int> nums):
        c(nums.size()),a(nums.size()), length(nums.size()){
            for (int i = 0; i < length; i++){
                a[i] = nums[i];
            }
            for (int i = 1; i < length; i++){
                for(int j = i - lowbit(i) + 1; j <= i; j++){
                    c[i] += a[j];
                }
            }
    }
    void update(int i, int val){
        int delta = val - a[i];
        a[i] = val;
        if(i == 0)
            return;
    
        int j = i;
        while(j < length){
            c[j] += delta;
            j = j + lowbit(j);
        }
    }
    int sumRange(int i, int j){
        return sum(j) - sum(i-1);
    }
    int sum(int i){
        if (i < 0)
            return 0;
        
        // get a[0] + ... + a[i]
        int n = i;
        int sum = a[0];
        while (n != lowbit(n)){
            // n == 2^k => end loop
            sum += c[n];
            n = n - lowbit(n);
        }
        return sum+c[n];
    }
    int lowbit(int x){
        return x & (-x);
    }
    // NumArray will be instantiated and called as such
    // NumArray obj = new NumArray(nums);
    // obj.update(i, val);
    // int param_2 = obj.sumRange(i, j);
};

int main(){
    int a1[3] = {1, 3, 5};
    vector<int> nums1(a1, a1 + 3);
    NumArray arr1(nums1);
    cout << arr1.sumRange(0, 2) << endl;
    arr1.update(1, 2);
    cout << arr1.sumRange(0, 2) << endl;
    
    int a2[1] = {-1};
    vector<int> nums2(a2, a2+1);
    NumArray arr2(nums2);
    cout << arr2.sumRange(0, 0) << endl;
    arr2.update(0, 1);
    cout << arr2.sumRange(0, 0) << endl;
    
    int a3[5] = {0, 9, 5, 7, 3};
    vector<int> nums3(a3, a3+5);
    NumArray arr3(nums3);
    cout << arr3.sum(3) << endl;
    return 0;
}
