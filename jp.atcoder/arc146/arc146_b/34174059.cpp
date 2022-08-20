#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n, m, k;
  cin >> n >> m >> k;
  vector<long> a(n);
  for(long i = 0; i < n; i++) { cin >> a[i]; }
  // greedy from topbit
  // long l = ;
  long res = 0;
  // for(long i = 9; i >= 0; i--) {
  for(long i = 29; i >= 0; i--) {
    sort(a.rbegin(), a.rend());
    n = a.size();
    assert(n >= k);
    long v = 1 << i;
    long cnt = 0;
    long todo = 0;
    // vector<long> b;
    vector<long> delta(n);
    for(long j = 0; j < n; j++) {
      auto& x = a[j];
      if(x >> i & 1) {
        // b.push_back(x);
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
    for(long j = cnt; j < n; j++) { a[j] = 0; }
    m -= todo;
    res += v;
    while((long)a.size() > max(cnt, k)) a.pop_back();
    // for(auto& ) {}
  }
  cout << res << endl;
}
