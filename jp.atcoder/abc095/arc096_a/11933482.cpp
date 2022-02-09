#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int a, b, c, x, y;
  cin >> a >> b >> c >> x >> y;
  if (x > y) {
    swap(a, b);
    swap(x, y);
  }
  int tot = min(2 * c, a + b) * x;
  y -= x;
  tot += min(c * 2, b) * y;
  cout << tot << '\n';
  return 0;
}
