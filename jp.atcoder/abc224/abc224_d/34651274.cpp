#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int m;
  cin >> m;
  int n = 9;
  vector<vector<int>> g(n);
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  string s(n, '9');
  for(int i = 0; i < n - 1; i++) {
    int p;
    cin >> p;
    p--;
    s[p] = (char)(i + '1');
  }
  string t;
  for(int i = 0; i < n; i++) t += to_string(i + 1);
  map<string, int> dist;
  dist[s] = 0;
  queue<string> que;
  que.push(s);
  int const inf = 1 << 30;
  while(que.size()) {
    string u = que.front();
    que.pop();
    int i = 0;
    while(i < n) {
      if(u[i] == '9') break;
      i++;
    }
    int d = dist[u] + 1;
    for(auto& j: g[i]) {
      auto v = u;
      swap(v[i], v[j]);
      int dv = dist.count(v) ? dist[v] : inf;
      if(d >= dv) continue;
      dist[v] = d;
      que.push(v);
    }
  }
  int res = dist.count(t) ? dist[t] : inf;
  cout << (res == inf ? -1 : res) << endl;
}
