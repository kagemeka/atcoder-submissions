#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  int parity = 0;
  int mn_abs = 1 << 30;
  long s = 0;
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    parity ^= x < 0;
    x = abs(x);
    s += x;
    mn_abs = min(mn_abs, x);
  }
  cout << (parity ? s - mn_abs * 2 : s) << endl;
}
