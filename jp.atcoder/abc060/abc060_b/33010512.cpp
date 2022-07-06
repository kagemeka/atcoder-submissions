#include <bits/stdc++.h>
using namespace std;

auto gcd(int a, int b) -> int { return !b ? a : gcd(b, a % b); }

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int a, b, c;
  cin >> a >> b >> c;

  cout << (c % gcd(a, b) == 0 ? "YES" : "NO") << endl;
}