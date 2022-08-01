#include <bits/stdc++.h>
using namespace std;
auto enumerate_primes(int less_than) -> vector<int> {
  int n = less_than;
  vector<int> primes;
  primes.reserve(n >> 4);
  if(n > 2) primes.push_back(2);
  vector<bool> is_prime(n >> 1, true);
  for(int i = 3; i < n; i += 2) {
    if(!is_prime[i >> 1]) continue;
    primes.push_back(i);
    for(long j = (long)i * i >> 1; j < n >> 1; j += i) is_prime[j] = false;
  }
  return primes;
}
auto least_prime_factor(int size) -> vector<int> {
  vector<int> lpf(size);
  for(auto p: enumerate_primes(size)) lpf[p] = p;
  for(int i = 4; i < size; i += 2) lpf[i] = 2;
  for(int i = 3; i * i < size; i += 2) {
    if(lpf[i] != i) continue;
    for(int j = i * i; j < size; j += i << 1) {
      if(lpf[j] == 0) lpf[j] = i;
    }
  }
  return lpf;
}
struct prime_factorize_with_lpf {
  vector<int> lpf;
  prime_factorize_with_lpf(int size): lpf(least_prime_factor(size)) {}
  auto factorize(int n) -> vector<pair<int, int>> {
    vector<pair<int, int>> factors;
    int prime = 0, cnt = 0;
    while(n > 1) {
      int p = lpf[n];
      n /= p;
      if(p == prime) {
        cnt++;
        continue;
      }
      if(cnt > 0) factors.emplace_back(prime, cnt);
      prime = p, cnt = 1;
    }
    if(cnt > 0) factors.emplace_back(prime, cnt);
    return factors;
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const k = 1 << 20;
  prime_factorize_with_lpf f(k);
  vector<int> c(k);
  for(auto& x: a) {
    for(auto [p, e]: f.factorize(x)) { c[p]++; }
  }
  bool ok = true;
  for(int i = 0; i < k; i++) {
    if(c[i] >= 2) {
      ok = false;
      break;
    }
  }
  if(ok) {
    cout << "pairwise coprime" << endl;
    return 0;
  }
  ok = true;
  for(int i = 0; i < k; i++) {
    if(c[i] == n) ok = false;
  }
  if(ok) {
    cout << "setwise coprime" << endl;
  } else {
    cout << "not coprime" << endl;
  }
}
