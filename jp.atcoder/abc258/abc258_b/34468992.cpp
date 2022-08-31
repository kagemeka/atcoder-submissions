#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<string> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  long mx = 0;
  auto f = [&](int i, int j) -> long {
    for(int dy = -1; dy < 2; dy++) {
      for(int dx = -1; dx < 2; dx++) {
        if (dy == 0 && dx == 0) continue;
        string s = "";
        for(int k = 0; k < n; k++) {
          int y = (i + dy * k) % n;
          int x = (j + dx * k) % n;
          y = (y + n) % n;
          x = (x + n) % n;
          s += a[y][x];
        }
        mx = max(mx, stol(s));
      }
    }
    return mx;
  };
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) { mx = max(mx, f(i, j)); }
  }
  cout << mx << endl;
}
