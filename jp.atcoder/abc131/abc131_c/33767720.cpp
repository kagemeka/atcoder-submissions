#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long a, b, c, d;
  cin >> a >> b >> c >> d;
  auto f = [&](long n, long x) -> long { return n / x; };
  auto g = [&](long n) -> long {
    return n - (f(n, c) + f(n, d) - f(n, lcm(c, d)));
  };
  cout << g(b) - g(a - 1) << endl;
}
