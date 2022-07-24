#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, v;
  cin >> n >> v;
  int k = 30;
  int x0 = 0, x1 = (1 << k) - 1;
  while(n--) {
    int t, a;
    cin >> t >> a;
    if(t == 1) {
      x0 &= a;
      x1 &= a;
    }
    if(t == 2) {
      x0 |= a;
      x1 |= a;
    }
    if(t == 3) {
      x0 ^= a;
      x1 ^= a;
    }
    v = (v & x1) | (~v & x0);
    cout << v << endl;
  }
}
