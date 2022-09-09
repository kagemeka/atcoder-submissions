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
  int const m = 26;
  int mx = 0;
  for(int s = 1; s < n2; s++) {
    vector<int> cnt(m);
    for(int i = 0; i < n; i++) {
      if(~s >> i & 1) continue;
      for(int j = 0; j < m; j++) {
        if(~a[i] >> j & 1) continue;
        cnt[j]++;
      }
    }
    int res = 0;
    for(auto& c: cnt) res += c == k;
    mx = max(mx, res);
  }
  cout << mx << endl;
}
