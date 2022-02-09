#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  vector<string> canvas(n);
  for (int i = 0; i < n; i++) cin >> canvas[i];
  vector<string> target(m);
  for (int i = 0; i < m; i++) cin >> target[i];

  bool flag = false;
  for (int i = 0; i < n - m + 1; i++) {
    for (int j = 0; j < n - m + 1; j++) {
      for (int y = 0; y < m; y++) {
        for (int x = 0; x < m; x++) {
          if (canvas[i+y][j+x] == target[y][x]) continue;
          flag = true;
          break;
        }
        if (flag) break;
      }
      if (flag) continue;
      cout << "Yes" << '\n';
      return 0;
    }
  }
  cout << "No" << '\n';
  return 0;
}
