#include <bits/stdc++.h>
using namespace std;

long long pow2(long long x, long long y, int mod=0) {
  long long res = 1;
  if (mod) {
    while (y) {if (y & 1) res = res * x % mod; y >>= 1; x = x * x % mod;}
  } else {
    while (y) {if (y & 1) res *= x; y >>= 1; x *= x;}
  }
  return res;
}

int f(long long a, long long b) {
  return pow2(a, 5) - pow2(b, 5);
}

vector<long long> divisors(long long n) {
  vector<long long> res;
  for (int i = 1; i < (int)sqrt(n) + 1; i++) {
    if (n % i == 0) {
      res.push_back(i);
      if (n / i != i) res.push_back(i);
    }
  }
  sort(res.begin(), res.end());
  return res;
}

int x;

int ternary_search(int d) {
  int lo = -1, hi = 1e3;
  while (lo + 1 < hi) {
    int a = (lo + hi) / 2;
    int b = a - d;
    bool bl1 = f(a, b) >= x;
    bool bl2 = a >= abs(b);
    (bl1 ^ bl2) ? lo = a: hi = a;
  }
  return hi;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> x;
  for (auto d: divisors(x)) {
    int a = ternary_search(d);
    int b = a - d;
    if (f(a, b) == x) {
      printf("%d %d\n", a, b);
      return 0;
    }
  }
}
