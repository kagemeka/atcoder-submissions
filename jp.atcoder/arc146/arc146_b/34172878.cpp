#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m, k;
  cin >> n >> m >> k;
  vector<int> a(n);
  for(int i = 0; i < n; i++) { cin >> a[i]; }
  // greedy from topbit
  // int l = ;
  int res = 0;
  // for(int i = 9; i >= 0; i--) {
  for(int i = 29; i >= 0; i--) {
    sort(a.rbegin(), a.rend());
    n = a.size();
    assert(n >= k);
    int v = 1 << i;
    int cnt = 0;
    long todo = 0;
    vector<int> b;
    vector<int> delta(n);
    for(int j = 0; j < n; j++) {
      auto& x = a[j];
      if(x >> i & 1) {
        b.push_back(x);
        cnt++;
        continue;
      }
      assert(v > x);
      if(j >= k) break;
      delta[j] = v - x;
      if(j < k) todo += delta[j];
    }
    for(auto& x: a) { x &= ~(1 << i); }
    // cout << i << ' ' << todo << endl;
    if(todo > m) { continue; }
    for(int j = cnt; j < n; j++) { a[j] = 0; }
    m -= todo;
    res += v;
    while((int)a.size() > max(cnt, k)) a.pop_back();
    // for(auto& ) {}
  }
  cout << res << endl;
}
