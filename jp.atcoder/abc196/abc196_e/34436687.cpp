#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  long const inf = 1l << 60;
  long l = -inf, r = inf;
  long d = 0;
  while(n--) {
    long a, t;
    cin >> a >> t;
    if(t == 1) {
      d += a;
      l += a;
      r += a;
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
    long y = min(r, max(l, x + d));
    cout << y << '\n';
  }
}
