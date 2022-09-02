#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long x, a, d, n;
  cin >> x >> a >> d >> n;
  long b = a + d * (n - 1);
  if(d < 0) {
    d *= -1;
    swap(a, b);
  }
  if(x < a) {
    cout << a - x;
  } else if(x > b) {
    cout << x - b;
  } else {
    x -= a;
    if(x == 0) {
      cout << 0 << endl;
    } else {
      long lo = x / d;
      long hi = (x + d - 1) / d;
      cout << min(x - lo * d, hi * d - x);
    }
  }
  cout << endl;
}
