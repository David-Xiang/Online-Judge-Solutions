// Openjudge 41
// Pipe
// Computational Geometry
// 第155行之前都是几何的模版，之后为本题解法：
// 枚举所有转角下沿和上沿组成的直线，首先检查能否能和转角0线段相交
// 若能相交则，从1开始遍历每个转角，如不能通过i则，则可能与i-1~i
// 的上沿、下沿相交，求出交点即可

#include <iostream>
#include <cstdio>
#include <cmath>
#include <utility>
#include <vector>
#define ioOptimizer ios_base::sync_with_stdio(0); cin.tie(0)

using namespace std;
double PI = acos(-1);
double INF = 1e20;
double EPS = 1e-6; //精度不是越高越好
bool IsZero(double x) {
  return -EPS < x && x < EPS;
}
bool FLarger(double a, double b) {
	return a - b > EPS;
}
bool FLessEq(double a, double b)
{
	return b - a > EPS || IsZero(b-a);
}



class CVector {
public:
  double x, y;
  CVector(double xx, double yy){
      x = xx;
      y = yy;
  }
  CVector(){
      x = 0;
      y = 0;
  }
};
CVector operator +(CVector p, CVector q) {
  return CVector(p.x + q.x, p.y + q.y);
}
CVector operator -(CVector p, CVector q) {
  return CVector(p.x - q.x, p.y - q.y);
}
CVector operator *(double k, CVector p) {
  return CVector(k * p.x, k * p.y);
}
double operator *(CVector p, CVector q) {
  return p.x * q.x + p.y * q.y;
}
double operator ==(CVector p, CVector q){
    return IsZero(p.x-q.x) && IsZero(p.y-q.y);
}

#define Point CVector
double Cross(const CVector & v1, const CVector & v2)
{ 	//叉积
	return v1.x * v2.y - v1.y * v2.x;
}
double Area(CVector p, CVector q) {
  return Cross(p, q) / 2;  
}
struct Seg //线段 
{
	Point a, b; //向量是 a->b ,即 b-a 
	Seg(const Point & aa, const Point & bb):
			a(aa), b(bb) 	{ }
	//直线两点式方程 (y-y1)/(y2-y1) = (x-x1)/(x2-x1)	
	double getX(double y) { //给定y坐标，求直线上的 x坐标 
 	   return (y - a.y)/(b.y - a.y)*(b.x - a.x) + a.x;
	}
	double getY(double x) {  //给定x坐标，求直线上的y坐标 
	  return (x - a.x)/(b.x - a.x)*(b.y - a.y) + a.y;
	}
};
double length(CVector p) {
  return sqrt(p * p);
} //求矢量的模

double Distance(Point p, Seg l) {
  return fabs(Cross(p - l.a, l.b - l.a))
         / length(l.b - l.a);
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


/*---------------------------------------以上均为模版-----------------------------------------------------*/
vector<Point> segs;        // 转角处的上坐标


bool checkfirst(const vector<Point>& segs, int upper, int lower){
    // 检查能否通过第一个转角

    // 第一个转角
    Seg s(Point(segs[upper].x, segs[upper].y), Point(segs[lower].x, segs[lower].y-1));
    
    pair<int, Point> cross = CrossPoint(Seg(Point(segs[0].x, segs[0].y), Point(segs[0].x, segs[0].y-1)), s);
    if (cross.first == 0 || cross.first == 1 || cross.first == 3 || cross.first == 8){
        return true;
    }
    return false;
}

bool checkrest(const vector<Point>& segs, int upper, int lower, double* maxdis){
    Seg s(Point(segs[upper].x, segs[upper].y), Point(segs[lower].x, segs[lower].y-1));

    // 检查其余转角
    for (int i = 1; i < segs.size(); i++){
        pair<int, Point> cross = CrossPoint(Seg(Point(segs[i].x, segs[i].y), Point(segs[i].x, segs[i].y-1)), s);
        if (cross.first == 0 || cross.first == 1 || cross.first == 3 || cross.first == 8 || cross.first == 2)
            continue;
        else if(cross.first == 4 || cross.first == 9){
            double maxx = 0;
            if(FLarger(cross.second.y, segs[i].y)){
                // 与i-1~i上管壁相交
                Seg tmp(Point(segs[i-1].x ,segs[i-1].y), Point(segs[i].x, segs[i].y));
                maxx = CrossPoint(tmp, s).second.x;
            }else{
                Seg tmp(Point(segs[i-1].x ,segs[i-1].y-1), Point(segs[i].x, segs[i].y-1));
                maxx = CrossPoint(tmp, s).second.x;
            }

            if (maxx > *maxdis) // 更新光线能通过的最大距离
                *maxdis = maxx;
            return false;
        }
    }
    return true;
}
bool solve(){
    int n;
    cin >> n;
    if (n == 0)
        return false;
    
    segs.clear();
    segs.resize(n);
    
    for (int i = 0; i < n; i++){
        cin >>segs[i].x >> segs[i].y;
    }

    double dis = -INF;              // 坑点！x坐标的初始值要设置为-INF

    for (int i = 0; i < n; i++){    // enum upper point
        for (int j = 0; j < n; j++){ // enum lower point
            if (i == j)
                continue;
            
            if (checkfirst(segs, i, j)){
                if (checkrest(segs, i, j, &dis)){   // modify maxdis
                    cout << "Through all the pipe." << endl;
                    return true;
                }
            }
        }
    }

    printf("%.2f\n", dis);

    return true;;
}
int main(){
    while(solve()){}
    return 0;
}