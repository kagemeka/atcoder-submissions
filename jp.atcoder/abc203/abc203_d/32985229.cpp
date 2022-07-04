#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  // binary search median;

  int n, k;
  cin >> n >> k;

  vector<vector<int>> a(n, vector<int>(n));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> a[i][j];
    }
  }

  int border = k * k / 2 + 1;
  auto possible = [&](int x) -> bool {
    vector<vector<int>> s(n + 1, vector<int>(n + 1, 0));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        s[i + 1][j + 1] = a[i][j] >= x;
      }
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n + 1; j++) {
        s[i + 1][j] += s[i][j];
      }
    }
    for (int j = 0; j < n; j++) {
      for (int i = 0; i < n + 1; i++) {
        s[i][j + 1] += s[i][j];
      }
    }

    for (int i = k; i < n + 1; i++) {
      for (int j = k; j < n + 1; j++) {
        if (s[i][j] - s[i - k][j] - s[i][j - k] + s[i - k][j - k] < border)
          return false;
      }
    }
    return true;
  };

  int ok = 0, ng = 1 << 30;
  while (ng - ok > 1) {
    int x = (ng + ok) >> 1;
    if (possible(x)) ok = x;
    else ng = x;
  }
  cout << ok << endl;
}
