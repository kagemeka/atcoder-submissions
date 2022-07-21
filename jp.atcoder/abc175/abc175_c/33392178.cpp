#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long x, k, d;
  cin >> x >> k >> d;
  x = abs(x);
  long t = x / d;
  if(t >= k) {
    x -= k * d;
  } else {
    k -= t;
    x -= t * d;
    if(k & 1) x = d - x;
  }
  cout << x << endl;
}
