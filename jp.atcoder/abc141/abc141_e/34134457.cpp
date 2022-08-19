#include <bits/stdc++.h>
using namespace std;
template<typename A> auto z_algorithm(const A& a) -> vector<int> {
  int n = a.size();
  vector<int> lcp(n);
  for(int i = 1, l = 0; i < n; i++) {
    int r = l + lcp[l];
    int d = r <= i ? 0 : min(lcp[i - l], r - i);
    while(i + d < n && a[i + d] == a[d]) d++;
    lcp[i] = d;
    if(i + d > r) l = i;
  }
  lcp[0] = n;
  return lcp;
}
auto main() -> int {
  int n;
  string s;
  cin >> n >> s;
  int mx = 0;
  for(int i = 0; i < n; i++) {
    auto z = z_algorithm(s.substr(i, n - i));
    for(int j = 0; j < n - i; j++) { mx = max(mx, min(j, z[j])); }
  }
  cout << mx << endl;
}
