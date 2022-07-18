#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  using pi = pair<int, int>;
  vector<pi> xy(n);
  for(int i = 0; i < n; i++) cin >> xy[i].first >> xy[i].second;
  sort(xy.begin(), xy.end());
  auto possible = [&](int d) -> bool {
    set<int> st;
    for(int i = 0, j = 0; i < n; i++) {
      auto& [x, y] = xy[i];
      while(j < i && x - xy[j].first >= d) {
        st.insert(xy[j].second);
        j++;
      }
      if(st.lower_bound(y + d) != st.end() || st.upper_bound(y - d) != st.begin())
        return true;
    }
    return false;
  };
  long ok = 0, ng = 1l << 31;
  while(ng - ok > 1) {
    int d = (ok + ng) >> 1;
    if(possible(d)) ok = d;
    else ng = d;
  }
  cout << ok << endl;
}
