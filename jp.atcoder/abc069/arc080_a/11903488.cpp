#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  int c2 = 0;
  int c4 = 0;
  for (auto &x : a) {
    if (x % 4 == 0) c4++;
    else if (x % 2 == 0) c2++;
  }
  string ans = (c4 >= n / 2 || c4 * 2 + c2 >= n) ? "Yes" : "No";
  cout << ans << '\n';
  return 0;
}
