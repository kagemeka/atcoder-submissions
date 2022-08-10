#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int l;
  cin >> l;
  using tup = tuple<int, int, int>;
  vector<tup> res;
  int i = 0;
  while(l > 1) {
    if(l & 1) { res.emplace_back(i, -1, (l - 1) << i); }
    l >>= 1;
    res.emplace_back(i, i + 1, 0);
    res.emplace_back(i, i + 1, 1 << i);
    i++;
  }
  int n = i + 1;
  cout << n << ' ' << res.size() << endl;
  for(auto& [u, v, w]: res) {
    if(v == -1) v = n - 1;
    u++;
    v++;
    cout << u << ' ' << v << ' ' << w << endl;
  }
}
