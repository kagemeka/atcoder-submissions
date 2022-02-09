#include <bits/stdc++.h>
using namespace std;

long long mod_pow(long long x, int n, int mod) {
  if (n == 0) return 1;
  if (n & 1) return x * mod_pow(x, n - 1, mod) % mod;
  long long h = mod_pow(x, n / 2, mod);
  return h * h % mod;
}

int MOD = 1e9 + 7;
int U = 2 * 1e5;
vector<long long> fac(U + 1, 0);
vector<long long> ifac(U + 1, 0);
void make_fac_ifac(int n=U, int p=MOD) {
  fac[0] = 1;
  for (int i = 0; i < n; i++) {
    fac[i+1] = fac[i] * (i + 1) % p;
  }
  ifac[n] = mod_pow(fac[n], p - 2, p);
  for (int i = n; i > 0; i--) {
    ifac[i-1] = ifac[i] * i % p;
  }
}
int mod_choose(int n, int r,int p=MOD) {
  return fac[n] * ifac[r] % p * ifac[n-r] % p;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  make_fac_ifac();
  int h, w;
  cin >> h >> w;
  cout << mod_choose(h + w - 2, h - 1) << '\n';
  return 0;
}
