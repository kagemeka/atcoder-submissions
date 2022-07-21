#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  int max_l = 0, min_r = n;
  while(m--) {
    int l, r;
    cin >> l >> r;
    max_l = max(max_l, l);
    min_r = min(min_r, r);
  }
  cout << max(0, min_r - max_l + 1) << endl;
}
