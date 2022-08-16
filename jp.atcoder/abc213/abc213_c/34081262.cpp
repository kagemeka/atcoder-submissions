#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w, n;
  cin >> h >> w >> n;
  vector<int> a(n), b(n);
  auto dedup = [&](vector<int> a) -> vector<int> {
    sort(a.begin(), a.end());
    a.erase(unique(a.begin(), a.end()), a.end());
    return a;
  };
  for(int i = 0; i < n; i++) cin >> a[i] >> b[i];
  auto va = dedup(a), vb = dedup(b);
  for(int i = 0; i < n; i++) {
    int y = lower_bound(va.begin(), va.end(), a[i]) - va.begin();
    int x = lower_bound(vb.begin(), vb.end(), b[i]) - vb.begin();
    cout << y + 1 << ' ' << x + 1 << '\n';
  }
}
