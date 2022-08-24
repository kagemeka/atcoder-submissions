#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, x, y;
  cin >> n >> x >> y;
  long a = 1, b = 0;
  for(int t = 0; t < n - 1; t++) {
    long c = a * x + b;
    a += c;
    b = y * c;
  }
  cout << b << endl;
}
