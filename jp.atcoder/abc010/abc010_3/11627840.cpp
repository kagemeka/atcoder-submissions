#include <bits/stdc++.h>
using namespace std;

double dist(int &a, int &b, int &c, int &d) {
  return sqrt((c - a) * (c - a) + (d - b) * (d - b));
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, c, d, t, v, n;
  cin >> a >> b >> c >> d >> t >> v >> n;
  string ans = "NO";
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    if (dist(a, b, x, y) + dist(x, y, c, d) <= t * v) ans = "YES";
  }
  cout << ans << '\n';
  return 0;
}
