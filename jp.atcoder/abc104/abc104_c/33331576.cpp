#include <bits/stdc++.h>
using namespace std;
auto clz64(long n) -> int { return __builtin_clzl(n); }
auto clz(int n) -> int { return __builtin_clz(n); }
auto bit_length(long n) -> int { return 64 - clz64(n); }
auto msb(long n) -> int {
  assert(n != 0);
  return bit_length(n) - 1;
}
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, g;
  cin >> n >> g;
  g /= 100;
  using pi = pair<int, int>;
  vector<pi> pc(n);
  for(int i = 0; i < n; i++) {
    cin >> pc[i].first >> pc[i].second;
    pc[i].second /= 100;
  }
  int mn = 1 << 30;
  int t = (1 << n) - 1;
  for(int s = 0; s < t + 1; s++) {
    int r = g;
    int cnt = 0;
    for(int i = 0; i < n; i++) {
      if(~s >> i & 1) continue;
      auto& [p, c] = pc[i];
      r -= (i + 1) * p + c;
      cnt += p;
    }
    if(r > 0) {
      int i = msb(t & ~s);
      auto& p = pc[i].first;
      int q = (r + i) / (i + 1);
      if(q >= p) continue;
      cnt += q;
    }
    mn = min(mn, cnt);
  }
  cout << mn << endl;
}
