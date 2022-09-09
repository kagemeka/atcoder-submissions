#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  int n2 = 1 << n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) {
    string s;
    cin >> s;
    int x = 0;
    for(auto& c: s) { x |= 1 << (c - 'a'); }
    a[i] = x;
  }
  auto popcnt = [&](int x) -> int { return __builtin_popcount(x); };
  int full = (1 << 26) - 1;
  int res = 0;
  for(int s = 1; s < n2; s++) {
    int t = full;
    int c = 0;
    for(int i = 0; i < n; i++) {
      if(~s >> i & 1) continue;
      t &= a[i];
      c++;
    }
    if(c != k) continue;
    res |= t;
  }
  cout << popcnt(res) << endl;
}
