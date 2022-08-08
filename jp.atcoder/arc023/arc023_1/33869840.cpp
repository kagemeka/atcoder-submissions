#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int y, m, d;
  cin >> y >> m >> d;
  // auto g = [](int n) -> int { return ((n - 3) % 12 + 12) % 12 + 3; };
  auto f = [&](int y, int m, int d) -> int {
    if(m < 3) {
      m += 12;
      y -= 1;
    }
    return 365 * y + y / 4 - y / 100 + y / 400 + 306 * (m + 1) / 10 + d - 429;
  };
  cout << f(2014, 5, 17) - f(y, m, d) << endl;
}
