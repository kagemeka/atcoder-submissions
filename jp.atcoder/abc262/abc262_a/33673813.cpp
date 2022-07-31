#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int y;
  cin >> y;
  int r = y % 4;
  y += (6 - r) % 4;
  cout << y << endl;
}
