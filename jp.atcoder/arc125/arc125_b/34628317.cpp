#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n;
  cin >> n;
  long const mod = 998244353;
  // (x - z)(x + z) = y (0 <= z, 1 <= x, y <= n)
  // brute force (x - z)
  // count up y such that x - z is the lower divisor of y.
  long cnt = 0;
  for(long i = 1; i * i <= n; i++) {
    long j = n / i;
    cnt += 1 + (j - i) / 2;
  }
  cout << cnt % mod << endl;
}
