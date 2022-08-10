#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  using pi = pair<int, int>;
  vector<pi> yx(n);
  for(int i = 0; i < n; i++) cin >> yx[i].first >> yx[i].second;
  sort(yx.begin(), yx.end());
  long const inf = 1l << 62;
  auto f = [&](int y0, int y1) -> long {
    vector<long> a;
    for(int i = y0; i <= y1; i++) { a.push_back(yx[i].second); }
    sort(a.begin(), a.end());
    int m = a.size();
    long dy = yx[y1].first - yx[y0].first;
    long dx = inf;
    for(int i = 0; i < m - k + 1; i++) { dx = min(dx, a[i + k - 1] - a[i]); }
    return dx == inf ? inf : dx * dy;
  };
  long mn = inf;
  for(int y0 = 0; y0 < n; y0++) {
    for(int y1 = y0; y1 < n; y1++) { mn = min(mn, f(y0, y1)); }
  }
  cout << mn << endl;
}
