#include <bits/stdc++.h>
using namespace std;

double area(int x1, int y1, int x2, int y2, int x3, int y3) {
  int a, b, c, d;
  a = x2 - x1;
  b = y2 - y1;
  c = x3 - x1;
  d = y3 - y1;
  double s = abs(a*d - b*c) / 2.0;
  return s;
}

int main() {
  int a, b, c, d, e, f;
  cin >> a >> b >> c >> d >> e >> f;
  double s = area(a, b, c, d, e, f);
  cout << setprecision(10) << s << endl;
  return 0;
}
