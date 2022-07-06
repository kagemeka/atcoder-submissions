#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, k;
  cin >> n >> k;

  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int s = 0;
  for(int i = 0; i < n; i++) s += a[i];
  vector<int> divs;
  for(int i = 1; i * i <= s; i++) {
    if(s % i) continue;
    divs.push_back(i);
    if(i * i != s) divs.push_back(s / i);
  }

  int mx = 1;

  auto possible = [&](int d) -> bool {
    int s = n * d;
    vector<int> r(n);
    for(int i = 0; i < n; i++) {
      r[i] = a[i] % d;
      s -= r[i];
    }
    sort(r.begin(), r.end());
    int tot = 0;
    for(auto& x: r) {
      s -= d;
      tot += x;
      if(s == 0) { return (tot <= k); }
    }
    return false;
  };

  for(auto& d: divs) {
    if(possible(d)) mx = max(mx, d);
  }
  cout << mx << endl;
}