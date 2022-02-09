#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<vector<int>> graph(n, vector<int>(n));
  for (int i = 0; i < n; i++) {
    int a; cin >> a;
    int res = 0;
    for (int j = 0; j < a; j++) {
      int x, y; cin >> x >> y;
      graph[i][x-1] = y + 1;
    }
  }

  int ans = 0;
  for (int i = 0; i < (1 << n); i++) {
    bitset<1001> res(i);
    bool flag = false;
    for (int j = 0; j < n; j++) {
      if (!res[j]) continue;
      for (int k = 0; k < n; k++) {
        int vote = graph[j][k];
        if ((res[k] && vote == 1) or (!res[k] && vote == 2)) {
          flag = true;
          break;
        }
      }
      if (flag) break;
    }
    if (!flag) ans = max(ans, (int)res.count());
  }
  cout << ans << '\n';
  return 0;
}
