#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int a, b;
  cin >> a >> b;
  int c = a - a / 100 * 100 + 900;
  int d = b - b / 100 * 100 + 100;
  cout << max(c - b, a - d) << endl;
}
