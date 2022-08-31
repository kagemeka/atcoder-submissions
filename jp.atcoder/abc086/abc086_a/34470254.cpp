#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int a, b;
  cin >> a >> b;
  cout << ((a & 1) && (b & 1) ? "Odd" : "Even") << endl;
}
