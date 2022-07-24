#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long x, y;
  cin >> x >> y;
  long const inf = 1l << 60;
  function<long(long)> f;
  map<long, long> cache;
  f = [&](long y) -> long {
    if(cache.count(y)) return cache[y];
    if(y <= x) { return x - y; }
    long mn = inf;
    if(y == 1) { return abs(x - 1); }
    if(y & 1) {
      mn = min(f(y + 1), f(y - 1)) + 1;
    } else {
      mn = min(abs(x - y), f(y >> 1) + 1);
    }
    cache[y] = mn;
    return mn;
  };
  cout << f(y) << endl;
}
