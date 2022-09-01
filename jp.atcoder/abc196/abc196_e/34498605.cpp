#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  long const inf = 1l << 60;
  long l = -inf, r = inf;
  long d = 0;
  while(n--) {
    long a, t;
    cin >> a >> t;
    if(t == 1) {
      l += a;
      r += a;
      d += a;
    }
    if(t == 2) {
      l = max(l, a);
      r = max(r, a);
    }
    if(t == 3) {
      l = min(l, a);
      r = min(r, a);
    }
  }
  int q;
  cin >> q;
  while(q--) {
    long x;
    cin >> x;
    cout << max(l, min(x + d, r)) << '\n';
  }
}
