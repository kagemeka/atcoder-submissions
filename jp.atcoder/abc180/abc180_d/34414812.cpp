#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long x, y, a, b;
  cin >> x >> y >> a >> b;
  long cnt = 0;
  while(true) {
    if(x > b / (a - 1)) break;
    int nx = x * a;
    if(nx >= y) break;
    cnt++;
    x = nx;
  }
  assert(x < y);
  cout << cnt + (y - x - 1) / b << endl;
}
