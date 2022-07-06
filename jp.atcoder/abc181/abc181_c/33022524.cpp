#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  using p = pair<int, int>;
  vector<p> xy(n);
  for(int i = 0; i < n; i++) cin >> xy[i].first >> xy[i].second;

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) {
      for(int k = 0; k < j; k++) {
        auto [xi, yi] = xy[i];
        auto [xj, yj] = xy[j];
        auto [xk, yk] = xy[k];
        if((yj - yi) * (xk - xj) == (xj - xi) * (yk - yj)) {
          cout << "Yes" << endl;
          return 0;
        }
      }
    }
  }
  cout << "No" << endl;
}