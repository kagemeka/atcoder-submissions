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
  for (int i = U; i > 0; i--) ifac[i-1] = ifac[i] * i % p;
  n_choose[0] = 1;
  for (int i = 0; i < U; i++) n_choose[i+1] = n_choose[i] * (n - i) % p;
  for (int i = 0; i < U + 1; i++) n_choose[i] = n_choose[i] * ifac[i] % p;
}

int mod_choose(int n, int r, int p=MOD) {
  if (r > n || r < 0) return 0;
  return fac[n] * ifac[r] % p * ifac[n-r] % p;
}

bitset<1001001001> is_prime(0);
vector<int> prime_numbers;
void sieve_of_eratosthenes(int n=1e7) {
  for (int i = 2; i < n + 1; i++) {is_prime.set(i);}
  for (int i = 2; i < (int)sqrt(n) + 1; i++) {
    if (is_prime[i]) for (int j = i * 2; j < n + 1; j += i) is_prime.reset(j);
  }
  for (int i = 2; i < n + 1; i++) if (is_prime[i]) prime_numbers.push_back(i);
}

unordered_map<int, int> prime_factorize(int n) {
  unordered_map<int, int> res;
  if (n < 2) return res;
  int border = int(sqrt(n));
  for (int &p : prime_numbers) {
    if (p > border) break;
    if (n % p == 0) {
      res[p] = 1; n /= p;
      while (n % p == 0) {res[p]++; n /= p;}
    }
    if (n == 1) return res;
  }
  res[n] = 1; return res;
}

unordered_map<int, int> prime_factorize_factorial(int n) {
  unordered_map<int, int> res;
  for (int i = 1; i < n + 1; i++) {
    for (auto &pc : prime_factorize(i)) {
      if (res.find(pc.first) == res.end()) res[pc.first] = pc.second;
      else res[pc.first] += pc.second;
    }
  }
  return res;
}

long long nHr(int n, int r) {
  return mod_choose(n-1+r, r);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  make_tables();
  sieve_of_eratosthenes();

  int n, m; cin >> n >> m;
  long long res = 1;
  for (auto p: prime_factorize(m)) {
    res *= nHr(n, p.second);
    res %= MOD;
  }
  cout << res << '\n';
  return 0;
}
