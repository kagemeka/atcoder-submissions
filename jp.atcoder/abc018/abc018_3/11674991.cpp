#include <bits/stdc++.h>
using namespace std;
int INF = numeric_limits<int>::max();

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int r, c, k;
  cin >> r >> c >> k;
  vector<vector<int>> res(r + 2, vector<int>(c + 2));
  for (int i = 1; i < r + 1; i++) {
    for (int j = 1; j < c + 1; j++) {
      char cell;
      cin >> cell;
      res[i][j] = (cell == 'o') * INF;
    }
  }
  for (int i = 1; i < r + 1; i++) {
    for (int j = 1; j < c + 1; j++) {
      res[i][j] = min(res[i][j-1] + 1, res[i][j]);
    }
  }
  for (int i = 1; i < r + 1; i++) {
    for (int j = c; j > 0; j--) {
      res[i][j] = min(res[i][j+1] + 1, res[i][j]);
    }
  }
  for (int j = 1; j < c + 1; j++) {
    for (int i = 1; i < r + 1; i++) {
      res[i][j] = min(res[i-1][j] + 1, res[i][j]);
    }
  }
  for (int j = 1; j < c + 1; j++) {
    for (int i = r; i > 0; i--) {
      res[i][j] = min(res[i+1][j] + 1, res[i][j]);
    }
  }
  int cnt = 0;
  for (int i = 1; i < r + 1; i++) {
    for (int j = 1; j < c + 1; j++) {
      cnt += res[i][j] >= k;
    }
  }
  cout << cnt << '\n';
  return 0;
}
