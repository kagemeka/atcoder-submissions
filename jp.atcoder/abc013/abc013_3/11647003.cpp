#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  long long n, h, a, b, c, d, e;
  cin >> n >> h >> a >> b >> c >> d >> e;
  long long res = c * n;
  for (int i = 0; i < n + 1; i++) {
    long long j = (e * (n - i) - h - b * i) / (d + e) + 1;
    j = max(j, (long long)0);
    if (i + j <= n) {
      res = min(res, a * i + c * j);
    }
  }
  cout << res << '\n';
  return 0;
}
