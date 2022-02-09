#include <bits/stdc++.h>
using namespace std;
int INF = 1001001;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> a(n + 1);
  for (int i = 1; i < n + 1; i++) cin >> a[i];
  vector<int> s = a;
  for (int i = 0; i < n; i++) s[i+1] += s[i];

  int ans = -INF;
  for (int i = 1; i < n + 1; i++) {
    vector<vector<int>> res;
    for (int j = 1; j < n + 1; j++) {
      if (i == j) continue;
      int l = min(i, j), r = max(i, j);
      int tmp = 0;
      for (int k = l + 1; k <= r; k += 2) {
        tmp += a[k];
      }
      res.push_back({tmp, s[r] - s[l-1] - tmp});
    }
    sort(res.begin(), res.end(), greater<vector<int>>());
    ans = max(ans, res[0][1]);
  }
  cout << ans << '\n';
  return 0;
}
