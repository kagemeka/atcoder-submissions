#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  int x;
  cin >> x;

  for(int y = 0; y <= x; y++) {
    int rem = x - y * 100;
    if(0 <= rem && rem <= 5 * y) {
      cout << 1 << endl;
      return 0;
    }
  }
  cout << 0 << endl;
}