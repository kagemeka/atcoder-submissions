#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  if(m < 0 || m == n) {
    cout << -1 << endl;
    return 0;
  }
  if(n == 1) {
    if(m != 0) {
      cout << -1 << endl;
    } else {
      cout << 1 << ' ' << 2 << endl;
    }
    return 0;
  }
  if(m >= n - 1) {
    cout << -1 << endl;
    return 0;
  }
  int l = 1, r = 1000000000;
  cout << l << ' ' << r << endl;
  for(int i = 0; i < n - 2 - m; i++) {
    l++;
    r--;
    cout << l << ' ' << r << endl;
  }
  r = l;
  for(int i = 0; i < m + 1; i++) {
    l = r + 1, r = r + 2;
    cout << l << ' ' << r << endl;
  }
}
