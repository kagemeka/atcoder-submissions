#include <bits/stdc++.h>
using namespace std;

template<typename G, typename F> auto graph_dfs(const G& g, F f, int src)
  -> void {
  function<void(int)> dfs;
  dfs = [&](int u) -> void {
    for(auto& v: g[u])
      if(f(u, v)) dfs(v);
  };
  dfs(src);
}

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, k;
  cin >> n >> k;

  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int a, b;
    cin >> a >> b;
    a--;
    b--;
    g[a].push_back(b);
    g[b].push_back(a);
  }

  vector<int> parent(n, -1), cnt(n, 0), rem(n, k - 1);
  parent[0] = 0;

  cnt[0] = k;

  auto f = [&](int u, int v) -> bool {
    if(v == parent[u]) return false;
    parent[v] = u;
    cnt[v] = max(0, rem[u]);
    rem[v]--;
    rem[u]--;
    return true;
  };

  graph_dfs(g, f, 0);

  int const mod = 1000000007;

  long p = 1;
  for(auto& c: cnt) {
    p *= c;
    p %= mod;
  }
  cout << p << endl;
}
