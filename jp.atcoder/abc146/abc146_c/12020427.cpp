#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int a, b;
  long long x;
  cin >> a >> b >> x;
  if (x >= a * 1e9 + b * 10) {
    cout << 1000000000 << '\n';
    return 0;
  }
  if (x < a + b) {
    cout << 0 << '\n';
    return 0;
  }
  long long ans = 0;
  for (int d = 1; d < 10; d++) {
    long long n = (x - b * d) / a;
    if (n < pow(10, d - 1)) continue;
    ans = max(ans, min(n, (long long)pow(10, d) - 1));
  }

  cout << ans << '\n';
  return 0;
}
