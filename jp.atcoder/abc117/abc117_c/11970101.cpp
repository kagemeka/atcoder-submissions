#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m; cin >> n >> m;
  vector<int> x(m);
  for (int i = 0; i < m; i++) cin >> x[i];
  sort(x.begin(), x.end());
  vector<int> d(m);
  for (int i = 0; i < m - 1; i++) {
    d[i+1] = x[i+1] - x[i];
  }
  sort(d.begin()+1, d.end(), greater<int>());
  for (int i = 0; i < m - 1; i++) d[i+1] += d[i];
  int res = d[m-1] - d[min(n, m)-1];
  cout << res << '\n';
  return 0;
}
