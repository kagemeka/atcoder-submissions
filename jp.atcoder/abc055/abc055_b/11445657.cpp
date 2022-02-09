#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;

  long long p = 1;
  for (int i = 1; i <= n; i++) {
    p *= i;
    p %= MOD;
  }
  cout << p << '\n';
  return 0;
}
