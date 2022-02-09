#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> t(n + 1);
  vector<int> x(n + 1);
  vector<int> y(n + 1);
  for (int i = 1; i < n + 1; i++) {
    cin >> t[i] >> x[i] >> y[i];
  }
  string ans = "Yes";
  for (int i = 0; i < n; i++) {
    int dt = t[i+1] - t[i];
    int dd = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i]);
    if (dd > dt || (dd & 1) ^ (dt & 1)) {ans = "No"; break;}
  }
  cout << ans << '\n';
  return 0;

}
