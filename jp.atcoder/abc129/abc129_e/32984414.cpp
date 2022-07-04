#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  string s;
  cin >> s;

  const int mod = 1000000007;

  long x = 1, y = 0;

  for (auto& c : s) {
    int d = c - '0';
    y *= 3;
    if (d == 1) {
      y += x;
      x *= 2;
    }
    x %= mod, y %= mod;
  }
  cout << (x + y) % mod << endl;
}
