#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  int mn_r = n;
  int mx_l = 1;
  while(m--) {
    int l, r;
    cin >> l >> r;
    mn_r = min(mn_r, r);
    mx_l = max(mx_l, l);
  }
  cout << max(0, mn_r - mx_l + 1) << endl;
}
