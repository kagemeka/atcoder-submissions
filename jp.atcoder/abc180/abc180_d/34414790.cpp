#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long x, y, a, b;
  cin >> x >> y >> a >> b;
  long cnt = 0;
  while(true) {
    long nx = x <= b / (a - 1) ? x * a : x + b;
    if(nx >= y) break;
    x = nx;
    cnt++;
  }
  assert(x < y);
  cout << cnt + (y - x - 1) / b << endl;
}
