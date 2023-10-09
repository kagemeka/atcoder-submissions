#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  using pi = pair<int, int>;
  vector<pi> a(n);
  for(int i = 0; i < n; i++) cin >> a[i].first >> a[i].second;
  vector<int> p(n);
  iota(p.begin(), p.end(), 0);
  int cnt = 0;
  double tot = 0;
  auto dist = [&](int i, int j) -> double {
    auto& [xi, yi] = a[i];
    auto& [xj, yj] = a[j];
    double dx = xj - xi;
    double dy = yj - yi;
    return sqrt(dx * dx + dy * dy);
  };
  do {
    double s = 0;
    for(int i = 0; i < n - 1; i++) { s += dist(p[i], p[i + 1]); }
    cnt++;
    tot += s;
  } while(next_permutation(p.begin(), p.end()));
  cout << setprecision(16) << tot / cnt << endl;
}
