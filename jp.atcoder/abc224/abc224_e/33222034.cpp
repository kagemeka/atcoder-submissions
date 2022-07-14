#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int h, w, n;
  cin >> h >> w >> n;
  using tup = tuple<int, int, int, int>;
  vector<tup> a(n);
  for(int i = 0; i < n; i++) {
    int r, c, x;
    cin >> r >> c >> x;
    r--;
    c--;
    a[i] = {x, r, c, i};
  }
  sort(a.rbegin(), a.rend());
  vector<int> dist_r(h, -1), dist_c(w, -1);
  vector<int> res(n);
  for(int j = 0; j < n;) {
    auto& x = get<0>(a[j]);
    int k = j;
    while(k < n) {
      auto& [y, r, c, i] = a[k];
      if(y != x) break;
      res[i] = max(dist_r[r], dist_c[c]) + 1;
      k++;
    }
    while(j < k) {
      auto& [y, r, c, i] = a[j];
      dist_r[r] = max(dist_r[r], res[i]);
      dist_c[c] = max(dist_c[c], res[i]);
      j++;
    }
  }
  for(auto& d: res) { cout << d << endl; }
}
