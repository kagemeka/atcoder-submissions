#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<int> a(m), b(m);
  for(int i = 0; i < m; i++) {
    cin >> a[i] >> b[i];
    a[i]--;
    b[i]--;
  }
  int k;
  cin >> k;
  vector<vector<int>> x(k, vector<int>(2));
  for(int i = 0; i < k; i++) {
    for(int j = 0; j < 2; j++) {
      cin >> x[i][j];
      x[i][j]--;
    }
  }
  int mx = 0;
  for(int s = 0; s < 1 << k; s++) {
    vector<bool> ok(n);
    for(int i = 0; i < k; i++) { ok[x[i][s >> i & 1]] = true; }
    int cnt = 0;
    for(int i = 0; i < m; i++) { cnt += ok[a[i]] && ok[b[i]]; }
    mx = max(mx, cnt);
  }
  cout << mx << endl;
}
