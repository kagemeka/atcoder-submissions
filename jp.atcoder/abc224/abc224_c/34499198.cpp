#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  using pi = pair<int, int>;
  vector<pi> p(n);
  for(int i = 0; i < n; i++) cin >> p[i].first >> p[i].second;
  int c = n * (n - 1) * (n - 2) / 6;
  for(int i = 0; i < n; i++) {
    auto& [xi, yi] = p[i];
    for(int j = 0; j < i; j++) {
      auto& [xj, yj] = p[j];
      for(int k = 0; k < j; k++) {
        auto& [xk, yk] = p[k];
        c -= (xj - xi) * (yk - yi) == (xk - xi) * (yj - yi);
      }
    }
  }
  cout << c << endl;
}
