// Openjudge 230
// Grandpa's Estate
// Graham Algo for Convex Hull Problem
// 本题需要判断凸包的每一条边上至少有一个多余点（非顶点），核心是检查每条边，不能出现"\_/"这种情况
// 但是有两个坑点：
// 1.点过少（仅1个点）会导致段错误
// 2.所有点共线的情况出错，需要特判

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <stack>
#include <vector>
#include <algorithm>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define EPS 1e-6

using namespace std;

double fabs(double x){return x > 0 ? x : -x;}

int Sign(double x) { // 判断 x 是大于0,等于0还是小于0
    return fabs(x)<EPS?0:x>0?1: -1;
}

struct Point {
    double x,y;
    Point(double xx = 0,double yy = 0):x(xx),y(yy) { }
    Point operator-(const Point & p) const {
        return Point(x-p.x,y-p.y);
    }
    bool operator <(const Point & p) const {
        if( y < p.y)
            return true;
        else if( y > p.y)
            return false;
        else
            return x < p.x;
    }
};
typedef Point Vector;

double Cross(const Vector & v1, const Vector & v2)
{//叉积
    return v1.x * v2.y - v2.x * v1.y;
}
double Distance(const Point & p1,const Point & p2)
{
    return sqrt( (p1.x - p2.x)*(p1.x - p2.x) + (p1.y-p2.y)*(p1.y-p2.y));
}


vector<Point> & Graham(vector<Point>  & points, vector<Point> & stack) {
    //在凸包上，但不是顶点的点，没有抛弃，留在stack里面
    if( points.size() < 3)
        return stack;
    stack.clear();
    //先按坐标排序，最左下的放到points[0]
    sort(points.begin(),points.end()); 
    stack.push_back(points[0]);
    stack.push_back(points[1]);
    int n = points.size();
    for(int i = 2; i< n; ++i) { //做右半凸包
        while(stack.size()>1)    {//定要这一条
            Point p2 = * (stack.end()-1);
            Point p1 = * (stack.end()-2);
            if( Sign(Cross(p2-p1,points[i]-p2) < 0)) {
                //p2->points[i]向右转，才让p2出栈 ，这样能保留凸包边上的点
                stack.pop_back();
            }
            else
                break;
        }
        stack.push_back(points[i]);
    }
    int size = stack.size();
    //此时栈顶定是points[n-1]
    stack.push_back(points[n-2]);
    for(int i = n-3; i >= 0;--i) { //做左半凸包
        while(stack.size() > size) {
            Point p2 = * (stack.end()-1);
            Point p1 = * (stack.end()-2);
            if( Sign(Cross(p2-p1,points[i]-p2) < 0))
                stack.pop_back();
            else
                break;
        }
        stack.push_back(points[i]);
    }
    stack.pop_back();
    return stack;
}

void solve(){
    int n;
    cin >> n;
    vector<Point> arr(n);
    for (int i = 0; i < n; i++){
        cin >> arr[i].x >> arr[i].y;
    }

    if (n < 6){
        cout << "NO" << endl;
        return;
    }
    
    vector<Point> stk;
    
    stk = Graham(arr,stk);
    int num = stk.size();
    
    stk.push_back(stk[0]);
    stk.push_back(stk[1]);
    stk.push_back(stk[2]);

    // cout << "stack:" << endl;
    // cout << stk.size() << endl;
    // for (int i = 0; i < stk.size(); i++)
    //     cout << stk[i].x << " " << stk[i].y << endl;
    
    bool line = true;
    for (int i = 1; i < num + 1; i++){
        if (Sign(Cross(stk[i]-stk[i-1], stk[i+1]-stk[i])) == 1 &&
            Sign(Cross(stk[i+1]-stk[i], stk[i+2]-stk[i+1])) == 1){
            cout << "NO" << endl;
            return;
        }
        if (Sign(Cross(stk[i]-stk[i-1], stk[i+1]-stk[i])) != 0)
            line = false;
    }
    if (line == true){
        cout << "NO" << endl;
        return;
    }
    cout << "YES" << endl;
}

int main(){
    int testcase;
    cin >> testcase;
    while(testcase--){
        solve();
    }
    return 0;
}
