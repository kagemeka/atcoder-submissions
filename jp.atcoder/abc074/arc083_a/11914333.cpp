#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, c, d, e, f;
  cin >> a >> b >> c >> d >> e >> f;
  vector<int> x;
  vector<int> y;
  for (int i = 0; i <= 15; i++) {
    for (int j = 0; j < 15; j++) {
      x.push_back(100 * (a * i + b * j));
    }
  }
  for (int i = 0; i < 1500; i++) {
    for (int j = 0; j < 1500; j++) {
      y.push_back(c * i + d * j);
    }
  }
  sort(x.begin(), x.end());
  sort(y.begin(), y.end());
  int u = 0, v = 0;
  for (int &s : x) {
    if (s > f) break;
    if (s == 0) continue;
    for (int &t : y) {
      if (s + t > f) break;
      if ((100 + e) * t > (s + t) * e) break;
      if (t * u >= v * (s + t)) {
        u = s + t;
        v = t;

      }
    }
  }
  cout << u << " " << v << '\n';
  return 0;
}
