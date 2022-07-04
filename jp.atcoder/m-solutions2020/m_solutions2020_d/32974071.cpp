#include <bits/stdc++.h>

using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  int mx = 0;
  int mn = 1 << 10;
  for (int i = 0; i < n; i++) {
    mx = max(mx, 1000 / mn * (a[i] - mn));
    mn = min(mn, a[i]);
  }
  cout << 1000 + mx << endl;
}
