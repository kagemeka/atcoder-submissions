#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m; cin >> n >> m;
  vector<int> x(m);
  for (int i = 0; i < m; i++) cin >> x[i];
  int res = 0;
  if (n >= m) res = 0;
  else {
    vector<int> d(m-1);
    sort(x.begin(), x.end());
    for (int i = 0; i < m - 1; i++) {
      d[i] = x[i+1] - x[i];
    }
    sort(d.begin(), d.end(), greater<int>());
    res = d[m-2];
    if (n != 1) {
      for (int i = 0; i < m - 2; i++) d[i+1] += d[i];
      res -= d[n-2];
    }
  }
  cout << res << '\n';
  return 0;
}
