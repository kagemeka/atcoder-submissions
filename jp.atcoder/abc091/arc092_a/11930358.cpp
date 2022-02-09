#include <bits/stdc++.h>
using namespace std;

int INF = 1001;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> a(n);
  vector<int> b(n);
  vector<int> c(n);
  vector<int> d(n);
  for (int i = 0; i < n; i++) cin >> a[i] >> b[i];
  for (int i = 0; i < n; i++) cin >> c[i] >> d[i];
  vector<vector<int>> res;
  for (int i = 0; i < n; i++) res.push_back({a[i], b[i], 1});
  for (int i = 0; i < n; i++) res.push_back({c[i], d[i], 0});
  sort(res.begin(), res.end());
  bitset<1001> confirmed(0);
  int cnt = 0;
  for (int i = 0; i < n * 2 - 1; i++) {
    if (res[i][2]) {
      int yr = res[i][1];
      int yb = INF;
      int k;
      for (int j = i + 1; j < n * 2; j++) {
        if (confirmed[j]) continue;
        if (res[j][2]) continue;
        if (res[j][1] > yr && res[j][1] < yb) {
          yb = res[j][1]; k = j;
        }
      }
      if (yb == INF) continue;
      confirmed.set(k);
      cnt++;
    }
  }
  cout << cnt << '\n';
  return 0;

}
