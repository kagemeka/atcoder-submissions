#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, h, a, b, c, d, e;
  cin >> n >> h >> a >> b >> c >> d >> e;
  int res = c * n;
  for (int i = 0; i < n + 1; i++) {
    int j = (e * (n - i) - h - b * i) / (d + e) + 1;
    if (j >= 0 && i + i <= n) {
      res = min(res, a * i + c * j);
    }
  }
  cout << res << '\n';
  return 0;
}
