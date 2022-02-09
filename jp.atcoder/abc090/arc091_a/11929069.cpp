#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  long long n, m; cin >> n >> m;
  if (n > m) swap(n, m);
  long long ans;
  ans = (n == 1) ? abs(m - 2) : (n - 2) * (m - 2);
  cout << ans << '\n';
  return 0;
}
