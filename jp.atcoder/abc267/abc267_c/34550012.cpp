#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  // shakutori
  // cumsum
  vector<long> s(n + 1);
  for(int i = 0; i < n; i++) s[i + 1] = s[i] + a[i];
  long const inf = 1l << 60;
  long mx = -inf;
  long now = 0;
  for(int i = 0; i < m; i++) { now += a[i] * (i + 1); }
  mx = now;
  for(int i = m; i < n; i++) {
    now -= s[i] - s[i - m];
    now += m * a[i];
    mx = max(mx, now);
  }
  cout << mx << endl;
}
