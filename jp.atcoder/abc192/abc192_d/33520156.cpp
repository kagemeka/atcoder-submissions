#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  long m;
  cin >> s >> m;
  int n = s.size();
  vector<int> a(n);
  for(int i = 0; i < n; i++) a[i] = s[n - 1 - i] - '0';
  if(n == 1) {
    cout << (a[0] <= m) << endl;
    return 0;
  }
  int d = *max_element(a.begin(), a.end());
  auto is_ok = [&](long b) -> bool {
    long p = 1;
    long v = 0;
    for(int i = 0; i < n; i++) {
      v += p * a[i];
      if(v > m) { return false; }
      if(i == n - 1) break;
      if(p > m / b) return false;
      p *= b;
    }
    return true;
  };
  long ok = 1;
  long ng = m + 1;
  while(ng - ok > 1) {
    long b = (ok + ng) >> 1;
    if(is_ok(b)) ok = b;
    else ng = b;
  }
  cout << max(ok - d, 0l) << endl;
}
