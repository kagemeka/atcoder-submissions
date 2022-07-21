#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int a, b, c, d;
  cin >> a >> b >> c >> d;
  cout << (a == c || a == d || b == c || b == d ? "YES" : "NO") << endl;
}
