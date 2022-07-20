#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<string> a(n), b(m);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < m; i++) cin >> b[i];
  auto match = [&](int i, int j) -> bool {
    for(int y = 0; y < m; y++) {
      for(int x = 0; x < m; x++) {
        if(a[i + y][j + x] != b[y][x]) return false;
      }
    }
    return true;
  };
  for(int i = 0; i < n - m + 1; i++) {
    for(int j = 0; j < n - m + 1; j++) {
      if(match(i, j)) {
        cout << "Yes" << endl;
        return 0;
      }
    }
  }
  cout << "No" << endl;
}
