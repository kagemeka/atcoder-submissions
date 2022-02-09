#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  long long w, h, x, y;
  cin >> w >> h >> x >> y;
  long double s = w * h / 2.0;
  int t = (x * 2 == w && y * 2 == h) ? 1 : 0;
  cout << setprecision(13) << s << " " << t << '\n';
  return 0;

}
