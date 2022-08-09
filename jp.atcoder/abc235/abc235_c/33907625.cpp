#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, q;
  cin >> n >> q;
  using pi = pair<int, int>;
  map<pi, int> res;
  map<int, int> cnt;
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    cnt[x]++;
    res[{x, cnt[x]}] = i + 1;
  }
  while(q--) {
    int x, k;
    cin >> x >> k;
    cout << (res.count({x, k}) ? res[{x, k}] : -1) << endl;
  }
}
