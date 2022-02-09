#include <iostream>
#include <vector>
#include <tuple>
#include <map>
#include <functional>
#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int w, h, n; cin >> w >> h >> n;
  vector<int> x(n), y(n);
  for (int i = 0; i < n; i++) {
    cin >> x[i] >> y[i];
    x[i]--; y[i]--;
  }
  using Rectangle = tuple<int, int, int, int>;
  map<Rectangle, int> cache;
  function<int(Rectangle)> count = [&](const Rectangle rect) -> int {
    if (cache.count(rect)) return cache[rect];
    int mx = 0;
    int l, r, d, u;
    tie(l, r, d, u) = rect;
    for (int i = 0; i < n; i++) {
      if (x[i] < l or r <= x[i] or y[i] < d or u <= y[i]) continue;
      int cnt = r - l + u - d - 1;
      cnt += count(Rectangle(l, x[i], d, y[i]));
      cnt += count(Rectangle(x[i] + 1, r, d, y[i]));
      cnt += count(Rectangle(l, x[i], y[i] + 1, u));
      cnt += count(Rectangle(x[i] + 1, r, y[i] + 1, u));
      mx = max(mx, cnt);
    }
    return cache[rect] = mx;
  };
  cout << count(Rectangle(0, w, 0, h)) << '\n';
}
