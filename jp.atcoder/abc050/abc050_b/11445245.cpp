#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> t(n);
  for (int i = 0; i < n; i++) {
    cin >> t[i];
  }
  int m;
  cin >> m;
  int tot = accumulate(t.begin(), t.end(), 0);
  int p, x;
  for (int i = 0; i < m; i++) {
    cin >> p >> x;
    cout << tot + (x - t[p-1]) << '\n';
  }
  return 0;
}
