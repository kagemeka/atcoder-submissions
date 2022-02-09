#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  vector<vector<int>> d(n + 1, vector<int>(n + 1));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> d[i + 1][j + 1];
    }
  }
  int q;
  cin >> q;
  vector<int> p(q);
  for (int i = 0; i < q; i++) cin >> p[i];

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n + 1; j++) {
      d[i + 1][j] += d[i][j];
    }
  }
  for (int j = 0; j < n; j++) {
    for (int i = 0; i < n + 1; i++) {
      d[i][j + 1] += d[i][j];
    }
  }

  vector<int> res(n * n + 1);
  for (int y = 1; y < n + 1; y++) {
    for (int x = 1; x < n + 1; x++) {
      int mx = 0;
      for (int i = y; i < n + 1; i++) {
        for (int j = x; j < n + 1; j++) {
          mx = max(mx, d[i][j] - d[i - y][j] - d[i][j - x] + d[i - y][j - x]);
        }
      }
      res[y * x] = max(res[y * x], mx);
    }
  }
  for (int i = 0; i < n * n; i++) res[i + 1] = max(res[i + 1], res[i]);
  for (const int &x : p) {cout << res[x] << '\n';}
}
