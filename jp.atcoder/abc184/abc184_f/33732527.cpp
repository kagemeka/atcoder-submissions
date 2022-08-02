#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, t;
  cin >> n >> t;
  // meet in the middle
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  auto enumerate = [&](vector<long> const& a) -> vector<long> {
    int n = a.size();
    vector<long> cand;
    for(int s = 0; s < 1 << n; s++) {
      long v = 0;
      for(int i = 0; i < n; i++) {
        if(s >> i & 1) v += a[i];
      }
      cand.push_back(v);
    }
    sort(cand.begin(), cand.end());
    return cand;
  };
  int m = n >> 1;
  vector<long> b, c;
  for(int i = 0; i < m; i++) b.push_back(a[i]);
  for(int i = m; i < n; i++) c.push_back(a[i]);
  b = enumerate(b);
  c = enumerate(c);
  long mx = 0;
  for(auto& x: b) {
    auto it = upper_bound(c.begin(), c.end(), t - x);
    if(it == c.begin()) break;
    mx = max(mx, x + *--it);
  }
  cout << mx << endl;
}
