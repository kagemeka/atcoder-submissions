#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  long x;
  cin >> n >> x;
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  function<long(long, int)> dfs;
  map<pair<long, int>, long> cache;
  dfs = [&](long x, int i) -> long {
    if(i == n - 1) { return x; }
    if(cache.count({x, i})) return cache[{x, i}];
    long b = a[i + 1] / a[i];
    long r = x % b;
    long q = x / b;
    return cache[{x, i}] = min(dfs(q, i + 1) + r, dfs(q + 1, i + 1) + (b - r));
  };
  long ans = dfs(x, 0);
  cout << ans << endl;
}
