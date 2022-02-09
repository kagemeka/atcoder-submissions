#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  int tot = 0;
  vector<int> res(m + 1, 0);
  for (int i = 0; i < n; i++) {
    int l, r, s;
    cin >> l >> r >> s;
    l--; r--;
    tot += s;
    res[l] += s;
    res[r+1] -= s;
  }
  for (int i = 0; i < m; i++) {
    res[i+1] += res[i];
  }
  int ans = tot - *min_element(res.begin(), res.end() - 1);
  cout << ans << '\n';
  return 0;
}
