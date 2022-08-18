#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, x;
  cin >> n >> x;
  x *= 100;
  using pi = pair<int, int>;
  vector<pi> beer(n);
  for(int i = 0; i < n; i++) cin >> beer[i].first >> beer[i].second;
  for(int i = 0; i < n; i++) {
    auto& [v, p] = beer[i];
    x -= v * p;
    if(x < 0) {
      cout << i + 1 << endl;
      return 0;
    }
  }
  cout << -1 << endl;
}
