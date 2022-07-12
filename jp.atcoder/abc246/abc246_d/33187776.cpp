#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  long n;
  cin >> n;
  auto f = [&](long a, long b) -> long {
    long s = a + b;
    long t = a * b;
    return s * s * s - 2 * s * t;
  };
  auto find_b = [&](long a) -> long {
    long ng = -1, ok = 1 << 20;
    while(ok - ng > 1) {
      long b = (ng + ok) >> 1;
      if(f(a, b) >= n) ok = b;
      else ng = b;
    }
    return ok;
  };
  long mn = 1l << 62;
  for(int a = 0; a < 1 << 20; a++) {
    auto b = find_b(a);
    mn = min(mn, f(a, b));
  }
  cout << mn << endl;
}
