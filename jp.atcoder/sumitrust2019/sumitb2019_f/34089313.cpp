#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long t0, t1, a0, a1, b0, b1;
  cin >> t0 >> t1 >> a0 >> a1 >> b0 >> b1;
  long a = (a0 - b0) * t0;
  long b = (a1 - b1) * t1;
  if(a < 0) {
    a *= -1;
    b *= -1;
  }
  long c = a + b;
  // cout << a << ' ' << b << ' ' << c << endl;
  if(c == 0) {
    cout << "infinity" << endl;
    return 0;
  }
  if(c > 0) {
    cout << 0 << endl;
    return 0;
  }
  c *= -1;
  // a + k * (a + b) <= 0
  // k >= -a/(a + b), (a + b < 0)
  long k = a / c;
  long res = 1 + k * 2 + (k * c == a);
  cout << res << endl;
}
