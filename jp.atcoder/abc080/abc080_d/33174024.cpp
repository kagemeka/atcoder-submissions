#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  int const k = 1 << 17;
  vector<vector<int>> a(m, vector<int>(k));
  while(n--) {
    int s, t, c;
    cin >> s >> t >> c;
    c--;
    a[c][s - 1] += 1;
    a[c][t] -= 1;
  }
  int mx = 0;
  for(int j = 0; j < k - 1; j++) {
    int cnt = 0;
    for(int i = 0; i < m; i++) {
      cnt += a[i][j];
      a[i][j + 1] += a[i][j];
    }
    mx = max(mx, cnt);
  }
  cout << mx << endl;
}
