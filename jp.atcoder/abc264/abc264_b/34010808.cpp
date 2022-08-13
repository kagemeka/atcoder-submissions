#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int y, x;
  cin >> y >> x;
  int dy = abs(y - 8);
  int dx = abs(x - 8);
  cout << (max(dy, dx) & 1 ? "black" : "white") << endl;
}
