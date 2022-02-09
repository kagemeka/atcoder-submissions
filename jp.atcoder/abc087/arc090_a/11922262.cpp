#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> a(n + 1);
  vector<int> b(n + 1);
  for (int i = 1; i < n + 1; i++) cin >> a[i];
  for (int i = 1; i < n + 1; i++) cin >> b[i];
  for (int i = 0; i < n; i++) {
    a[i+1] += a[i]; b[i+1] += b[i];
  }
  int res = 0;
  for (int i = 1; i < n + 1; i++) {
    res = max(res, a[i] + b[n] - b[i-1]);
  }
  cout << res << '\n';
  return 0;

}
