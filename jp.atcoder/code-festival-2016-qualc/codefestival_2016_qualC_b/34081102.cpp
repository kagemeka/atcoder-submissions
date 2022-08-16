#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int k, t;
  cin >> k >> t;
  int mx = 0;
  for(int i = 0; i < t; i++) {
    int x;
    cin >> x;
    mx = max(mx, x);
  }
  cout << max(0, 2 * mx - k - 1) << endl;
}
