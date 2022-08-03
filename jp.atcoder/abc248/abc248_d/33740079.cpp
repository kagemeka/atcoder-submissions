#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<vector<int>> b(n + 1);
  for(int i = 0; i < n; i++) { b[a[i]].push_back(i); }
  int q;
  cin >> q;
  for(int i = 0; i < q; i++) {
    int l, r, x;
    cin >> l >> r >> x;
    l--;
    r--;
    int res = upper_bound(b[x].begin(), b[x].end(), r) -
              lower_bound(b[x].begin(), b[x].end(), l);
    cout << res << endl;
  }
}
