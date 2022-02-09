#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m, x, y;
  cin >> n >> m >> x >> y;
  vector<int> a(n + 1);
  vector<int> b(m + 1);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  for (int i = 0; i < m; i++) {
    cin >> b[i];
  }
  a[n] = x; b[m] = y;
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  string ans = (a[n] < b[0]) ? "No War" : "War";
  cout << ans << '\n';
  return 0;
}
