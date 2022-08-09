#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, q;
  cin >> n >> q;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  using pi = pair<int, int>;
  map<pi, int> qi;
  vector<int> res(q, -1);
  for(int i = 0; i < q; i++) {
    int x, k;
    cin >> x >> k;
    qi[{x, k}] = i;
  }
  map<int, int> cnt;
  for(int i = 0; i < n; i++) {
    auto& x = a[i];
    pi p = {x, ++cnt[x]};
    if(qi.count(p)) {
      res[qi[p]] = i + 1;
      qi.erase(p);
    }
  }
  for(auto& i: res) { cout << i << endl; }
}
