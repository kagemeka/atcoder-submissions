#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, c, d, e, f;
  cin >> a >> b >> c >> d >> e >> f;
  set<int> w;
  set<int> s;
  for (int i = 0; i <= f + 1; i += 100 * a) {
    for (int j = 0; j < f - i + 1; j += 100 * b) {
      if (i == 0 && j == 0) continue;
      w.insert(i + j);
    }
  }
  for (int i = 0; i < f + 1; i += c) {
    for (int j = 0; j < f - i + 1; j += d) {
      s.insert(i + j);
    }
  }
  int u = 0, v = 0;
  for (auto &y : w) {
    for (auto &x : s) {
      if (y + x > f) break;
      if ((100 + e) * x > (y + x) * e) break;
      if (x * u >= v * (y + x)) {
        u = y + x;
        v = x;
      }
    }
  }
  cout << u << " " << v << '\n';
  return 0;
}
