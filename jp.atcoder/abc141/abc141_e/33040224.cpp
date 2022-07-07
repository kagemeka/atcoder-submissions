
#include <bits/stdc++.h>
using namespace std;
template<typename A> auto z_algorithm(const A& a) -> vector<int> {
  int n = a.size();
  vector<int> lcp(n, 0);
  for(int i = 1, l = 0; i < n; ++i) {
    auto r = l + lcp[l];
    auto d = r <= i ? 0 : std::min(lcp[i - l], r - i);
    while(i + d < n && a[i + d] == a[d]) ++d;
    lcp[i] = d;
    if(r < i + d) l = i;
  }
  lcp[0] = n;
  return lcp;
}
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  string s;
  cin >> n >> s;
  int mx = 0;
  for(int i = 0; i < n; i++) {
    auto lcp = z_algorithm(s.substr(i, n - i));
    for(int j = 0; j < (int)lcp.size(); j++) {
      if(lcp[j] <= j) mx = max(mx, lcp[j]);
    }
  }
  cout << mx << endl;
}
