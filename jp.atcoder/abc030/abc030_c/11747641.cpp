#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m, x, y;
  cin >> n >> m >> x >> y;
  vector<int> a(n);
  vector<int> b(m);
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < m; i++) cin >> b[i];

  long long t = 0;
  int cnt = 0;
  long long flight;
  while (true) {
    flight = *lower_bound(a.begin(), a.end(), t);
    if (!flight) break;
    t = flight + x;
    flight = *lower_bound(b.begin(), b.end(), t);
    if (!flight) break;
    t = flight + y;
    cnt++;
  }
  cout << cnt << '\n';
  return 0;
}
