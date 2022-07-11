#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, s, d;
  cin >> n >> s >> d;
  using p = pair<int, int>;
  vector<p> xy(n);
  for(int i = 0; i < n; i++) cin >> xy[i].first >> xy[i].second;
  for(auto& [x, y]: xy) {
    if(x >= s || y <= d) continue;
    cout << "Yes" << endl;
    return 0;
  }
  cout << "No" << endl;
}
