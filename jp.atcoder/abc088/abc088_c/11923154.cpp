#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  vector<vector<int>> grid(3, vector<int>(3));
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      cin >> grid[i][j];
    }
  }
  for (int i = 0; i < 3; i++) {
    for (int j = 2; j > -1; j--) {
      grid[i][j] -= grid[i][0];
    }
  }
  for (int j = 0; j < 3; j++) {
    for (int i = 2; i > -1; i--) {
      grid[i][j] -= grid[0][j];
    }
  }
  string ans = "Yes";
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      if (grid[i][j]) {
        ans = "No";
        break;
      }
    }
  }
  cout << ans << '\n';
  return 0;
}
