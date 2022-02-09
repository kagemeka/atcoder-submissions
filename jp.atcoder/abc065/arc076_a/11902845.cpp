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

int MOD = 1e9 + 7;
int U = 1e7;
vector<unsigned long long> fac(U + 1);
vector<unsigned long long> ifac(U + 1);
vector<unsigned long long> n_choose(U + 1);
void make_tables(int n=1e9, int p=MOD) {
  fac[0] = 1;
  for (int i = 0; i < U; i++) fac[i+1] = fac[i] * (i + 1) % p;
  ifac[U] = pow2(fac[U], p - 2, p);
  for (int i = U; i > 0; i--) ifac[i-1] = fac[i] * i % p;
  n_choose[0] = 1;
  for (int i = 0; i < U; i++) n_choose[i+1] = n_choose[i] * (n - i) % p;
  for (int i = 0; i < U + 1; i++) n_choose[i] = n_choose[i] * ifac[i] % p;
}

int mod_choose(int n, int r, int p=MOD) {
  if (r > n || r < 0) return 0;
  return fac[n] * ifac[r] % p * ifac[n-r] % p;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  make_tables();
  int n, m;
  cin >> n >> m;
  int ans;
  int d = abs(n - m);
  if (d >= 2) ans = 0;
  else if (d == 1) ans = fac[n] * fac[m] % MOD;
  else ans = fac[n] * fac[m] * 2 % MOD;
  cout << ans << '\n';
  return 0;
}
