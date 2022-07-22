#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, mx, mn;
  cin >> n >> mx >> mn;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int cmax = 0, cmin = 0;
  int i = 0;
  long cnt = 0;
  for(int l = 0, r = 0; l < n; l++) {
    if(a[l] < mn || a[l] > mx) continue;
    r = max(r, l);
    i = max(i, l);
    while(r < n && mn <= a[r] && a[r] <= mx) { r++; }
    while(i < r && (cmax == 0 || cmin == 0)) {
      cmax += a[i] == mx;
      cmin += a[i] == mn;
      i++;
    }
    if(cmax > 0 && cmin > 0) cnt += r - i + 1;
    cmax -= a[l] == mx;
    cmin -= a[l] == mn;
  }
  cout << cnt << endl;
}
