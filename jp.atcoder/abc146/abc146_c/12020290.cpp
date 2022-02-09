#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int a, b;
  long long x;
  cin >> a >> b >> x;
  int tmp = 0;
  for (int d = 1; d <= 9; d++) {
    long long y = x - b * d;
    if (y < a * pow(10, d - 1)) {
      cout << tmp << '\n';
      return 0;
    } else if (y >= a * pow(10, d - 1) && y < a * pow(10, d)) {
      cout << y / a << '\n';
      return 0;
    } else {
      tmp = pow(10, d) - 1;
    }
  }
  int ans = (a * 1000000000 + b * 10 <= x) ? 1000000000 : tmp;
  cout << ans << '\n';
  return 0;
}
