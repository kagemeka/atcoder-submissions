#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> f(n);
  for(int i = 0; i < n; i++) {
    cin >> f[i];
    f[i]--;
  }
  function<void(int u)> dfs;
  vector<int> state(n, 0);
  int cnt = 0;
  dfs = [&](int u) {
    state[u] = 1;
    int v = f[u];
    if(state[v] == 1) { cnt++; }
    if(state[v] == 0) { dfs(v); }
    state[u] = 2;
  };
  for(int i = 0; i < n; i++) {
    if(state[i] != 2) dfs(i);
  }
  long const mod = 998244353;
  long p = 1;
  for(int i = 0; i < cnt; i++) {
    p *= 2;
    p %= mod;
  }
  p--;
  p += mod;
  p %= mod;
  cout << p << endl;
}
