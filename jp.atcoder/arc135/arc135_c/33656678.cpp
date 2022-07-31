#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const k = 30;
  vector<int> c(k);
  for(auto& x: a) {
    for(int i = 0; i < k; i++) { c[i] += x >> i & 1; }
  }
  auto sum = [&](vector<int> const& c) -> long {
    long s = 0;
    for(int i = 0; i < k; i++) { s += (1l << i) * c[i]; }
    return s;
  };
  long mx = sum(c);
  for(auto& x: a) {
    auto b = c;
    for(int i = 0; i < k; i++) {
      if(x >> i & 1) { b[i] = n - c[i]; }
    }
    mx = max(mx, sum(b));
  }
  cout << mx << endl;
}
