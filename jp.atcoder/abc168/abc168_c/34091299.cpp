#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  // m / 60, (h * 60 + m) / (60 * 12)
  // m * 60, (h * 60 + m) / 2
  double a, b, h, m;
  cin >> a >> b >> h >> m;
  auto const pi = acos(-1);
  double ta = m / 60 * 2 * pi;
  double tb = (h * 60 + m) / (60 * 12) * 2 * pi;
  double d = sqrt(a * a + b * b - 2 * a * b * cos(ta - tb));
  cout << setprecision(16) << d << endl;
}
