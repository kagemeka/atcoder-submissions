#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, g; cin >> n >> g;
  vector<int> p(n);
  vector<int> c(n);
  for (int i = 0; i < n; i++) cin >> p[i] >> c[i];

  int res = 1001001001;
  for (int i = 0; i < (1 << n); i++) {
    int tot = 0;
    int cnt = 0;
    int k = -1;
    for (int j = 0; j < n; j++) {
      if (i >> j & 1) {
        cnt += p[j];
        tot += 100 * (j + 1) * p[j] + c[j];
      } else {
        k = j;
      }
    }
    if (tot >= g) {
      res = min(res, cnt);
    } else {
      int d = (g - tot + 100 * (k + 1) - 1) / (100 * (k + 1));
      if (d >= p[k]) continue;
      res = min(res, cnt + d);
    }
  }
  cout << res << '\n';
  return 0;
}
