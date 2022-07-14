#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  long s = 0;
  for(auto& x: a) s ^= x;
  long res = s;
  for(auto& x: a) x &= ~s;
  int r = 0;
  for(int k = 60; k >= 0; k--) {
    int i = r;
    for(; i < n; i++) {
      if(a[i] >> k & 1) { break; }
    }
    if(i == n) continue;
    swap(a[r], a[i]);
    for(int i = 0; i < n; i++) {
      if(i != r && a[i] >> k & 1) a[i] ^= a[r];
    }
    r++;
  }
  s = 0;
  for(auto& x: a) s ^= x;
  res += s << 1;
  cout << res << endl;
}
