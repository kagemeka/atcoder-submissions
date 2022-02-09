#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int w, h, x, y;
  cin >> w >> h >> x >> y;
  double s = w * h / 2.0;
  int t = (x * 2 == w && y * 2 == h) ? 1 : 0;
  cout << setprecision(13) << s;
  cout << " " << t << '\n';
  return 0;

}
