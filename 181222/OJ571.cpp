// Openjudge 571 Myacm Triangles
// Computational Geometry

#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define Vector Point
#define EPS 1e-6
#define MAXN 20
using namespace std;

struct Point{
    char c;
    double x;
    double y;
    Point(){
        c = 0;
        x = 0;
        y = 0;
    }
    Point(char c, double x, double y){
        this->c = c;
        this->x = x;
        this->y = y;
    }
    Point(double x, double y){
        this->x = x;
        this->y = y;
    }
    Vector operator - (Point b){
        return Point(x - b.x, y - b.y);
    }
    Vector operator + (Point b){
        return Point(x + b.x, y + b.y);
    }
    double operator ^ (Point b){
        return x * b.y - y * b.x;
    }
};
struct Line{
    Point a;
    Point b;
    Line(Point a, Point b){
        this->a = a;
        this->b = b;
    }
};

Point p[MAXN];

bool isZero(double x){
    return x < EPS && x > -EPS;
}

double area(Vector a, Vector b){
    return a ^ b;
}

void init(){
    memset(p, 0, sizeof(p));
}

bool checkSide(Line l, Point m, Point n){
    double s1 = area(m-l.a, l.b-l.a);
    double s2 = area(n-l.a, l.b-l.a);
    if (s1 * s2 > 0 || isZero(s1 * s2)){
        // 边界问题？
        return true;
    }
    return false;
}

void print3(char a, char b, char c){
    char t;
    if (b < a){
        t = b;
        b = a;
        a = t;
    }
    if (c < a){
        t = c;
        c = a;
        a = t;
    }
    if (c < b){
        t = c;
        c = b;
        b = t;
    }
    cout << a << b << c << endl;
}

void solve(int n){
    // select all triangles and check it's area and whether no point inside
    double maxarea = 0;
    int maxi, maxj, maxk;
    for (int i = 0; i < n - 2; i++){
        for (int j = i + 1; j < n - 1; j++){
            for (int k = j + 1; k < n; k++){
                if (abs(area(p[j]-p[i], p[k]-p[i])/2) < maxarea)
                    continue;
                // found a large triangle
                bool in = false;    // now no point inside
                for (int s = 0; s < n && !in; s++){
                    if (s == i || s == j || s == k)
                        continue;
                    // 每次选定一条边，如果始终和剩下的点在边的同侧，则说明在三角形内部
                    if (checkSide(Line(p[i], p[j]), p[k], p[s]) &&
                        checkSide(Line(p[i], p[k]), p[j], p[s]) &&
                        checkSide(Line(p[k], p[j]), p[i], p[s]))
                        in = true;
                }
                if (!in){
                    // this triangle in valid
                    maxarea = abs(area(p[j]-p[i], p[k]-p[i])/2);
                    maxi = i;
                    maxj = j;
                    maxk = k;
                }
            }
        }
    }
    print3(p[maxi].c, p[maxj].c, p[maxk].c);
}

int main(){
    init();
    int n;
    cin >> n;
    while(n){
        for (int i = 0; i < n; i++){
            cin >> p[i].c >> p[i].x >> p[i].y;
        }
        solve(n);
        cin >> n;
    }
    return 0;
}
