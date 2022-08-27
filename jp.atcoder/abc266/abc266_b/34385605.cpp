#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n;
  cin >> n;
  long const mod = 998244353;
  n %= mod;
  n = (n + mod) % mod;
  cout << n << endl;
}
