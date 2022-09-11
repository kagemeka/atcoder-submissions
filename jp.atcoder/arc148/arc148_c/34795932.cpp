#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  // number of connected components
  // +
  // for each connected components,
  // how many children (initially face down) are there ?
  // if parent is in query set, components -= 1, childlren -= 1
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  cin >> n >> q;
  vector<int> c(n), p(n, -1);
  for(int i = 1; i < n; i++) {
    int x;
    cin >> x;
    x--;
    p[i] = x;
    c[x]++;
  }
  vector<bool> in_set(n);
  while(q--) {
    int m;
    cin >> m;
    vector<int> v(m);
    int cnt = 0;
    for(int i = 0; i < m; i++) {
      cin >> v[i];
      v[i]--;
      in_set[v[i]] = true;
      cnt++;
      cnt += c[v[i]];
    }
    for(auto& x: v) {
      if(x == 0) continue;
      if(in_set[p[x]]) cnt -= 2;
    }
    cout << cnt << '\n';
    for(auto& v: v) in_set[v] = false;
  }
}
