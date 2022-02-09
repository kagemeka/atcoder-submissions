#include <bits/stdc++.h>
using namespace std;
int MOD = 2019;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int l, r;
  cin >> l >> r;
  r = min(r, l + 2018);

  int res = MOD;
  for (int i = l; i < r; i++) {
    for (int j = i + 1; j < r + 1; j++) {
      int a = i % MOD;
      int b = j % MOD;
      res = min(res, a * b % MOD);
    }
  }
  cout << res << '\n';
  return 0;
}
