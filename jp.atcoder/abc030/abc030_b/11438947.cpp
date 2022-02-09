#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  n %= 12;

  double a, b;
  b = 6 * m;
  a = 30 * (n + b / 360);
  double ans = min(abs(a - b), abs(b - a));
  cout << setprecision(10) << ans << '\n';
  return 0;
}
