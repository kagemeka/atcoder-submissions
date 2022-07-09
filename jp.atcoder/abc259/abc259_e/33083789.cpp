#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  using pi = pair<int, int>;
  // using pi = pair<int, vector<int>>;
  map<int, vector<pi>> a;
  for(int i = 0; i < n; i++) {
    int m;
    cin >> m;
    for(int j = 0; j < m; j++) {
      int p, e;
      cin >> p >> e;
      a[p].emplace_back(e, i);
    }
  }
  int cnt = 1;
  vector<bool> flg(n);
  for(auto& [p, b]: a) {
    sort(b.begin(), b.end());
    int m = b.size();
    if(m == 1) {
      flg[b[0].second] = true;
    } else if(m > 1) {
      if(b[m - 1].first == b[m - 2].first) { continue; }
      flg[b[m - 1].second] = true;
    }
  }
  for(int i = 0; i < n; i++) {
    if(flg[i]) cnt++;
    // if(flg[i]) cout << i << endl;
  }
  cnt = min(cnt, n);
  cout << cnt << endl;
}
