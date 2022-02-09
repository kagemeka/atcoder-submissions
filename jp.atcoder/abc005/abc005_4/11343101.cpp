#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<vector<int>> d(n+1, vector<int>(n+1, 0));
  for (int i = 1; i < n + 1; i++) {
    for (int j = 1; j < n + 1; j++) {
      cin >> d[i][j];
    }
  }
  int q;
  cin >> q;
  vector<int> p(q);
  for (int i = 0; i < q; i++) {
    cin >> p[i];
  }

  for (int i = 1; i < n + 1; i++) {
    for (int j = 0; j < n; j++) {
      d[i][j+1] += d[i][j];
    }
  }

  for (int j = 1; j < n + 1; j++) {
    for (int i = 0; i < n; i++) {
      d[i+1][j] += d[i][j];
    }
  }

  vector<vector<int>> maximum(n+1, vector<int>(n+1, 0));
  for (int y = 1; y <= n; y++) {
    for (int x = 1; x <= n; x++) {
      for (int i = y; i < n + 1; i++) {
        for (int j = x; j < n + 1; j++) {
          int deliciousness = d[i][j] - d[i-y][j] - d[i][j-x] + d[i-y][j-x];
          maximum[y][x] = max(maximum[y][x], deliciousness);
        }
      }
    }
  }

  vector<int> res(pow(n, 2)+1);
  for (int y = 1; y <= n; y++) {
    for (int x = 1; x <= n; x++) {
      res[y*x] = max(res[y*x], maximum[y][x]);
    }
  }
  for (int i = 1; i < res.size(); i++) {
    res[i] = max(res[i], res[i-1]);
  }

  for (int x : p) {
    cout << res[x] << endl;
  }
  return 0;
}
