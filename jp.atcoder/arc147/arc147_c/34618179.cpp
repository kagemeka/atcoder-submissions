#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<pair<int, int>> lr(n);
  for(int i = 0; i < n; i++) cin >> lr[i].first >> lr[i].second;
  // ternary search population become median.
  // sliding window
  auto f = [&](int x) -> long {
    vector<long> b(n);
    for(int i = 0; i < n; i++) {
      auto& [l, r] = lr[i];
      if(x < l) b[i] = l;
      else if(r < x) b[i] = r;
      else b[i] = x;
    }
    sort(b.begin(), b.end());
    for(int i = n - 1; i >= 0; i--) { b[i] -= b[0]; }
    for(int i = n - 1; i > 0; i--) {
      b[i] -= b[i - 1];
      b[i] *= i;
    }
    for(int i = 0; i < n - 1; i++) b[i + 1] += b[i];
    return accumulate(b.begin(), b.end(), 0l);
  };
  int const inf = 1 << 30;
  int lmin = inf;
  int rmax = 0;
  for(auto& [l, r]: lr) {
    lmin = min(lmin, l);
    rmax = max(rmax, r);
  }
  int lo = lmin;
  int hi = rmax;
  // cout << lmin << ' ' << rmax << endl;
  while(lo + 1 < hi) {
    int x0 = (lo * 2 + hi + 2) / 3;
    int x1 = (lo + hi * 2) / 3;
    assert(lo <= x1 && x0 <= hi);
    if(f(x0) <= f(x1)) {
      hi = x1;
    } else {
      lo = x0;
    }
    // cout << lo << ' ' << hi << endl;
  }
  cout << min(f(lo), f(hi)) << endl;
  // int x = (f(lo) <= f(hi)) ? lo : hi;
  // for(int i = 0; i <= 6; i++) { cout << i << ' ' << f(i) << endl; }
  // cout << x << endl;
  // cout << f(x) << endl;
}
