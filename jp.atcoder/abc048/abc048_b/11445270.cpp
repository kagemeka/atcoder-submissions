#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  long long a, b, x;
  cin >> a >> b >> x;

  long long ans = (a == 0) ? b / x + 1 : b / x - (a - 1) / x;
  cout << ans << '\n';
  return 0;
}
