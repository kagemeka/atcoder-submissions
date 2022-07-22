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
  string s;
  cin >> s;
  auto z = z_algorithm(s);
  int n = s.size();
  for(int i = (n - 1) / 2; i >= 0; i--) {
    if(z[i] >= i) {
      cout << i * 2 << endl;
      return 0;
    }
  }
}
