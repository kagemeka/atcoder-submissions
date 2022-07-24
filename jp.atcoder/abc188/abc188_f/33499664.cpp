#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long x, y;
  cin >> x >> y;
  long const inf = 1l << 60;
  function<long(long, int)> f;
  f = [&](long y, int t) -> long {
    if(y <= x) { return x - y; }
    long mn = inf;
    if((y & 1) && t != 0) mn = min(mn, f((y + 1) >> 1, 2) + 2);
    if((~y & 1)) mn = min(mn, f(y >> 1, 2) + 1);
    mn = min(mn, f(y - 1, 0) + 1);
    return mn;
  };
  cout << f(y, 2) << endl;
}
