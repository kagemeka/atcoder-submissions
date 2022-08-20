#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int a, b;
  cin >> a >> b;
  int c = a, d = b;
  for(int i = 2; i >= 0; i--) {
    int p = 1;
    for(int t = 0; t < i; t++) { p *= 10; }
    c = a - a / p % 10 * p + p * 9;
    if (c == a) continue;
    break;
  }
  for(int i = 2; i >= 0; i--) {
    int p = 1;
    for(int t = 0; t < i; t++) { p *= 10; }
    d = b - b / p % 10 * p + p;
    if(d == b) continue;
    break;
  }
  cout << max(c - b, a - d) << endl;
}
