#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m, x;
  cin >> n >> m >> x;
  vector<int> a(m);
  for (int i = 0; i < m; i++) {
    cin >> a[i];
  }
  int i = lower_bound(a.begin(), a.end(), x) - a.begin();
  cout << min(i, m - i) << '\n';
  return 0;
}
