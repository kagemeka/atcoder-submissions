#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long r, x, y;
  cin >> r >> x >> y;
  long d = x * x + y * y;
  r *= r;
  long t = d / r;
  t = sqrtl(t);
  if(t * t * r < d) t++;
  cout << t << endl;
}
