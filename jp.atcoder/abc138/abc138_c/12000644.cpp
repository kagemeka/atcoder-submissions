#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n; cin >> n;
  vector<int> v(n);
  for (int i = 0; i < n; i++) cin >> v[i];
  sort(v.begin(), v.end());
  double res = v[0];
  for (int i = 1; i < n; i++) {
    res = (res + v[i]) / 2;
  }
  cout << setprecision(6) << res << '\n';
  return 0;
}
