#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  long long a, b, c;
  cin >> a >> b >> c;

  long long v = a * b % MOD * c % MOD;
  cout << v << '\n';
  return 0;
}
