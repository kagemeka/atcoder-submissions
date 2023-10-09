#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int r0, c0, r1, c1;
  cin >> r0 >> c0 >> r1 >> c1;
  int dy = abs(r1 - r0);
  int dx = abs(c1 - c0);
  if(dx == 0 && dy == 0) {
    cout << 0 << endl;
  } else if(dx + dy <= 3 || dx == dy) {
    cout << 1 << endl;
  } else if(abs(dx - dy) <= 3 || dx + dy <= 6 || ((dx - dy) & 1) == 0) {
    cout << 2 << endl;
  } else {
    cout << 3 << endl;
  }
}
