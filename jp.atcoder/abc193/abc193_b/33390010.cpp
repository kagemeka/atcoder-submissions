#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n), p(n), x(n);
  for(int i = 0; i < n; i++) cin >> a[i] >> p[i] >> x[i];
  int const inf = 1 << 30;
  int mn = inf;
  for(int i = 0; i < n; i++) {
    if(x[i] - a[i] > 0) mn = min(mn, p[i]);
  }
  cout << (mn == inf ? -1 : mn) << endl;
}
