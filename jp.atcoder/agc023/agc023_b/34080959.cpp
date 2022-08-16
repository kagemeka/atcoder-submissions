#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<string> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int res = 0;
  auto is_ok = [&](int i) -> bool {
    for(int y = 0; y < n; y++) {
      for(int x = 0; x < n; x++) {
        if(a[(i + y) % n][x] != a[(x + i) % n][y]) { return false; }
      }
    }
    return true;
  };
  for(int i = 0; i < n; i++) {
    if(is_ok(i)) res += n;
  }
  cout << res << endl;
}
