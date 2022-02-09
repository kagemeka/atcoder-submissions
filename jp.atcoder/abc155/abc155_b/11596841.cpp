#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  string ans = "APPROVED";
  for (int i = 0; i < n; i++) {
    if (a[i] & 1) continue;
    if (a[i] % 3 == 0 || a[i] % 5 == 0) continue;
    ans = "DENIED";
    break;
  }
  cout << ans << '\n';
  return 0;
}
