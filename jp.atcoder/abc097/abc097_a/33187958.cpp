#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int a, b, c, d;
  cin >> a >> b >> c >> d;
  cout << ((abs(c - a) <= d || (abs(b - a) <= d && abs(c - b) <= d)) ? "Yes"
                                                                     : "No")
       << endl;
}