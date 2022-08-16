#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const k = 1 << 17;
  vector<int> l(k, n), r(k, -1);
  for(int i = 0; i < n; i++) {
    int x = a[i];
    l[x] = min(l[x], i);
    r[x] = max(r[x], i);
  }
  vector<pair<int, int>> b;
  for(int i = 0; i < k; i++) {
    if(l[i] == n) continue;
    b.emplace_back(l[i], r[i]);
  }
  int x = -1;
  int cnt = 1;
  for(auto& [l, r]: b) {
    if(l < x) { cnt++; }
    x = r;
  }
  if(x == 0) { cnt--; }
  cout << cnt << '\n';
}
