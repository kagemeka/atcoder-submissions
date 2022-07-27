#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s, t;
  int n;
  cin >> s >> t >> n;
  n += 2;
  vector<string> a(n);
  a[0] = s;
  a[n - 1] = t;
  for(int i = 0; i < n - 2; i++) cin >> a[i + 1];
  int k = s.size();
  auto diff = [&](string const& s, string const& t) -> int {
    int d = 0;
    for(int i = 0; i < k; i++) d += s[i] != t[i];
    return d;
  };
  vector<vector<int>> g(n);
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) {
      if(diff(a[i], a[j]) > 1) continue;
      g[i].push_back(j);
      g[j].push_back(i);
    }
  }
  queue<int> que;
  que.push(0);
  int const inf = 1 << 29;
  vector<int> dist(n, inf), prev(n, -1);
  dist[0] = 0;
  while(que.size()) {
    int u = que.front();
    que.pop();
    for(int v: g[u]) {
      int dv = dist[u] + 1;
      if(dv >= dist[v]) continue;
      prev[v] = u;
      dist[v] = dv;
      que.push(v);
    }
  }
  int d = dist[n - 1];
  if(d == inf) {
    cout << -1 << endl;
    return 0;
  }
  cout << max(0, d - 1) << endl;
  int v = n - 1;
  vector<int> path;
  while(v != 0) {
    path.push_back(v);
    v = prev[v];
  }
  path.push_back(v);
  for(int i = (int)path.size() - 1; i >= 0; i--) { cout << a[path[i]] << endl; }
}
