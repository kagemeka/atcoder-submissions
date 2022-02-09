#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  int m = 101;
  int s = 0;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    s += a;
    if (a % 10) m = min(m, a);
  }
  int ans;
  if (s % 10) ans = s;
  else if (m == 101) ans = 0;
  else ans = s - m;
  cout << ans << '\n';
  return 0;
}
