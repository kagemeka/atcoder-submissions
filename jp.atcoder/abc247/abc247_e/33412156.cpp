#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, mx, mn;
  cin >> n >> mx >> mn;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<bool> b(n);
  for(int i = 0; i < n; i++) b[i] = a[i] < mn || a[i] > mx;
  vector<bool> b0 = b, b1 = b, b2 = b;
  for(int i = 0; i < n; i++) {
    b0[i] = b0[i] || a[i] == mx;
    b1[i] = b1[i] || a[i] == mn;
    b2[i] = b2[i] || a[i] == mx || a[i] == mn;
  }
  auto f = [&](vector<bool> const& b) -> long {
    long res = 0;
    int now = 0;
    for(int i = 0; i < n; i++) {
      if(!b[i]) {
        now++;
        continue;
      }
      res += (long)now * (now + 1) >> 1;
      now = 0;
    }
    res += (long)now * (now + 1) >> 1;
    return res;
  };
  cout << f(b) - f(b0) - f(b1) + f(b2) << endl;
}
