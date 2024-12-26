// Openjudge 6088  Most Distant Point from the Sea
// Half Plane & Dichotomy
// 有BUG
// 样例答案为：
// 5000.000000
// 494.233641
// 34.542948
// 0.353553
// 本程序答案为：
// 5000.000000
// 505.671195
// 35.462106
// 0.707097
#include <iostream>
#include <cmath>
#include <vector>
#include <cmath>
#define EPS 1e-9
#define PI acos(-1)
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)

using namespace std;

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
typedef Point CVector;

double Cross(const CVector & v1, const CVector & v2)
{//叉积
    return v1.x * v2.y - v2.x * v1.y;
}
double Distance(const Point & p1,const Point & p2)
{
    return sqrt( (p1.x - p2.x)*(p1.x - p2.x) + (p1.y-p2.y)*(p1.y-p2.y));
}

struct Seg //线段
{
    Point a, b; //向量是 a->b ,即 b-a
    Seg(const Point & aa, const Point & bb):
    a(aa), b(bb)     { }
    //直线两点式方程 (y-y1)/(y2-y1) = (x-x1)/(x2-x1)
    double getX(double y) { //给定y坐标，求直线上的 x坐标
        return (y - a.y)/(b.y - a.y)*(b.x - a.x) + a.x;
    }
    double getY(double x) {  //给定x坐标，求直线上的y坐标
        return (x - a.x)/(b.x - a.x)*(b.y - a.y) + a.y;
    }
};

CVector operator +(CVector p, CVector q) {
    return CVector(p.x + q.x, p.y + q.y);
}


CVector operator *(double k, CVector p) {
    return CVector(k * p.x, k * p.y);
}

double operator *(CVector p, CVector q) {
    return p.x * q.x + p.y * q.y;
}

double operator ^(CVector p, CVector q) {
    return (p.x * q.y)-(q.x * p.y);
}

double Area(CVector p, CVector q) {
    return (p ^ q) / 2;
}

bool IsZero(double x) {
    return -EPS < x && x < EPS;
}

bool operator ==(CVector p, CVector q){
    return IsZero(p.x-q.x) && IsZero(p.y-q.y);
}

bool FLessEq(double a, double b)
{
    return b - a > EPS || IsZero(b-a);
}

bool PointInSeg(Point p, Seg L)
{
    double tmp = Cross(L.a - p, L.a - L.b);
    if (!IsZero(tmp))
        return false;
    if ( FLessEq(min(L.a.x, L.b.x),p.x) &&
        FLessEq(p.x ,max(L.a.x, L.b.x)) &&
        FLessEq(min(L.a.y, L.b.y), p.y) &&
        FLessEq(p.y , max(L.a.y, L.b.y)))
        return true;
    return false;
}

double length(CVector p) {
    return sqrt(p * p);
} //求矢量的模


double Distance(Point p, Seg l) {
    return fabs((p-l.a) ^ (l.b-l.a)) / length(l.b-l.a);
}


