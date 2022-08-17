#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  set<int> ng;
  for(int i = 0; i < 3; i++) {
    int x;
    cin >> x;
    ng.insert(x);
  }
  auto f = [&]() -> bool {
    if(ng.count(n)) return false;
    for(int t = 0; t < 100; t++) {
      bool flg = false;
      for(int d = 3; d >= 1; d--) {
        int y = n - d;
        if(ng.count(y)) continue;
        n = y;
        flg = true;
        break;
      }
      if(!flg) return false;
      if(n <= 0) return true;
    }
    return false;
  };
  cout << (f() ? "YES" : "NO") << endl;
}
