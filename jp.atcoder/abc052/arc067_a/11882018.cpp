#include <bits/stdc++.h>
using namespace std;

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
  for (int i = 2; i < n + 1; i++) {
    for (auto &pc : prime_factorize(i)) {
      if (res.find(pc.first) == res.end()) res[pc.first] = pc.second;
      else res[pc.first] += pc.second;
    }
  }
  return res;
}

int MOD = 1e9 + 7;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  sieve_of_eratosthenes(1e7);
  long long res = 1;
  for (auto &pc : prime_factorize_factorial(n)) {
    res *= pc.second + 1; res %= MOD;
  }
  cout << res << '\n';
  return 0;
}
