#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int x, y, n, m, l;
  cin >> x >> y >> n >> m >> l;

  priority_queue<pair<int, int>> que;
  for (int i = 0; i < n; i++) {
    int v;
    cin >> v;
    que.push({v, 0});
  }
  for (int i = 0; i < m; i++) {
    int v;
    cin >> v;
    que.push({v, 1});
  }
  for (int i = 0; i < l; i++) {
    int v;
    cin >> v;
    que.push({v, 2});
  }

  int a = 0, b = 0, c = 0;
  long s = 0;
  while (true) {
    auto [v, i] = que.top();
    que.pop();
    if (i == 0) {
      if (a == x) continue;
      a++;
      s += v;
    }
    if (i == 1) {
      if (b == y) continue;
      b++;
      s += v;
    }
    if (i == 2) {
      c++;
      s += v;
    }
    if (a + b + c == x + y) break;
  }
  cout << s << endl;
}
