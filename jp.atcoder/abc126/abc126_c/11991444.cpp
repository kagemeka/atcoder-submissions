#include <bits/stdc++.h>
using namespace std;

long long pow2(long long x, long long n, int mod=0) {
  if (n == 0) return 1;
  if (mod) {
    if (n & 1) return x * pow2(x, n - 1, mod) % mod;
    long long y = pow2(x, n / 2, mod);
    return y * y % mod;
  } else {
    if (n & 1) return x * pow2(x, n - 1);
    long long y = pow2(x, n / 2);
    return y * y;
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, k; cin >> n >> k;
  double res = 0;
  for (int i = 1; i < n + 1; i++) {
    int j = i;
    int denom = 1;
    while (j < k) {
      j *= 2;
      denom *= 2;
    }
    res += 1 / (double)denom;
  }
  res /= n;
  cout << setprecision(10) << res << '\n';
  return 0;

}
