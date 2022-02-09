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
  int c1 = n / k;
  long long cnt;
  if (k & 1) {
    cnt = pow(c1, 3);
  } else {
    int c2 = n / (k / 2);
    cnt = pow2(c1, 3) + pow2(c2 - c1, 3);
  }
  cout << cnt << '\n';
  return 0;
}
