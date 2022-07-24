#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int a, b, c, d;
  cin >> a >> b >> c >> d;
  cout << max(0, min(b, d) - max(a, c)) << endl;
}
