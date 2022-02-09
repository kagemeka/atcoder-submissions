#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int d, n;
  cin >> d >> n;
  int res = pow(100, d) * n;
  if (n == 100) res += pow(100, d);
  cout << res << '\n';
  return 0;
}
