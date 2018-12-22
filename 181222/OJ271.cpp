// Openjudge 271 Intersecting Lines
// Computational Geometry

#include <iostream>
#include <cstdio>
#include <cmath>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)
#define Vector Point
#define MAXN 10
#define EPS 1e-6
using namespace std;

struct Point{
    double x;
    double y;
    Point(){
        x = 0;
        y = 0;
    }
    Point(double x, double y){
        this->x = x;
        this->y = y;
    }
    Vector operator - (Point b){
        return Vector(x - b.x, y - b.y);
    }
    
    Vector operator + (Point b){
        return Vector(x + b.x, y + b.y);
    }
    
    Vector operator * (double a){
        return Vector(a * x, a * y);
    }
    
    double operator * (Point b){
        return x * b.x + y * b.y;
    }
    
    double operator ^ (Point b){
        return x * b.y - y * b.x;
    }
};

struct Line{
    Point a;
    Point b;
};

bool isZero(double x){
    return x < EPS && x > -EPS;
}

double length(Point l){
    return sqrt(l.x * l.x + l.y * l.y);
}

double area(Vector a, Vector b){
    return a ^ b;
}

double dist(Point a, Point b){
    return length(a - b);
}

double dist(Point a, Line l){
    return abs(area(a - l.a, l.b - l.a)) / length(l.b - l.a);
}

void intersect(Line l1, Line l2){
    double s1 = area(l1.a - l2.a, l2.b - l2.a);
    double s2 = area(l2.a - l1.b, l2.b - l2.a);
    
    int ans;    // 1: coincide, 2: parallel, 3:
    double x, y;
    
    if (isZero(s1 + s2)){
        if (isZero(dist(l1.a, l2))){ // coincide
            ans = 1;
        }else{
            ans = 2;
        }
    }else{
        ans = 3;
        Point intersect = l1.a + (l1.b - l1.a) * (s1 / (s1 + s2));
        x = intersect.x;
        y = intersect.y;
    }
    
    switch(ans){
        case 1:
            printf("LINE\n");
            break;
        case 2:
            printf("NONE\n");
            break;
        case 3:
            printf("POINT %.2lf %.2lf\n", x, y);
    }
}

int main(){
    ioOptimizer;
    Line l1, l2;
    int testcase;
    cin >> testcase;
    printf("INTERSECTING LINES OUTPUT\n");
    while(testcase--){
        cin >> l1.a.x >> l1.a.y >> l1.b.x >> l1.b.y >> l2.a.x >> l2.a.y >> l2.b.x >> l2.b.y;
        intersect(l1, l2);
    }
    printf("END OF OUTPUT\n");
}
