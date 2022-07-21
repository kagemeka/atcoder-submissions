#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  long m;
  cin >> n >> m;
  // digit dp
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  bool just = true;
  int const k = 40;
  vector<int> cnt(k);
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < k; j++) { cnt[j] += a[i] >> j & 1; }
  }
  long x = 0;
  for(int i = k - 1; i >= 0; i--) {
    if(cnt[i] * 2 >= n) {
      x += (long)cnt[i] * (1l << i);
      if(m >> i & 1) { just = false; }
    } else {
      if(just && ~m >> i & 1) {
        x += (long)cnt[i] * (1l << i);
      } else {
        x += (long)(n - cnt[i]) * (1l << i);
      }
    }
  }
  cout << x << endl;
}
