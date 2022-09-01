#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s, t;
  cin >> s >> t;
  int n = s.size();
  int m = t.size();
  int mn = 1 << 30;
  for(int i = 0; i < n - m + 1; i++) {
    int cnt = 0;
    for(int j = 0; j < m; j++) { cnt += s[i + j] != t[j]; }
    mn = min(mn, cnt);
  }
  cout << mn << endl;
}
