#include <bits/stdc++.h>
using namespace std;
template<typename T> void print(vector<T> v) {
  for(int i = 0; i < (int)v.size(); ++i) {
    cout << v[i] << " \n"[i == (int)v.size() - 1];
  }
}
template<typename T, unsigned long N> void print(array<T, N> v) {
  for(unsigned long i = 0; i < N; ++i) { cout << v[i] << " \n"[i == N - 1]; }
}
template<typename T> void print(const T& v) { cout << v << '\n'; }
template<typename T, typename... U> void print(const T& t, const U&... args) {
  cout << t << ' ';
  print(args...);
}
template<typename T, typename... U>
void print(char sep, const T& t, const U&... args) {
  if(sizeof...(args) > 0) {
    cout << t << sep;
    print(sep, args...);
  } else {
    print(t);
  }
}
#ifdef CPP_DEBUG // g++ -DCPP_DEBUG ...
#define debug(...) print(__VA_ARGS__);
#else
#define debug(...) nullptr
#endif
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<vector<pair<int, int>>> g(n);
  for(int i = 0; i < n; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].emplace_back(v, i);
    g[v].emplace_back(u, i);
  }
  // check edge id
  vector<bool> on_cycle(n);
  vector<bool> on_stack(n);
  vector<bool> visited(n);
  function<int(int, int)> dfs;
  dfs = [&](int u, int eid_u) -> int {
    if(on_stack[u]) {
      on_cycle[u] = true;
      return u ;
    }

    int k = -1;
    on_stack[u] = true;
    for(auto& [v, eid_v]: g[u]) {
      if(eid_v == eid_u) continue;
      // cout << u + 1 << ' ' << v + 1 << " a\n\n";
      k = dfs(v, eid_v);
      // if  (k == u)
      if (k != -1) on_cycle[u] = true;
      // if(on_stack[v] && on_cycle[]) on_cycle[u] = true;
    }
    // cout << u + 1 << ' ' << on_cycle[u] << " b\n\n";
    if (k == u) k = -1;
    on_stack[u] = false;
    return k;
  };
  dfs(0, -1);
  queue<int> que;
  vector<int> leader(n, -1);
  for(int i = 0; i < n; i++) {
    if(on_cycle[i]) {
      leader[i] = i;
      que.push(i);
    }
  }
  while(que.size()) {
    int u = que.front();
    que.pop();
    for(auto [v, _]: g[u]) {
      if(leader[v] != -1) continue;
      leader[v] = leader[u];
      que.push(v);
    }
  }
  auto f = [&](int u, int v) -> bool {
    if(on_cycle[u]) { swap(u, v); }
    if(on_cycle[u]) { return false; }
    return leader[u] == leader[v];
    // if(on_cycle[v]) { return leader[u] == v; }
  };
  debug(on_cycle);
  debug(leader);
  int q;
  cin >> q;
  while(q--) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    cout << (f(u, v) ? "Yes" : "No") << '\n';
  }
}
