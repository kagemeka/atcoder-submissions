#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int w, h, x, y;
  cin >> w >> h >> x >> y;

  long s = (double)w * h / 2;

  int flg = x == 0 || x == w || y == h || y == 0;
  cout << s << ' ' << flg << endl;
}
