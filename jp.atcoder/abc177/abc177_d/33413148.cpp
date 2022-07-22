#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<set<int>> g(n);
  while(m--) {
    int a, b;
    cin >> a >> b;
    g[--a].insert(--b);
    g[b].insert(a);
  }
  int mx = 0;
  for(int i = 0; i < n; i++) mx = max(mx, (int)g[i].size());
  cout << mx + 1 << endl;
}
