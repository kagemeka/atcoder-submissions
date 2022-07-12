#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, q;
  cin >> n >> m >> q;
  vector<long> a(n + 2), b(m + 2);
  long const inf = 1l << 60;
  a[0] = -inf;
  a[n + 1] = inf;
  b[0] = -inf;
  b[m + 1] = inf;
  for(int i = 0; i < n; i++) cin >> a[i + 1];
  for(int i = 0; i < m; i++) cin >> b[i + 1];
  auto query = [&](long x) -> long {
    auto la = *--upper_bound(a.begin(), a.end(), x);
    auto lb = *--upper_bound(b.begin(), b.end(), x);
    auto ra = *lower_bound(a.begin(), a.end(), x);
    auto rb = *lower_bound(b.begin(), b.end(), x);
    return min(
      min(x - min(la, lb), max(ra, rb) - x),
      min(ra - lb + min(ra - x, x - lb), rb - la + min(rb - x, x - la))
    );
  };
  while(q--) {
    long x;
    cin >> x;
    cout << query(x) << endl;
  }
}
