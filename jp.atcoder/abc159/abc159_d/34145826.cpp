#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  int const k = 1 << 18;
  vector<int> cnt(k);
  for(int i = 0; i < n; i++) {
    int& x = a[i];
    cin >> x;
    cnt[x]++;
  }
  long tot = 0;
  for(auto& c: cnt) { tot += (long)c * (c - 1) >> 1; }
  for(auto& x: a) { cout << tot - cnt[x] + 1 << '\n'; }
}
