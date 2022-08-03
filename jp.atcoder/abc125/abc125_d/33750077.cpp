#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int p = 0;
  int mn = 1 << 30;
  long s = 0;
  for(auto x: a) {
    p ^= x < 0;
    x = abs(x);
    s += x;
    mn = min(mn, x);
  }
  if(p) { s -= 2 * mn; }
  cout << s << endl;
}
