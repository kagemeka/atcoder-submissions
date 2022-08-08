#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<long> s(m + 1);
  long tot = 0;
  while(n--) {
    int l, r, x;
    cin >> l >> r >> x;
    l--;
    s[l] += x;
    s[r] -= x;
    tot += x;
  }
  long mx = 0;
  for(int i = 0; i < m; i++) {
    s[i + 1] += s[i];
    mx = max(mx, tot - s[i]);
  }
  cout << mx << endl;
}
