#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, c, x;
  cin >> a >> b >> c >> x;
  x /= 50;
  int res = 0;
  for (int i = 0; i <= a; i++) {
    for (int j = 0; j <= b; j++) {
      int r = x - 10 * i - 2 * j;
      res += (0 <= r && r <= c);
    }
  }
  cout << res << '\n';
  return 0;
}
