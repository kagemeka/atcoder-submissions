#include <bits/stdc++.h>
using namespace std;

int MOD = 1e9 + 7;
long long mod_pow(long long x, int n, int mod) {
  if (n == 0) return 1;
  if (n & 1) return x * mod_pow(x, n - 1, mod) % mod;
  long long h = mod_pow(x, n / 2, mod);
  return h * h % mod;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> c(n);
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    c[a]++;
  }

  int ans = 0;
  if (n % 2 == 0 || c[0] == 1) {
    bool flag = true;
    for (int i = 1 + (n & 1); i < n; i += 2) {
      if (c[i] != 2) {
        flag = false;
        break;
      }
    }
    if (flag) ans = mod_pow((long long)2, n / 2, MOD);
  }
  cout << ans << '\n';
  return 0;
}
