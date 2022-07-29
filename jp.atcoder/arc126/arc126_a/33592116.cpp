#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int t;
  cin >> t;
  while(t--) {
    long x, y, z;
    cin >> x >> y >> z;
    y >>= 1;
    long cnt = 0;
    long c = min(y, z);
    y -= c;
    z -= c;
    cnt += c;
    c = min(z >> 1, x);
    z -= c << 1;
    x -= c;
    cnt += c;
    c = min(y, x >> 1);
    y -= c;
    x -= c << 1;
    cnt += c;
    c = min(x / 3, z);
    z -= c;
    x -= 3 * c;
    cnt += c;
    cnt += x / 5;
    cout << cnt << endl;
  }
}
