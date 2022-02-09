#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int x;
  cin >> x;
  int res = 1;
  for (int i = 2; i < floor(sqrt(x)) + 1; i++) {
    int lo = 0;
    int hi = 11;
    while (lo + 1 < hi) {
      int m = (lo + hi) / 2;
      (pow(i, m) <= x) ? lo = m : hi = m;
    }
    res = max(res, (int)pow(i, lo));
  }
  cout << res << '\n';
  return 0;
}
