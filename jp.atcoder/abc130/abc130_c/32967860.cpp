#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int w, h, x, y;
  cin >> w >> h >> x >> y;

  long s = (double)w * h / 2;

  int flg = x * 2 == w && y * 2 == h;
  cout << s << ' ' << flg << endl;
}
