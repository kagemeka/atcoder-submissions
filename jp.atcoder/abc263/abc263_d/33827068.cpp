#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n, l, r;
  cin >> n >> l >> r;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  long tot = 0;
  for(int i = 0; i < n; i++) tot += a[i];
  vector<long> d(n + 1);
  for(int i = 0; i < n; i++) d[i + 1] = l - a[i];
  for(int i = 0; i < n; i++) d[i + 1] += d[i];
  vector<long> mn = d;
  for(int i = 0; i < n; i++) mn[i + 1] = min(mn[i + 1], mn[i]);
  long res = min(r * n, l * n);
  long diff = 0;
  // for (int i = 0; i <= n; i++) cout << mn[i] <<" \n"[i == n];
  for(int i = 0; i <= n; i++) {
    if(i >= 1) { diff += r - a[n - i]; }
    res = min(res, tot + mn[n - i] + diff);
  }
  cout << res << endl;
}
