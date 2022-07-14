#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int const k = 200;
  using p = pair<int, int>;
  vector<p> index(k, {-1, -1});
  vector<vector<bool>> a(3, vector<bool>(3));
  for(int i = 0; i < 3; i++)
    for(int j = 0; j < 3; j++) {
      int x;
      cin >> x;
      index[x] = {i, j};
    }
  int n;
  cin >> n;
  for(int i = 0; i < n; i++) {
    int b;
    cin >> b;
    auto [y, x] = index[b];
    if(y == -1) continue;
    a[y][x] = true;
  }
  auto rot90 = [&]() {
    auto b = a;
    for(int i = 0; i < 3; i++) {
      for(int j = 0; j < 3; j++) { b[j][3 - i - 1] = a[i][j]; }
    }
    a = b;
  };
  bool ok = false;
  for(int t = 0; t < 2; t++) {
    for(int i = 0; i < 3; i++) { ok |= a[i][0] && a[i][1] && a[i][2]; }
    ok |= a[0][0] && a[1][1] && a[2][2];
    rot90();
  }
  cout << (ok ? "Yes" : "No") << endl;
}
