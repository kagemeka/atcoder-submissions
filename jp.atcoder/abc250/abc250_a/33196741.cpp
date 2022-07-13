#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w, r, c;
  cin >> h >> w >> r >> c;
  cout << 4 - (r == 1) - (r == h) - (c == 1) - (c == w) << endl;
}
