#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  using pi = pair<int, int>;
  vector<pi> xy(n);
  for(int i = 0; i < n; i++) cin >> xy[i].first >> xy[i].second;
  sort(xy.begin(), xy.end());
  int const inf = (1l << 31) - 1;
  auto possible = [&](long d) -> bool {
    long mn = inf, mx = -inf;
    for(int i = 0, j = 0; i < n; i++) {
      auto& [x, y] = xy[i];
      while(j < i && x - xy[j].first >= d) {
        long py = xy[j].second;
        mn = min(mn, py);
        mx = max(mx, py);
        j++;
      }
      if(y - mn >= d || mx - y >= d) return true;
    }
    return false;
  };
  long ok = 0, ng = inf;
  while(ng - ok > 1) {
    int d = (ok + ng) >> 1;
    if(possible(d)) ok = d;
    else ng = d;
  }
  cout << ok << endl;
}
