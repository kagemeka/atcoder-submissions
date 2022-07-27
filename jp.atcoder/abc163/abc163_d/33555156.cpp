#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  auto f = [&](int lo, int hi) -> long {
    return (long)(lo + hi) * (hi - lo + 1) >> 1;
  };
  int const mod = 1000000007;
  long res = 0;
  for(int i = k; i <= n + 1; i++) {
    long hi = f(n - i + 1, n);
    long lo = f(0, i - 1);
    res += hi - lo + 1;
    res %= mod;
  }
  cout << res << endl;
}
