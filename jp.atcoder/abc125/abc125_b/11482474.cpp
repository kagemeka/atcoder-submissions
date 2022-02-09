#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> v(n);
  vector<int> c(n);
  for (int i = 0; i < n; i++) cin >> v[i];
  for (int i = 0; i < n; i++) cin >> c[i];
  int res = 0;
  for (int i = 0; i < n; i++) {
    res += max(0, v[i] - c[i]);
  }
  cout << res << '\n';
  return 0;
}