pair<int, Point> CrossPoint(Seg s1, Seg s2)  {
    Point p1 = s1.a;
    Point p2 = s1.b;
    Point p3 = s2.a;
    Point p4 = s2.b;
    
    double a1 = Area(p3 - p1, p4 - p1);
    double a2 = Area(p4 - p2, p3 - p2);//这些顺序不能乱
    if (Cross(p2 - p1, p3 - p1)*
        Cross(p2 - p1, p4 - p1) < -EPS &&
        Cross(p4 - p3, p1 - p3)*
        Cross(p4 - p3, p2 - p3) < -EPS) {// 规范相交
        return
        make_pair(0,p1+(a1/(a1 + a2))*(p2 - p1));
    }
    if (!(IsZero(Cross(p2 - p1, p3 - p4)))) {
        //不平行,不共线
        if (p1 == p3 || p1 == p4)
            //端点重合且不平行，不共线
            return make_pair(1, p1);
        if (p2 == p3 || p2 == p4)
            return make_pair(1, p2);
        if (PointInSeg(p1, s2))
            return make_pair(2, p1);
        if (PointInSeg(p2, s2))
            return make_pair(2, p2);
        if (PointInSeg(p3, s1))
            return make_pair(3, p3);
        if (PointInSeg(p4, s1))
            return make_pair(3, p4);
        Point crossPoint =
        p1+(a1/(a1+ a2))*(p2 - p1);
        if (PointInSeg(crossPoint, s1))
            return make_pair(8, crossPoint);
        if (PointInSeg(crossPoint, s2))
            return make_pair(9, crossPoint);
        return make_pair(4, crossPoint);
        // 直线和线段也无交点，不平行，不共线，两直线交点是second
        
    }
    if (!IsZero(Distance(p1, s2)))
        return make_pair(5, Point(0, 0)); //平行
    //下面都是共线，且有公共点
    if (PointInSeg(p1, s2))
        return make_pair(6, p1);
    if (PointInSeg(p2, s2))
        return make_pair(6, p2);
    if (PointInSeg(p3, s1))
        return make_pair(6, p3);
    if (PointInSeg(p4, s1))
        return make_pair(6, p4);
    return make_pair(7, Point(0, 0));//共线，且无公共点
}

Point rotate(Point b, Point a,
              double alpha) {//返回点C坐标
    CVector p = b-a;
    return Point(a.x + (p.x * cos(alpha)
                         - p.y * sin(alpha)),
                  a.y + (p.x * sin(alpha)
                         + p.y * cos(alpha)));
}
                  

typedef  vector<Point> Polygon;
int CutPolygon(const Polygon & src, Point a, Point b, Polygon & result)
{ //用直线a->b 切割src,返回其左侧的多边形，放到result
    //src里的点什么顺序无所谓
    int n = src.size();
    result.clear();
    for (int i = 0; i < n; ++i) {
        Point c = src[i];
        Point d = src[(i + 1) % n];
        if (Sign(Cross(b - a, c - a)) >= 0) //叉积>=0
            result.push_back(c);
        pair<int, Point> r = CrossPoint(Seg(c, d),
                                        Seg(a, b));
        //c,d在 a->b上，或者 c->d重合于 a->b这两种情况都不要考虑，因为会在上面两行处理了
        
        if (r.first == 0 || r.first == 8 || r.first == 3)  //规范相交或虽非规范相交但是交点在c->d上
            result.push_back(r.second);
    }
    return result.size();
}

void Translation(const Point& a, const Point& b, double dis, Point & from, Point & to){
    Point p = a + (b - a) * dis / length(b - a);
    Point q = b + (a - b) * dis / length(b - a);
    from = rotate(p, a, PI/2);
    to = rotate(q, b, 3*PI/2);
}

bool check(double d, Polygon p){
    int n = p.size();
    Polygon p1, p2;
    int retval;
    for (int i = 0; i < n; i++){
        Point from;
        Point to;
        Translation(p[i], p[(i+1)%n], d, from, to);
        
        if (i == 0){
            retval = CutPolygon(p, from, to, p1);
        }else if(i % 2 == 0){
            retval = CutPolygon(p2, from, to, p1);
        }else{
            retval = CutPolygon(p1, from, to, p2);
        }
        if (retval <= 1)
            return false;
    }
    return true;
}

bool solve(){
    int n;
    cin >> n;
    if (n == 0)
        return false;
    Polygon p(n);
    for (int i = 0; i < n; i++){
        cin >> p[i].x >> p[i].y;
    }
    
    double lb=0, ub=1e4;
    while(!IsZero(ub-lb)){
        double mid = (ub + lb) / 2;
        if (check(mid, p)){
            lb = mid;
        }else{
            ub = mid;
        }
    }
    printf("%.6f\n", lb);
    return true;
}

int main(){
    while(solve()){
    }
    return 0;
}
