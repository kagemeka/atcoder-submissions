#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int r, u, n;
  cin >> r >> u >> n;
  int l = 0, d = 0;

  int x, y, a;
  for (int i = 0; i < n; i++) {
    cin >> x >> y >> a;
    if (a == 1) {l = x;}
    else if (a == 2) {r = x;}
    else if (a == 3) {d = y;}
    else if (a == 4) {u = y;}
  }
  cout << max(0, u - d) * max(0, r - l) << '\n';
  return 0;
}
