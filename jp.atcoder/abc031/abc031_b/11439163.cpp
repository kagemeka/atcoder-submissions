#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int l, h, n;
  cin >> l >> h >> n;
  int a;
  int ans;
  for (int i = 0; i < n; i++) {
    cin >> a;
    if (a > h) {ans = -1;}
    else {ans = max(l - a, 0);}
    cout << ans << '\n';
  }
  return 0;
}
