#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, d, x, y;
  cin >> n >> d >> x >> y;
  if(x < 0) x = -x;
  if(y < 0) y = -y;
  if(x % d || y % d) {
    cout << 0 << endl;
    return 0;
  }
  x /= d;
  y /= d;
  int m = n - x - y;
  if(m < 0 || m & 1) {
    cout << 0 << endl;
    return 0;
  }
  int const k = 1 << 10;
  vector<vector<double>> choose(k);
  for(int i = 0; i < k; i++) {
    choose[i] = vector<double>(i + 1, 1);
    for(int j = 1; j < i; j++) {
      choose[i][j] = choose[i - 1][j - 1] / 4 + choose[i - 1][j];
    }
    if(i > 0) choose[i][i] = choose[i - 1][i - 1] / 4;
  }
  double tot = 0;
  for(int d = 0; d <= m / 2; d++) {
    int u = y + d;
    int l = m / 2 - d;
    int r = x + l;
    tot += choose[n][d] * choose[n - d][u] * choose[n - d - u][l] *
           choose[n - d - u - l][r];
  }
  cout << setprecision(16) << tot << endl;
}
