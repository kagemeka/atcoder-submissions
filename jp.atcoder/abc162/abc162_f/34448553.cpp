#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  function<long(int, int)> f;
  map<pair<int, int>, long> cache;
  f = [&](int i, int j) -> long {
    if(n - i < j) return 0;
    if(cache.count({i, j})) return cache[{i, j}];
    long s = a[i];
    s += f(i + 2, j);
    if(j >= 2) s = max(s, f(i + 1, j - 1));
    return cache[{i, j}] = s;
  };
  cout << f(0, 2 + (n & 1)) << endl;
}
