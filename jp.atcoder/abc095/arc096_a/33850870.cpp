#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long a, b, c, x, y;
  cin >> a >> b >> c >> x >> y;
  long const inf = 1l << 50;
  long mn = inf;
  for(int i = 0; i <= max(x, y); i++) {
    long s = c * 2 * i;
    s += max(x - i, 0l) * a;
    s += max(y - i, 0l) * b;
    mn = min(mn, s);
  }
  cout << mn << endl;
}
