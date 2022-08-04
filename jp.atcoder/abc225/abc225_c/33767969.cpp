#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<vector<int>> a(n, vector<int>(m));
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      cin >> a[i][j];
      a[i][j]--;
    }
  }
  auto ok = [&]() -> bool {
    for(int i = 0; i < n - 1; i++) {
      if(a[i + 1][0] - a[i][0] != 7) return false;
    }
    for(int i = 0; i < n; i++) {
      int x = a[i][0] % 7;
      if(!(0 <= x && x <= 7 - m)) return false;
      for(int j = 0; j < m - 1; j++) {
        if(a[i][j + 1] - a[i][j] != 1) return false;
      }
    }
    return true;
  };
  cout << (ok() ? "Yes" : "No") << endl;
}
