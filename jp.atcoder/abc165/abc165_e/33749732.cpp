#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  if(n & 1) {
    for(int i = 0; i < m; i++) { cout << i + 1 << ' ' << n - i << endl; }
  } else {
    int l = 1, r = n;
    int t = (m + 1) >> 1;
    for(int i = 0; i < t; i++) {
      cout << l << ' ' << r << endl;
      l++;
      r--;
      m--;
    }
    l++;
    while(m--) {
      cout << l << ' ' << r << endl;
      l++;
      r--;
    }
  }
}
