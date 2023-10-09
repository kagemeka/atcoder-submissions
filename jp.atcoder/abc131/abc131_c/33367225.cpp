#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long a, b, c, d;
  cin >> a >> b >> c >> d;
  long l = lcm(c, d);
  auto f = [&](long n) -> long { return n - n / c - n / d + n / l; };
  cout << f(b) - f(a - 1) << endl;
}
