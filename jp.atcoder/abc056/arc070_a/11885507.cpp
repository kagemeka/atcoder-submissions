#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int x;
  cin >> x;
  int n = int(sqrt(2 * x));
  int ans = ((1 + n) * n / 2 >= x) ? n : n + 1;
  cout << ans << '\n';
  return 0;
}
