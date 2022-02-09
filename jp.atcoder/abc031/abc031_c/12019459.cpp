#include <bits/stdc++.h>
using namespace std;
int INF = 1001001;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> a(n + 1);
  for (int i = 1; i < n + 1; i++) cin >> a[i];
  auto se = a, so = a;
  for (int i = 0; i < n - 1; i += 2) se[i+2] += se[i];
  for (int i = 0; i < n; i += 2) se[i+1] = se[i];
  for (int i = 1; i < n - 1; i += 2) so[i+2] += so[i];
  for (int i = 1; i < n; i += 2) so[i+1] = so[i];

  int ans = -1001001;
  for (int i = 1; i < n + 1; i++) {
    int score = -1001001;
    int res;
    for (int j = 1; j < n + 1; j++) {
      if (i == j) continue;
      int x = i, y = j;
      if (x > y) swap(x, y);
      int s1 = so[y] - so[x-1];
      int s2 = se[y] - se[x-1];
      if (!(x & 1)) swap(s1, s2);
      if (s2 > score) {
        score = s2;
        res = s1;
      }
    }
    ans = max(ans, res);
  }
  cout << ans << '\n';
  return 0;
}
