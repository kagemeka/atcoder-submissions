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
  int n;
  cin >> n;
  vector<vector<pair<int, long>>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    long w;
    cin >> u >> v >> w;
    u--;
    v--;
    g[u].emplace_back(v, w);
    g[v].emplace_back(u, w);
  }
  vector<long> dist(n);
  function<void(int, int)> dfs;
  dfs = [&](int u, int p) {
    for(auto& [v, w]: g[u]) {
      if(v == p) continue;
      dist[v] = dist[u] ^ w;
      dfs(v, u);
    }
  };
  dfs(0, -1);
  int const k = 60;
  vector<int> c(k);
  for(auto& x: dist) {
    for(int i = 0; i < k; i++) c[i] += x >> i & 1;
  }
  debug(dist);
  long const mod = 1000000007;
  long s = 0;
  for(int i = 0; i < k; i++) {
    long v = (1l << i) % mod;
    s += ((long)c[i] * (n - c[i])) % mod * v % mod;
    s %= mod;
  }
  cout << s << '\n';
}
