#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  long s = 0;
  long t = 0;
  long const mod = 1000000007;
  for(int i = 0; i < n; i++) {
    long x;
    cin >> x;
    s += x;
    t += x * x;
    s %= mod;
    t %= mod;
  }
  long inv = (mod + 1) >> 1;
  s *= s;
  s %= mod;
  s -= t;
  s *= inv;
  s %= mod;
  s += mod;
  s %= mod;
  cout << s << endl;
}
