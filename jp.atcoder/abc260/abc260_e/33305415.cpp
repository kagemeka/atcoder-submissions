#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  // shakutori imos
  int n, m;
  cin >> n >> m;
  using p = pair<int, int>;
  vector<p> a(n);
  for(int i = 0; i < n; i++) cin >> a[i].first >> a[i].second;
  vector<int> res(m + 2);
  vector<int> cnt(n);
  vector<vector<int>> b(m + 1);
  for(int i = 0; i < n; i++) {
    auto& [x, y] = a[i];
    b[x].push_back(i);
    b[y].push_back(i);
  }
  int r = 1;
  int now = 0;
  int i = 1;
  while(i < m + 1) {
    while(r < m + 1 && now < n) {
      for(auto& j: b[r]) {
        cnt[j]++;
        if(cnt[j] == 1) now++;
      }
      r++;
    }
    if(r == m + 1 && now < n) break;
    int d = r - i;
    int dmax = m - i + 1;
    // cout << d << ' ' << dmax << endl;
    res[d] += 1;
    res[dmax + 1] -= 1;
    for(auto& j: b[i]) {
      cnt[j]--;
      if(cnt[j] == 0) now--;
    }
    i++;
  }
  // cout << m << endl;
  // cout << res.size() << endl;
  for(int i = 0; i < m + 1; i++) { res[i + 1] += res[i]; }
  for(int i = 1; i < m + 1; i++) { cout << res[i] << " \n"[i == m]; }
}
