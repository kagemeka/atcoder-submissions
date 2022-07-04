#include <bits/stdc++.h>

using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, t;
  cin >> n >> t;

  vector<pair<int, int>> ab;
  for (int i = 0; i < n; i++) {
    int a, b;
    cin >> a >> b;
    ab.emplace_back(a, b);
  }

  vector<vector<int>> dp_l(n + 1, vector<int>(t, 0)),
      dp_r(n + 1, vector<int>(t, 0));
  for (int i = 0; i < n; i++) {
    {
      auto [a, b] = ab[i];
      for (int j = 0; j < a; j++) {
        dp_l[i + 1][j] = dp_l[i][j];
      }
      for (int j = 0; j < t - a; j++) {
        dp_l[i + 1][j + a] = max(dp_l[i][j + a], dp_l[i][j] + b);
      }
    }
    {
      auto [a, b] = ab[n - 1 - i];
      for (int j = 0; j < a; j++) {
        dp_r[i + 1][j] = dp_r[i][j];
      }
      for (int j = 0; j < t - a; j++) {
        dp_r[i + 1][j + a] = max(dp_r[i][j + a], dp_r[i][j] + b);
      }
    }
  }

  int mx = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < t; j++) {
      int v = dp_l[i][j] + dp_r[n - 1 - i][t - 1 - j] + ab[i].second;
      mx = max(mx, v);
    }
  }

  cout << mx << endl;
}
