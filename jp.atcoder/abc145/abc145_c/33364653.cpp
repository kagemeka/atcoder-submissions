#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  using pi = pair<int, int>;
  vector<pi> a(n);
  for(int i = 0; i < n; i++) cin >> a[i].first >> a[i].second;
  auto dist = [&](int i, int j) -> double {
    auto& [xi, yi] = a[i];
    auto& [xj, yj] = a[j];
    double dx = xj - xi;
    double dy = yj - yi;
    return sqrt(dx * dx + dy * dy);
  };
  double tot = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) { tot += dist(i, j); }
  }
  cout << setprecision(16) << tot * 2 / n << endl;
}
