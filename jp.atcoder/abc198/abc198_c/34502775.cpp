#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long r, x, y;
  cin >> r >> x >> y;
  long d = x * x + y * y;
  r *= r;
  if (d < r) {
    cout << 2 << endl;
    return 0;
  }
  long t = d / r;
  t = sqrtl(t);
  while(t * t * r < d) t++;
  cout << t << endl;
}
