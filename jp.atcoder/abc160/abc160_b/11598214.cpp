#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int x;
  cin >> x;
  int q, r;
  q = x / 500;
  r = x % 500;
  int res = q * 1000 + r / 5 * 5;
  cout << res << '\n';
  return 0;
}
