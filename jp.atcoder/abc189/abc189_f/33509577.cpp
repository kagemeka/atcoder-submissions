#include <bits/stdc++.h>
using namespace std;
struct linear {
  double a, b;
  linear(double a = 0, double b = 0): a(a), b(b) {}
  auto operator+(linear const& rhs) -> linear { return {a + rhs.a, b + rhs.b}; }
  auto operator-(linear const& rhs) -> linear { return {a - rhs.a, b - rhs.b}; }
  auto operator/(int x) -> linear { return {a / x, b / x}; }
};
auto main() -> int {
  int n, m, k;
  cin >> n >> m >> k;
  vector<bool> is_ng(n + 1);
  for(int i = 0; i < k; i++) {
    int x;
    cin >> x;
    is_ng[x] = true;
  }
  vector<linear> dp(n + m);
  auto s = dp[n];
  for(int i = n - 1; i >= 0; i--) {
    if(is_ng[i]) dp[i] = linear(1, 0);
    else dp[i] = s / m + linear(0, 1);
    s = s + dp[i];
    s = s - dp[i + m];
  }
  auto [a, b] = dp[0];
  double const eps = 1e-6;
  if(1 - a < eps) {
    cout << -1 << endl;
    return 0;
  }
  cout << setprecision(16) << b / (1 - a) << endl;
}
