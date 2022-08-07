#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n;
  cin >> n;
  long const mod = 998244353;
  long p = 1;
  long s = 0;
  long inv = (mod + 1) >> 1;
  auto f = [&](long x) -> long {
    return (1 + x) % mod * (x % mod) % mod * inv % mod;
  };
  while(true) {
    if(p > n) break;
    long pp = p * 10;
    s += f(min(pp, n + 1) - p);
    p = pp;
  }
  cout << s % mod << endl;
}
