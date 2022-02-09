#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  vector<vector<int>> x(2, vector<int>(2));
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 2; j++) {
      cin >> x[i][j];
    }
  }

  string ans = "NO";
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 2; j++) {
      if (x[0][i] == x[1][j]) {
        ans = "YES";
        break;
      }
    }
  }
  cout << ans << '\n';
  return 0;
}
