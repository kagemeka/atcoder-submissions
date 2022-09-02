#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int w;
  cin >> w;
  cout << 300 << endl;
  int p = 1;
  for(int t = 0; t < 3; t++) {
    for(int i = 1; i <= 100; i++) { cout << p * i << ' '; }
    p *= 100;
  }
  cout << endl;
}
