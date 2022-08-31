#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int h, w, n;
  cin >> h >> w >> n;
  vector<tuple<int, int, int, int>> a(n);
  for(int i = 0; i < n; i++) {
    int r, c, x;
    cin >> r >> c >> x;
    r--;
    c--;
    a[i] = {x, r, c, i};
  }
  sort(a.rbegin(), a.rend());
  vector<int> res(n);
  vector<int> row(h), col(w);
  int k = 0;
  while(k < n) {
    auto& [u, r, c, i] = a[k];
    int j = k;
    while(j < n) {
      auto& [v, y, x, l] = a[j];
      if(v != u) break;
      res[l] = max(row[y], col[x]);
      j++;
    }
    while (k < j) {
      auto&[v, y, x, l] = a[k];
      row[y] = max(row[y], res[l] + 1);
      col[x] = max(col[x], res[l] + 1);
      k++;
    }
  }
  for(auto& x: res) cout << x << '\n';
}
