#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long a, b, c, x, y;
  cin >> a >> b >> c >> x >> y;
  if(x > y) {
    swap(x, y);
    swap(a, b);
  }
  cout << min(c << 1, a + b) * x + min(c << 1, b) * (y - x) << endl;
}
