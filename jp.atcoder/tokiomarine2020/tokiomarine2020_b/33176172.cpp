#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  long a, v, b, w, t;
  cin >> a >> v >> b >> w >> t;
  cout << (abs(b - a) + (w - v) * t <= 0 ? "YES" : "NO") << endl;
}
