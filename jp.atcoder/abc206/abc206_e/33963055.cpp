#include <bits/stdc++.h>
using namespace std;
auto enumerate_primes(long n) -> vector<int> {
  vector<bool> is_prime(n, true);
  for(long i = 2; i * i < n; i++) {
    if(!is_prime[i]) continue;
    for(long j = i * i; j < n; j += i) is_prime[j] = false;
  }
  vector<int> res;
  for(int i = 2; i < n; i++)
    if(is_prime[i]) res.push_back(i);
  return res;
}
auto main() -> int {
  int l, r;
  cin >> l >> r;
  l = max(l, 2);
  int const k = 1 << 20;
  vector<long> f(k);
  for(int i = l; i <= r; i++) f[i] = 1;
  auto primes = enumerate_primes(k);
  auto zeta = [&](vector<long> f) -> vector<long> {
    int n = f.size() - 1;
    for(auto& p: primes) {
      for(int i = n / p; i >= 1; i--) { f[i] += f[i * p]; }
    }
    return f;
  };
  auto mobius = [&](vector<long> f) -> vector<long> {
    int n = f.size() - 1;
    for(auto& p: primes) {
      for(int i = 1; i <= n / p; i++) { f[i] -= f[i * p]; }
    }
    return f;
  };
  auto convolve = [&](vector<long> f, vector<long> g) -> vector<long> {
    f = zeta(f);
    g = zeta(g);
    for(int i = 0; i < (int)f.size(); i++) { f[i] *= g[i]; }
    return mobius(f);
  };
  f = convolve(f, f);
  long s = 0;
  for(int i = 2; i <= r; i++) {
    s += f[i];
    if(i >= l) s -= r / i * 2 - 1;
  }
  cout << s << endl;
}
