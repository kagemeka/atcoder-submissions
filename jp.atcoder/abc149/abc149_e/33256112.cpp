#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  long m;
  cin >> n >> m;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  sort(a.rbegin(), a.rend());
  vector<long> cum(n + 1);
  for(int i = 0; i < n; i++) { cum[i + 1] = cum[i] + a[i]; }
  auto f = [&](int x) -> pair<long, long> {
    long s = 0, c = 0;
    for(int i = n - 1, r = 0; i >= 0; i--) {
      while(r < n && a[r] + a[i] >= x) r++;
      s += r * a[i] + cum[r];
      c += r;
    }
    return {c, s};
  };
  int ok = 0, ng = 1 << 18;
  while(ng - ok > 1) {
    int x = (ng + ok) >> 1;
    auto [c, s] = f(x);
    if(c < m) ng = x;
    else ok = x;
  }
  auto [c, s] = f(ok);
  long res = s - (c - m) * ok;
  cout << res << endl;
}
