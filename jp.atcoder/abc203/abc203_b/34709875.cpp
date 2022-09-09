#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  auto f = [&](int n, int m) -> int { return (1 + n) * n / 2 * m; };
  cout << f(n, k) * 100 + f(k, n) << endl;
}
