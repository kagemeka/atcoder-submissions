#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, h;
  cin >> n >> h;
  vector<int> a(n);
  int mx = 0;
  for(int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    mx = max(mx, x);
    a[i] = y;
  }
  sort(a.rbegin(), a.rend());
  int cnt = 0;
  for(auto& x: a) {
    if(x <= mx) break;
    h -= x;
    cnt++;
    if(h <= 0) break;
  }
  if(h > 0) { cnt += (h + mx - 1) / mx; }
  cout << cnt << endl;
}
