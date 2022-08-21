#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int x, y, n;
  cin >> x >> y >> n;
  y = min(y, x * 3);
  int q = n / 3;
  int r = n % 3;
  cout << x * r + q * y << endl;
}
